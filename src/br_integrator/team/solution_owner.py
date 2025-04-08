from crewai import Agent, Task

from src.llms import global_llm


def create_solution_owner() -> Agent:
    solution_owner = Agent(
        role="Solution Owner",
        goal="Unire la Business Request originale con le risposte del cliente per creare un documento completo e pronto per l'analisi",
        backstory="""
        Sei un esperto Solution Owner con anni di esperienza nella gestione di documenti di requisiti.
        La tua specialità è integrare informazioni provenienti da diverse fonti per creare documenti di requisiti completi e coerenti.
        Sei abile nel sintetizzare le risposte dei clienti con i documenti originali, mantenendo la struttura logica e migliorando la chiarezza.
        Sai identificare dove inserire le nuove informazioni nel documento originale per massimizzare la comprensibilità.
        Puoi ricevere l'aiuto da parte di tutta la tua crew, formata da:
        - Software Architect
        - Business Analyst
        - ProjectModel Manager
        - Java Developer
        - Python Developer
        - Frontend Developer
        """,
        verbose=True,
        allow_delegation=True,
        llm=global_llm
    )
    return solution_owner


def create_integration_task(agent: Agent) -> Task:
    integration_task = Task(
        description="""Riscrivi i business request (BR) integrando il contenuto con le risposte ricevute dal cliente 
        Non limitarti a modificare il documento originale, ma creane uno nuovo che incorpori  tutte le indicazioni 
        ricevute, sfruttando l'aiuto possibile dagli altri membri della crew quando necessario.
        
        Business Request originale:
        {business_request}
        
        Risposte del cliente:
        {client_responses}
        
        """,
        expected_output="""Una versione completamente riscritta dei business_request (BR) che unisca i BR originali con
        le risposte arrivate da parte del cliente. Mantieni la struttura della risposta originale correggendo il contenuto
        usando le informazioni ricevuto dalle risposte.
        
        NOTA: Formatta il documento in markdown senza aggiungere delimitatori di codice.
        """,
        output_file='output/br_complete.md',
        agent=agent,
    )
    return integration_task
