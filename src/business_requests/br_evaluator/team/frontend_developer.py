from crewai import Agent

from src.llms import global_llm


def create_frontend_developer() -> Agent:
    frontend_developer = Agent(
        role="Senior Frontend Developer",
        goal="Assistere il Solution Owner nell'identificare problemi tecnici relativi allo sviluppo frontend",
        backstory="""
        Sei un senior frontend developer con vasta esperienza in sviluppo frontend e UI/UX.
        Puoi individuare potenziali problemi tecnici, sfide di implementazione e vincoli relativi allo stack Angular e frontend.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return frontend_developer
