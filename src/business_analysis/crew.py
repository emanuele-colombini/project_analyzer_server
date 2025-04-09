from crewai import Crew, Process

from business_analysis.team.business_analyst import create_business_analyst, create_functional_analysis_task
from business_analysis.team.solution_owner import create_solution_owner
from llms import ollama__memory_embedder


def create_functional_analysis_crew() -> Crew:

    # Agents
    business_analyst = create_business_analyst()
    solution_owner = create_solution_owner()

    # Tasks
    functional_analysis_task = create_functional_analysis_task(
        agent=business_analyst
    )

    # Crew
    crew = Crew(
        agents=[
            business_analyst,
            solution_owner
        ],
        tasks=[
            functional_analysis_task
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential
    )
    return crew
