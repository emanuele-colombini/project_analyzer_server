from crewai import Agent

from llms import global_llm


def create_python_developer() -> Agent:
    python_developer = Agent(
        role="Senior Python Developer",
        goal="Assistere il Solution Owner nell'identificare problemi tecnici relativi allo sviluppo Python",
        backstory="""
        Sei un senior Python developer con vasta esperienza in data processing, automazione e applicazioni web.
        Puoi individuare potenziali problemi tecnici, sfide di implementazione e vincoli relativi allo stack Python.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return python_developer
