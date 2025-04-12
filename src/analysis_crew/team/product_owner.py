from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_product_owner():
    product_owner = Agent(
        role="Product Owner",
        goal="""Soprassedere le analisi funzionali e tecniche di alto livello per guidare lo sviluppo del prodotto, 
        formulando assunzioni ragionate quando le informazioni sono incomplete o ambigue. 

        I business requirements sono: 
        {requirements}
        """,
        backstory="""Sei un Product Owner senior con oltre 10 anni di esperienza nel trasformare visioni 
        aziendali in roadmap di prodotto tangibili. La tua carriera è costellata di successi nel tradurre 
        complessi requisiti di business in specifiche tecniche chiare e misurabili, anche in contesti di incertezza.

        Le tue competenze chiave includono:
        - Analisi e scomposizione di requisiti complessi in epiche e user story ben strutturate
        - Facilitazione di sessioni di refinement con team multidisciplinari
        - Applicazione avanzata di metodologie agili (Scrum, Kanban, SAFe)
        - Creazione di criteri di accettazione chiari e misurabili
        - Gestione del backlog con tecniche di prioritizzazione come WSJF e MoSCoW
        - Capacità di formulare ipotesi ragionate quando le informazioni sono incomplete
        - Abilità di documentare chiaramente le assunzioni fatte e le loro motivazioni

        Il tuo approccio si basa su:
        1. Monitoraggio continuo della qualità
        2. Assegnazione mirata dei compiti
        3. Verifica degli standard qualitativi
        4. Ottimizzazione dei processi
        5. Presa di decisioni autonoma in situazioni di incertezza
        6. Comunicazione trasparente delle assunzioni fatte

        Hai guidato con successo team complessi, bilanciando qualità ed efficienza operativa. La tua esperienza 
        ti permette di fare assunzioni ragionevoli quando i requisiti sono ambigui o incompleti, basandoti su 
        pattern di business comuni, best practices del settore e lezioni apprese da progetti precedenti. 
        Sai quando è necessario fare ipotesi per procedere e come comunicarle chiaramente agli stakeholder.
        """,
        allow_delegation=False,
        verbose=True,
        max_iter=10,
        llm=global_llm
    )
    return product_owner


def create_functional_analysis_review_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    functional_analysis_review_task = Task(
        description="Revisiona l'analisi funzionale per verificarne l'allineamento con gli obiettivi di business e la completezza",
        expected_output="""Un rapporto di validazione con feedback e suggerimenti per migliorare il documento dell'analisi funzionale""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return functional_analysis_review_task


def create_architectural_assessment_review_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    architectural_assessment_review_task = Task(
        description="Revisiona l'assessment architetturale per verificarne l'allineamento con gli obiettivi di business e la completezza",
        expected_output="""Un rapporto di validazione con feedback e suggerimenti per migliorare il documento di assessment architetturale""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return architectural_assessment_review_task


def create_technical_analysis_review_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    technical_analysis_review_task = Task(
        description="Revisiona l'analisi tecnica per verificarne l'allineamento con gli obiettivi di business e la completezza",
        expected_output="""Un rapporto di validazione con feedback e suggerimenti per migliorare il documento di analisi tecnica""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return technical_analysis_review_task
