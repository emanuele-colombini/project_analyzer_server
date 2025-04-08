from crewai import Agent

from llms import global_llm


def create_project_manager() -> Agent:
    project_manager = Agent(
        role="ProjectModel Manager",
        goal="Assistere il Solution Owner nell'identificare rischi, vincoli temporali e di risorse",
        backstory="""
        Sei un project manager esperto, specializzato nella pianificazione e nella gestione dei rischi.
        Puoi individuare potenziali problemi di tempistica, allocazione delle risorse e dipendenze non chiarite.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return project_manager
