from crewai import Agent, Task
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

from llms import global_llm


def create_software_architect():
    software_architect = Agent(
        role="Software Architect",
        goal="Trasformare l'analisi funzionale in un'analisi tecnica strutturata che serva come guida per la creazione di un backlog dettagliato",
        backstory="""Sei un Software Architect esperto con profonda conoscenza di diversi stack tecnologici e metodologie di progettazione software. 
        La tua specialità è tradurre requisiti di business in architetture tecniche solide e scalabili.
        Hai esperienza nella creazione di documenti di analisi tecnica che fungono da ponte tra le esigenze di business e l'implementazione tecnica.""",
        verbose=True,
        allow_delegation=True,
        llm=global_llm
    )
    return software_architect


def create_architectural_assessment_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    architectural_assessment_task = Task(
        description="""Analizza attentamente il documento di analisi funzionale fornito e produci una valutazione architetturale che:

        1. Valuti i requisiti funzionali e non funzionali in termini di complessità, scalabilità e modularità
        2. Determini se l'architettura più adatta sia:
            a. Un'applicazione monolitica
            b. Un'architettura a microservizi basata su Kubernetes
        3. Giustifichi la scelta architettonica in base a:
            a. Requisiti di business e utente
            b. Complessità di implementazione
            c. Necessità di scalabilità e manutenibilità
            d. Vincoli di risorse e tempo
            e. Competenze del team disponibili
        4. Individui i principali componenti del sistema e le loro responsabilità
        5. Definisca i confini e le interfacce tra componenti
        6. Identifichi le dipendenze critiche tra componenti

        IMPORTANTE: La valutazione architettonica DEVE:
        - Essere basata su motivazioni tecniche e di business concrete
        - Considerare il ciclo di vita completo dell'applicazione
        - Valutare i trade-off tra diverse scelte architetturali
        - Fornire raccomandazioni chiare e giustificate
        """,
        expected_output="""Un documento di valutazione architettonica strutturato che includa:

        1. Riepilogo dell'analisi dei requisiti in ottica architettonica
        2. Raccomandazione chiara tra approccio monolitico o microservizi
        3. Giustificazione dettagliata della scelta con pro e contro
        4. Descrizione dei componenti principali identificati
        5. Schema delle relazioni tra componenti (descritto in formato testuale)
        6. Considerazioni sulle implicazioni della scelta architettonica su:
        a. Complessità di sviluppo
        b. Gestione del deployment
        c. Monitoraggio e manutenzione
        d. Scalabilità futura

        Il documento deve fornire una base solida per la successiva analisi tecnica dettagliata.""",
        context=context,
        output_file=output_file_path,
        agent=agent,
    )
    return architectural_assessment_task


def create_technical_analysis_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    technical_analysis_task = Task(
        description="""Analizza attentamente il documento di analisi funzionale fornito e produci un'analisi tecnica che:

        1. Identifichi l'architettura generale del sistema
        2. Definisca i componenti principali e le loro interazioni
        3. Specifichi le tecnologie e gli stack consigliati
        4. Fornisca linee guida per la gestione dei dati
        5. Delinei considerazioni di sicurezza e performance
        6. Identifichi potenziali rischi tecnici e strategie di mitigazione
        7. Proponga approcci per la scalabilità e la manutenibilità

        IMPORTANTE: L'analisi tecnica NON deve includere:
        - Codice sorgente o implementazioni dettagliate
        - Dettagli implementativi specifici a livello di codice
        - Soluzioni troppo specifiche che limitino la flessibilità del team di sviluppo

        L'analisi tecnica DEVE:
        - Essere sufficientemente dettagliata da permettere la creazione di un backlog attività granulare
        - Fornire linee guida chiare e principi di progettazione
        - Mantenere coerenza con i requisiti funzionali
        - Essere strutturata in modo da facilitare la pianificazione del lavoro
        """,
        expected_output="""Un documento di analisi tecnica strutturato che includa:

        1. Panoramica dell'architettura
        2. Descrizione dei componenti principali
        3. Diagrammi concettuali (descritti in formato testuale)
        4. Stack tecnologico consigliato con motivazioni
        5. Approccio alla gestione dei dati
        6. Considerazioni di sicurezza
        7. Strategie di performance e scalabilità
        8. Rischi tecnici e strategie di mitigazione
        9. Requisiti non funzionali
        10. Linee guida per lo sviluppo

        Il documento deve essere sufficientemente dettagliato da permettere la creazione di user stories o task per un backlog di sviluppo.""",
        context=context,
        output_file=output_file_path,
        agent=agent,
    )

    return technical_analysis_task


