from crewai import Agent

from llms import global_llm


def create_software_architect() -> Agent:
    software_architect = Agent(
        role="Software Architect",
        goal="Assistere il Solution Owner nell'identificare potenziali sfide tecniche e architetturali",
        backstory="""
        Sei un architetto software esperto con conoscenza approfondita di diverse tecnologie e pattern architetturali.
        Puoi identificare potenziali problemi tecnici, sfide di integrazione e vincoli architetturali nelle Business Request.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return software_architect
