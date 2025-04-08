from typing import List, Optional
from pydantic import BaseModel


class EvaluationQuestion(BaseModel):
    """Modello per rappresentare una domanda di valutazione della Business Request."""
    id: str  # ID domanda (numerato progressivamente)
    area: str  # Area Domanda (nome paragrafo/sezione del documento originale)
    question: str  # Domanda da porre al cliente (formulata in modo chiaro e conciso)
    motivation: str  # Motivazione della domanda (spiegazione del perché è necessario chiarire questo punto)


class EvaluationResult(BaseModel):
    """Modello per rappresentare il risultato completo della valutazione della Business Request."""
    questions: List[EvaluationQuestion]  # Lista di domande di valutazione