def create_architectural_assessment_final_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    architectural_assessment_review_task = Task(
        description="""Riscrivi completamente la valutazione architetturale tenendo conto del feedback e dei suggerimenti
        forniti dal Product Owner. Non limitarti a modificare il documento originale, ma creane uno nuovo che incorpori 
        tutte le indicazioni ricevute, garantendo che l'architettura proposta soddisfi pienamente i requisiti di business.""",
        expected_output="""Una versione completamente riscritta della valutazione architetturale che incorpora tutti i 
        feedback e i suggerimenti del Product Owner, migliorando la solidità della proposta architettonica e il suo 
        allineamento con gli obiettivi di business. Se la revisione del Product Owner indica che il documento originale è 
        già corretto e completo, riproduci il documento originale senza modifiche. In caso contrario, incorpora 
        tutti i feedback ricevuti per creare una versione migliorata.""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return architectural_assessment_review_task


def create_technical_analysis_final_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    technical_analysis_review_task = Task(
        description="""Riscrivi completamente l'analisi tecnica tenendo conto del feedback e dei suggerimenti 
        forniti dal Product Owner. Non limitarti a modificare il documento originale, ma creane uno nuovo che incorpori 
        tutte le indicazioni ricevute, assicurando che le soluzioni tecniche proposte siano allineate con gli obiettivi 
        di business e le aspettative degli stakeholder.""",
        expected_output="""Una versione completamente riscritta dell'analisi tecnica che incorpora tutti i feedback e i 
        suggerimenti del Product Owner, migliorando la chiarezza delle soluzioni proposte, la loro fattibilità e il loro 
        allineamento con gli obiettivi di business. Se la revisione del Product Owner indica che il documento originale è 
        già corretto e completo, riproduci il documento originale senza modifiche. In caso contrario, incorpora 
        tutti i feedback ricevuti per creare una versione migliorata.""",
        context=context,
        output_file=output_file_path,
        agent=agent
    )

    return technical_analysis_review_task


def create_microservices_documentation_task(
        software_architect
):
    microservices_documentation_task = Task(
        description="""Analizza attentamente la valutazione architetturale e crea un modello strutturato per ogni microservizio identificato.
        
        Se l'architettura scelta è monolitica, crea un unico modello che descriva il sistema monolitico e le sue componenti interne.
        
        Se l'architettura scelta è a microservizi, crea un modello separato per ciascun microservizio identificato.
        
        Per ogni microservizio (o per il sistema monolitico) il modello deve includere:
        1. Una descrizione dettagliata del microservizio/sistema e del suo scopo principale
        2. Le responsabilità funzionali del microservizio/sistema
        3. I confini e le interfacce con altri microservizi/componenti
        4. Una lista completa delle componenti interne con relative descrizioni
        5. Le dipendenze con altri microservizi/componenti
        6. Considerazioni tecniche specifiche per il microservizio/sistema
        
        IMPORTANTE: La documentazione DEVE:
        - Essere coerente con la valutazione architettonica
        - Fornire dettagli sufficienti per comprendere il ruolo e la struttura di ciascun microservizio/sistema
        - Evidenziare chiaramente le relazioni tra i diversi microservizi (se applicabile)
        - Mantenere una struttura uniforme per tutti i modelli
        
        Input: 
        
        Valutazione Architetturale:
        {architectural_assessment}
        
        Analisi funzionale:
        {functional_analysis}
        
        Analisi Tecnica:
        {technical_analysis}
        
        """,
        expected_output="""Un oggetto Pydantic di tipo MicroservicesDocumentationModel che contiene:
        
        1. Il tipo di architettura (monolitica o microservizi)
        2. Una lista di oggetti MicroserviceModel, ciascuno contenente:
           - Nome e scopo del microservizio/sistema
           - Descrizione dettagliata delle responsabilità
           - Interfacce e API esposte (oggetti InterfaceModel)
           - Componenti interne con descrizioni (oggetti ComponentModel)
           - Dipendenze con altri microservizi/componenti
           - Considerazioni tecniche specifiche
        
        L'oggetto Pydantic deve essere strutturato in modo chiaro e coerente, fornendo una visione completa dell'architettura del sistema.""",
        output_file='output/microservices_documentation.json',
        output_pydantic=MicroservicesDocumentationModel,
        agent=software_architect
    )
    
    return microservices_documentation_task


def create_microservices_documentation_validation_task(
        software_architect,
        architectural_assessment_task=None,
        technical_analysis_task=None
):
    microservices_documentation_validation_task = Task(
        description="""Analizza attentamente il documento di documentazione dei microservizi generato (microservices_documentation.json) e valuta la sua qualità e completezza.
        
        La validazione deve verificare i seguenti aspetti:
        
        1. Conformità strutturale:
           - Verifica che il documento rispetti la struttura del modello Pydantic definito
           - Controlla che tutti i campi obbligatori siano presenti e valorizzati correttamente
           - Verifica la coerenza dei tipi di dati utilizzati
        
        2. Completezza dei contenuti:
           - Verifica che la descrizione dell'architettura sia chiara e coerente con la valutazione architettonica
           - Controlla che ogni microservizio (o il sistema monolitico) abbia una descrizione completa e dettagliata
           - Verifica che le responsabilità di ogni componente siano chiaramente definite
           - Controlla che le interfacce e le API siano documentate in modo esaustivo
           - Verifica che le dipendenze tra componenti siano correttamente identificate
        
        3. Coerenza interna:
           - Verifica che non ci siano contraddizioni tra le diverse parti del documento
           - Controlla che le dipendenze dichiarate siano coerenti con le interfacce esposte
           - Verifica che le considerazioni tecniche siano allineate con le responsabilità dichiarate
        
        4. Qualità delle informazioni:
           - Valuta la chiarezza e la precisione delle descrizioni
           - Verifica che le informazioni fornite siano sufficientemente dettagliate
           - Controlla che non ci siano ambiguità o informazioni mancanti
        
        5. Coerenza con l'architettura scelta:
           - Se l'architettura è monolitica, verifica che il documento descriva adeguatamente la modularità interna
           - Se l'architettura è a microservizi, verifica che ogni microservizio abbia responsabilità ben definite e confini chiari
        
        IMPORTANTE: La validazione DEVE:
        - Essere obiettiva e basata su criteri concreti
        - Identificare eventuali problemi o carenze nel documento
        - Fornire suggerimenti specifici per migliorare la qualità del documento
        - Valutare se il documento è sufficientemente completo per essere utilizzato come base per lo sviluppo
        
        Utilizza il file microservices_documentation.json presente nella cartella output come input per questa validazione.
        """,
        expected_output="""Un report di validazione strutturato che includa:
        
        1. Valutazione generale della qualità del documento
        2. Analisi dettagliata dei punti di forza e delle criticità
        3. Elenco di eventuali problemi o carenze identificati, classificati per gravità
        4. Suggerimenti specifici per migliorare la qualità e la completezza del documento
        5. Valutazione finale sulla idoneità del documento come base per lo sviluppo
        
        Il report deve essere sufficientemente dettagliato da permettere un miglioramento mirato del documento di documentazione dei microservizi.""",
        context=[architectural_assessment_task, technical_analysis_task] if architectural_assessment_task and technical_analysis_task else [],
        output_file='output/microservices_documentation_validation.md',
        agent=software_architect
    )
    
    return microservices_documentation_validation_task


class ComponentModel(BaseModel):
    """Modello per rappresentare un componente interno di un microservizio o sistema monolitico."""
    name: str = Field(..., description="Nome del componente")
    description: str = Field(..., description="Descrizione dettagliata del componente e delle sue funzionalità")
    responsibilities: List[str] = Field(..., description="Lista delle responsabilità del componente")
    dependencies: Optional[List[str]] = Field(None, description="Lista delle dipendenze con altri componenti")
    technical_notes: Optional[str] = Field(None, description="Note tecniche specifiche per il componente")


class InterfaceModel(BaseModel):
    """Modello per rappresentare un'interfaccia o API esposta da un microservizio."""
    name: str = Field(..., description="Nome dell'interfaccia o API")
    description: str = Field(..., description="Descrizione dettagliata dell'interfaccia")
    endpoints: Optional[List[str]] = Field(None, description="Lista degli endpoint esposti, se applicabile")
    input_output: Optional[Dict[str, Any]] = Field(None, description="Descrizione degli input e output dell'interfaccia")


class MicroserviceModel(BaseModel):
    """Modello per rappresentare un microservizio o sistema monolitico."""
    name: str = Field(..., description="Nome del microservizio o sistema")
    purpose: str = Field(..., description="Scopo principale del microservizio o sistema")
    description: str = Field(..., description="Descrizione dettagliata del microservizio o sistema")
    responsibilities: List[str] = Field(..., description="Lista delle responsabilità funzionali")
    interfaces: List[InterfaceModel] = Field(..., description="Interfacce e API esposte")
    components: List[ComponentModel] = Field(..., description="Componenti interne con descrizioni")
    dependencies: Optional[List[str]] = Field(None, description="Dipendenze con altri microservizi o componenti esterni")
    technical_considerations: str = Field(..., description="Considerazioni tecniche specifiche")


class MicroservicesDocumentationModel(BaseModel):
    """Modello per rappresentare la documentazione completa dei microservizi o del sistema monolitico."""
    architecture_type: str = Field(..., description="Tipo di architettura: 'monolithic' o 'microservices'")
    microservices: List[MicroserviceModel] = Field(..., description="Lista dei microservizi o singolo sistema monolitico")