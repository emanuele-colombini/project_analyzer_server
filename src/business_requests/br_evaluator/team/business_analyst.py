from crewai import Agent

from llms import global_llm


def create_business_analyst() -> Agent:
    business_analyst = Agent(
        role="Business Analyst",
        goal="Assistere il Solution Owner nell'analisi dei requisiti di business",
        backstory="""
        Sei un analista di business esperto, capace di comprendere i processi aziendali e tradurli in requisiti funzionali.
        Puoi individuare requisiti impliciti, incongruenze logiche e gap nei flussi di processo descritti.
        """,
        verbose=True,
        allow_delegation=False,
        llm=global_llm
    )
    return business_analyst
