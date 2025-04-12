from crewai import Crew, Process
from pydantic import BaseModel

from business_requests.br_data import BusinessRequestModel
from functional_analysis.functional.team.business_analyst import (
    create_business_analyst,
    create_functional_specs_task,
    create_initial_analysis_task,
)
from functional_analysis.functional.team.domain_expert import (
    create_domain_expert,
    create_domain_context_task
)

from llms import ollama__memory_embedder


class FunctionalCrewOutputFiles(BaseModel):
    initial_analysis: str
    domain_context: str
    functional_specs: str

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.initial_analysis = data.get('initial_analysis')
        self.domain_context = data.get('domain_context')
        self.functional_specs = data.get('functional_specs')


class FunctionalCrewConfig(BaseModel):
    br_version: int
    br_content: str
    functional_output_path: str
    output_files: FunctionalCrewOutputFiles

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.br_version = data.get('br_version')
        self.br_content = data.get('br_content')
        self.functional_output_path = data.get('functional_output_path')
        self.output_files = FunctionalCrewOutputFiles(**data.get('output_files'))


def _create_functional_analysis_crew(config: FunctionalCrewConfig) -> Crew:

    # Agents
    business_analyst = create_business_analyst()
    domain_expert = create_domain_expert()

    # Tasks
    initial_analysis_task = create_initial_analysis_task(
        agent=business_analyst,
        output_file_path=config.output_files.initial_analysis
    )
    domain_context_task = create_domain_context_task(
        agent=domain_expert,
        output_file_path=config.output_files.domain_context,
        context=[
            initial_analysis_task
        ]
    )
    functional_specs_task = create_functional_specs_task(
        agent=business_analyst,
        output_file_path=config.output_files.functional_specs,
        context=[
            initial_analysis_task,
            domain_context_task
        ]
    )

    # Crew
    crew = Crew(
        agents=[
            business_analyst,
            domain_expert
        ],
        tasks=[
            initial_analysis_task,
            domain_context_task,
            functional_specs_task
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential
    )
    return crew

def generate_functional_analysis(config: FunctionalCrewConfig):

    crew = _create_functional_analysis_crew(config)
    crew.kickoff(inputs={
        "business_request": config.br_content
    })
