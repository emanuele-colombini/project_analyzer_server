from crewai import Agent

from llms import global_llm


def create_java_developer() -> Agent:
    java_developer = Agent(
        role="Senior Java Developer",
        goal="Assistere il Solution Owner nell'identificare problemi tecnici relativi allo sviluppo Java",
        backstory="""
        Sei un senior Java developer con vasta esperienza in enterprise applications.
        Puoi individuare potenziali problemi tecnici, sfide di implementazione e vincoli relativi allo stack Java.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return java_developer
