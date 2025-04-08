from crewai import Crew, Process

from src.br_integrator.team.business_analyst import create_business_analyst
from src.br_integrator.team.frontend_developer import create_frontend_developer
from src.br_integrator.team.java_developer import create_java_developer
from src.br_integrator.team.project_manager import create_project_manager
from src.br_integrator.team.python_developer import create_python_developer
from src.br_integrator.team.software_architect import create_software_architect
from src.br_integrator.team.solution_owner import create_solution_owner, create_integration_task
from src.llms import ollama__memory_embedder


def create_br_integrator_crew() -> Crew:

    # Agents
    solution_owner = create_solution_owner()
    software_architect = create_software_architect()
    business_analyst = create_business_analyst()
    project_manager = create_project_manager()
    java_developer = create_java_developer()
    python_developer = create_python_developer()
    frontend_developer = create_frontend_developer()

    # Task
    integration_task = create_integration_task(
        agent=solution_owner
    )

    # Crew
    crew = Crew(
        agents=[
            solution_owner,
            software_architect,
            business_analyst,
            project_manager,
            java_developer,
            python_developer,
            frontend_developer
        ],
        tasks=[
            integration_task
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential
    )
    return crew
