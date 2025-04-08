from crewai import Crew, Process

from business_requests.br_evaluator.team.business_analyst import create_business_analyst
from business_requests.br_evaluator.team.frontend_developer import create_frontend_developer
from business_requests.br_evaluator.team.java_developer import create_java_developer
from business_requests.br_evaluator.team.project_manager import create_project_manager
from business_requests.br_evaluator.team.python_developer import create_python_developer
from business_requests.br_evaluator.team.software_architect import create_software_architect
from business_requests.br_evaluator.team.solution_owner import create_solution_owner, create_evaluation_task
from business_requests.br_data import BusinessRequestModel
from llms import ollama__memory_embedder


def create_br_evaluator_crew(project_name: str) -> Crew:

    # Agents
    solution_owner = create_solution_owner()
    software_architect = create_software_architect()
    business_analyst = create_business_analyst()
    project_manager = create_project_manager()
    java_developer = create_java_developer()
    python_developer = create_python_developer()
    frontend_developer = create_frontend_developer()

    # Tasks
    evaluation_task = create_evaluation_task(
        agent=solution_owner,
        project_name=project_name
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
            evaluation_task
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential
    )
    return crew
