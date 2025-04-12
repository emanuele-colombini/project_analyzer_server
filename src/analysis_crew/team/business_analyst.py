from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_business_analyst():
    business_analyst = Agent(
        role="Business Analyst",
        goal="Analizzare i requisiti del cliente e trasformarli in una documentazione strutturata per il team tecnico",
        backstory="""Sei un esperto Business Analyst con anni di esperienza nell'analisi dei requisiti cliente e nella 
        loro trasformazione in specifiche comprensibili per i team tecnici. Hai una vasta esperienza in diversi settori 
        e sai come identificare requisiti impliciti, eliminare ambiguità e strutturare le informazioni in modo chiaro.
        Sei abile nell'individuare possibili criticità e rischi nei requisiti e nel suggerire soluzioni alternative.
        Il tuo obiettivo è creare un ponte comunicativo efficace tra le esigenze del cliente e le capacità 
        implementative del team tecnico.""",
        verbose=True,
        allow_delegation=True,
        llm=global_llm
    )
    return business_analyst


def create_functional_analysis_task(
        agent: Agent,
        output_file_path: str
):
    functional_analysis_task = Task(
        description="""Analizza attentamente i requisiti business del cliente forniti in input e produci una 
        documentazione strutturata che faciliti l'analisi tecnica successiva. 

        Il tuo lavoro include:

        1. COMPRENSIONE DEI REQUISITI:
            - Identificare e classificare i requisiti (funzionali, non funzionali, vincoli)
            - Rilevare ambiguità, contraddizioni o informazioni mancanti
            - Formulare domande chiarificatrici se necessario

        2. ANALISI E STRUTTURAZIONE:
            - Organizzare i requisiti in categorie logiche
            - Stabilire priorità e dipendenze tra i requisiti
            - Identificare stakeholder e utenti finali per ciascun requisito

        3. DOCUMENTAZIONE PER IL TEAM TECNICO:
            - Creare user stories o casi d'uso dettagliati
            - Definire criteri di accettazione per ciascun requisito
            - Elaborare diagrammi di flusso o schemi concettuali quando necessario
            - Documentare vincoli tecnici e di business

        4. ANALISI RISCHI E CRITICITÀ:
            - Identificare potenziali criticità nell'implementazione
            - Suggerire possibili soluzioni alternative
            - Evidenziare requisiti che potrebbero richiedere ricerca o competenze specifiche

        5. CONCLUSIONI E RACCOMANDAZIONI:
            - Fornire una sintesi dei punti chiave
            - Suggerire un approccio di implementazione
            - Proporre eventuali fasi successive di approfondimento

        Output atteso: Un documento di analisi dei requisiti strutturato, completo e pronto per essere utilizzato
        dal team tecnico per l'implementazione.
        Business requirements: {requirements}
        """,
        expected_output="""
        Un documento business di analisi dei requisiti completo che include:
        - Panoramica del progetto e obiettivi principali
        - Requisiti categorizzati e prioritizzati
        - User stories o casi d'uso dettagliati
        - Criteri di accettazione
        - Diagrammi o schemi concettuali
        - Analisi dei rischi e criticità
        - Raccomandazioni per l'implementazione
        """,
        output_file=output_file_path,
        agent=agent,
    )

    return functional_analysis_task


def create_functional_analysis_final_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    functional_analysis_review_task = Task(
        description="""Riscrivi completamente l'analisi funzionale tenendo conto del feedback e dei suggerimenti 
        forniti dal Product Owner. Non limitarti a modificare il documento originale, ma creane uno nuovo che 
        incorpori tutte le indicazioni ricevute mantenendo la coerenza e la completezza dell'analisi.""",
        expected_output="""Una versione completamente riscritta dell'analisi funzionale che incorpora tutti i 
        feedback e i suggerimenti del Product Owner, migliorando la chiarezza, la completezza e l'allineamento 
        con gli obiettivi di business. Se la revisione del Product Owner indica che il documento originale è 
        già corretto e completo, riproduci il documento originale senza modifiche. In caso contrario, incorpora 
        tutti i feedback ricevuti per creare una versione migliorata.""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return functional_analysis_review_task
