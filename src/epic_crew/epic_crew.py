from typing import List, Optional

from crewai import Crew, Process, LLM, Agent, Task
from pydantic import BaseModel

from src.analysis_crew import AnalysisModel


class EpicModel(BaseModel):
    id: str
    title: str
    description: str
    acceptance_criteria: List[str]
    dependencies: Optional[List[str]] = None
    complexity_estimate: str
    note: Optional[str] = None


class EpicListModel(BaseModel):
    epics: List[EpicModel]


class EpicCrew:
    def __init__(self):
        pass

    def generate_epic(self, analysis: AnalysisModel) -> Optional[EpicListModel]:

        # Agents
        epic_creator, epic_creation_task = self.create_epic_creator()

        # Crew
        crew = Crew(
            agents=[epic_creator],
            tasks=[epic_creation_task],
            verbose=True,
            process=Process.sequential,
            memory=True,
            embedder={
                "provider": "ollama",
                "config": {
                    "model": "nomic-embed-text"
                }
            }
        )

        # Run the crew
        result = crew.kickoff(inputs={
            "func_analysis": analysis.functional_analysis,
            "tech_analysis": analysis.technical_analysis
        })
        epic_list = result.pydantic

        return epic_list

    def create_epic_creator(self):

        llm = LLM(
            model='openai/saia:assistant:coder_assistant',
            api_base='https://api.beta.saia.ai/chat',
            api_key='coder_assistant_8TUnVI_h6Az_BxSa2NqSsXr4Udo35OQwOqc0fLyey9yHebo1XEkQwNFODPct0K9MXZ3GEa1uOiKJHdmY-xmqhg',
            temperature=0.1,
        )

        agent = Agent(
            role="Epic Creator",
            goal="Trasformare l'analisi funzionale e tecnica in epiche strutturate e dettagliate per il backlog di sviluppo",
            backstory="""Sei un Epic Creator esperto con anni di esperienza nella creazione di epiche e user stories per team agili. 
            La tua specialità è tradurre analisi funzionali e tecniche in elementi di backlog chiari, misurabili e implementabili.
            
            Hai una profonda conoscenza delle metodologie agili e sai come strutturare epiche che bilanciano valore di business, 
            complessità tecnica e dipendenze. Sei abile nell'identificare criteri di accettazione chiari e nel definire 
            la complessità delle attività in modo accurato.
            
            Il tuo approccio metodico assicura che ogni epica sia completa, ben definita e pronta per essere scomposta 
            in user stories dal team di sviluppo. Sei anche bravo a identificare dipendenze tra epiche e a suggerire 
            una sequenza logica di implementazione.""",
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

        task = Task(
            description="""Analizza attentamente i documenti di analisi funzionale e tecnica forniti e crea una lista di epiche strutturate. Ogni epica deve:
            
            1. Catturare l'essenza di una funzionalità significativa del sistema
            2. Definire chiaramente lo scopo e il valore di business
            3. Specificare criteri di accettazione misurabili
            4. Identificare eventuali dipendenze con altre funzionalità
            5. Fornire una stima di complessità basata sull'analisi tecnica
            
            Identifica tutte le funzionalità principali descritte nell'analisi e crea un'epica separata per ciascuna di esse.
            Ogni epica deve essere sufficientemente dettagliata da permettere al team di sviluppo di comprenderla 
            e scomporla in user stories, ma non deve entrare nei dettagli implementativi specifici.
            
            Utilizza le seguenti informazioni come input:
            - Analisi funzionale: {func_analysis}
            - Analisi tecnica: {tech_analysis}
            
            Assicurati che ogni epica sia allineata con i requisiti funzionali e le considerazioni tecniche descritte nei documenti di analisi.
            """,
            expected_output="""Una lista di epiche strutturate. Ogni epica deve includere:
            
            1. Identificatori univoci per ogni epica (ad es. EP001, EP002, ...)
            2. Titolo chiaro e conciso
            3. Descrizione dettagliata dello scopo e del valore di business
            4. Lista di criteri di accettazione specifici e misurabili
            5. Eventuali dipendenze con altre funzionalità (ad es, EP003)
            6. Stima di complessità (Bassa, Media, Alta, Molto Alta)
            7. Note aggiuntive o considerazioni particolari (opzionale)
            """,
            output_pydantic=EpicListModel,
            output_file='output/epic_list.json',
            agent=agent
        )
        
        return agent, task