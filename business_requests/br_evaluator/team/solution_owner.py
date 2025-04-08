from crewai import Agent, Task

from business_requests.br_evaluator.models import EvaluationResult
from business_requests.br_data import BusinessRequestModel
from llms import global_llm


def create_solution_owner() -> Agent:
    solution_owner = Agent(
        role="Solution Owner",
        goal="Valutare criticamente la Business Request identificando lacune informative e formulando domande chiare per il cliente",
        backstory="""
        Sei un esperto Solution Owner con anni di esperienza nella valutazione di documenti di requisiti.
        La tua specialità è individuare ambiguità, omissioni e potenziali problemi nelle Business Request.
        Sei abile nel formulare domande precise che aiutano a chiarire i punti critici. 
        
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


def create_evaluation_task(agent: Agent, project_name: str) -> Task:
    evaluation_task = Task(
        description="""
        Analizza attentamente la seguente Business Request:
        
        Il tuo compito è quello di:
        1. Leggere attentamente ogni sezione della Business Request
        2. Identificare qualsiasi ambiguità, mancanza di dettagli o potenziale problema
        3. Formulare domande specifiche da porre al cliente per chiarire questi punti, usa il linguaggio identificato dal file di business_request originale
        4. Consultare gli altri agenti specialisti per ottenere input nelle loro aree di competenza
        5. Produrre un oggetto strutturato che contenga le domande con le seguenti informazioni:
           - ID domanda (numerato progressivamente, es. "Q001")
           - Area Domanda (nome paragrafo/sezione del documento originale)
           - Domanda da porre al cliente (formulata in modo chiaro e conciso, mantenendo la lingua identificata dalle business request fornite)
           - Motivazione della domanda (spiegazione del perché è necessario chiarire questo punto, mantenendo la lingua identificata dalle business request fornite)
           
        Business request da parte del cliente:
        {business_request}
        """,
        agent=agent,
        expected_output="""
            Un oggetto Pydantic EvaluationResult che contiene tutte le domande da porre al cliente, organizzate in modo strutturato e chiaro.
            
            Ogni domanda (EvaluationQuestion) deve includere:
            1. ID domanda (formato "Q001", "Q002", ecc.)
            2. Area Domanda (nome paragrafo/sezione del documento originale)
            3. Domanda da porre al cliente (formulata in modo chiaro e conciso, mantenendo la lingua identificata dalle business request fornite)
            4. Motivazione della domanda (spiegazione del perché è necessario chiarire questo punto, mantenendo la lingua identificata dalle business request fornite)
        """,
        output_file=f'output/{project_name}/br_evaluation.json',
        output_pydantic=EvaluationResult,
    )
    return evaluation_task
