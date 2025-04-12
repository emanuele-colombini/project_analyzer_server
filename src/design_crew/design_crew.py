from crewai import Crew, Process
from devtools import pprint

from llms import ollama__memory_embedder
from analysis_crew.team.software_architect import (
    create_software_architect,
    create_microservices_documentation_task,
    create_microservices_documentation_validation_task
)


class DesignCrew:
    def __init__(self):
        pass

    def generate_design(self, architectural_assessment, functional_analysis, technical_analysis):

        # Agents
        software_architect = create_software_architect()

        # Tasks
        microservices_documentation_task = create_microservices_documentation_task(
            software_architect
        )
        microservices_documentation_validation_task = create_microservices_documentation_validation_task(
            software_architect,
            microservices_documentation_task
        )

        # Crew
        crew = Crew(
            agents=[
                software_architect
            ],
            tasks=[
                microservices_documentation_task,
                microservices_documentation_validation_task
            ],
            verbose=True,
            memory=True,
            embedder=ollama__memory_embedder,
            process=Process.sequential,
            # process=Process.hierarchical,
            # manager_llm=llm,
            # planning=True,
            # planning_llm=llm
        )

        # Run the crew
        result = crew.kickoff(inputs={
            "architectural_assessment": architectural_assessment,
            "functional_analysis": functional_analysis,
            "technical_analysis": technical_analysis
        })

        pprint(result.pydantic)
