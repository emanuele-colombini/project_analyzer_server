from crewai import Process, Crew
from pydantic import BaseModel

from architecture.architecture.team.infrastructure_specialist import (
    create_infrastructure_specialist,
    create_infrastructure_recommendations_task
)
from architecture.architecture.team.integration_specialist import (
    create_integration_specialist,
    create_design_integration_patterns_task
)
from architecture.architecture.team.security_architect import (
    create_security_architect,
    create_design_security_architecture_task
)
from architecture.architecture.team.solution_architect import (
    create_solution_architect,
    create_architecture_approach_task,
    create_design_core_components_task,
    create_final_architecture_document_task
)
from functional_analysis.ba_service import ba_service
from functional_analysis.functional.crew import FunctionalCrewConfig
from llms import ollama__memory_embedder
from utils import read_markdown_file


class ArchitectureCrewOutputFiles(BaseModel):
    architecture_approach: str
    core_components: str
    integration_pattern: str
    infrastructure_recommendations: str
    security_architecture: str
    architecture_document: str

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.architecture_approach = data.get('architecture_approach')
        self.core_components = data.get('core_components')
        self.integration_pattern = data.get('integration_pattern')
        self.infrastructure_recommendations = data.get('infrastructure_recommendations')
        self.security_architecture = data.get('security_architecture')
        self.architecture_document = data.get('architecture_document')


class ArchitectureCrewConfig(BaseModel):
    br_version: int
    br_content: str
    architecture_output_path: str
    output_files: ArchitectureCrewOutputFiles

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.br_version = data.get('br_version')
        self.br_content = data.get('br_content')
        self.architecture_output_path = data.get('architecture_output_path')
        self.output_files = ArchitectureCrewOutputFiles(**data.get('output_files'))


def _create_architecture_crew(config: ArchitectureCrewConfig) -> Crew:

    # Agents
    solution_architect = create_solution_architect()
    integration_specialist = create_integration_specialist()
    infrastructure_specialist = create_infrastructure_specialist()
    security_specialist = create_security_architect()

    # Tasks
    determine_architecture_approach = create_architecture_approach_task(
        agent=solution_architect,
        output_file_path=config.output_files.architecture_approach
    )
    design_core_components = create_design_core_components_task(
        agent=solution_architect,
        output_file_path=config.output_files.core_components,
        context=[
            determine_architecture_approach
        ]
    )
    design_integration_patterns = create_design_integration_patterns_task(
        agent=integration_specialist,
        output_file_path=config.output_files.integration_pattern,
        context=[
            determine_architecture_approach,
            design_core_components
        ]
    )
    recommend_infrastructure = create_infrastructure_recommendations_task(
        agent=infrastructure_specialist,
        output_file_path=config.output_files.infrastructure_recommendations,
        context=[
            determine_architecture_approach,
            design_core_components,
            design_integration_patterns
        ]
    )
    create_security_architecture = create_design_security_architecture_task(
        agent=security_specialist,
        output_file_path=config.output_files.security_architecture,
        context=[
            determine_architecture_approach,
            design_core_components,
            design_integration_patterns,
            recommend_infrastructure
        ]
    )
    create_architecture_document = create_final_architecture_document_task(
        agent=solution_architect,
        output_file_path=config.output_files.architecture_document,
        context=[
            determine_architecture_approach,
            design_core_components,
            design_integration_patterns,
            recommend_infrastructure,
            create_security_architecture
        ]
    )

    # Crew
    crew = Crew(
        agents=[
            solution_architect,
            integration_specialist,
            infrastructure_specialist,
            security_specialist
        ],
        tasks=[
            determine_architecture_approach,
            design_core_components,
            design_integration_patterns,
            recommend_infrastructure,
            create_security_architecture,
            create_architecture_document
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential
    )
    return crew

def generate_architecture_analysis(arch_config: ArchitectureCrewConfig, func_config: FunctionalCrewConfig):

    initial_analysis = read_markdown_file(func_config.output_files.initial_analysis)
    domain_context = read_markdown_file(func_config.output_files.domain_context)
    functional_specs = read_markdown_file(func_config.output_files.functional_specs)

    crew = _create_architecture_crew(arch_config)
    crew.kickoff(inputs={
        "business_request": arch_config.br_content,
        "initial_analysis": initial_analysis,
        "domain_context": domain_context,
        "functional_specs": functional_specs
    })
