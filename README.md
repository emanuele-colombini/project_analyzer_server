# Sistema di Analisi dei Requisiti con CrewAI

Questo progetto implementa un sistema multi-agente basato su CrewAI che analizza requisiti da file markdown e propone soluzioni tecniche appropriate. Il sistema utilizza un Analista dei Requisiti come agente principale che legge, analizza e propone soluzioni basate sui requisiti forniti.

## Struttura del Progetto

- `main.py`: File principale per l'esecuzione del sistema
- `agents.py`: Definizione degli agenti (Analista dei Requisiti)
- `tasks.py`: Definizione dei task che gli agenti devono eseguire
- `utils.py`: Funzioni di utilità e strumenti per gli agenti
- `requirements.md`: File di esempio contenente i requisiti da analizzare
- `guidelines.md`: Linee guida per l'analisi dei requisiti

## Prerequisiti

- Python 3.8 o superiore
- Pacchetti Python: crewai, langchain, langchain_openai, dotenv

## Configurazione

1. Assicurati di avere una chiave API valida per OpenAI
2. Configura le variabili d'ambiente nel file `.env`:
   - `OPENAI_API_KEY`: La tua chiave API di OpenAI
   - `MODEL_NAME`: Il modello da utilizzare (default: gpt-4-turbo)
   - `MODEL_TEMPERATURE`: La temperatura del modello (default: 0.2)

## Utilizzo

1. Prepara un file markdown con i requisiti da analizzare (puoi utilizzare o modificare il file `requirements.md` di esempio)
2. Esegui il sistema con il comando:

```bash
python main.py
```

3. Il sistema analizzerà i requisiti e genererà un report con proposte di soluzioni

## Personalizzazione

### Aggiungere Nuovi Requisiti

Puoi modificare il file `requirements.md` per includere i tuoi requisiti specifici. Assicurati di seguire la struttura del file di esempio, utilizzando i prefissi "RF" per i requisiti funzionali e "RNF" per i requisiti non funzionali.

### Modificare le Linee Guida

Puoi personalizzare le linee guida per l'analisi modificando il file `guidelines.md`. Queste linee guida influenzeranno il modo in cui l'agente Analista dei Requisiti interpreta e analizza i requisiti.

### Aggiungere Nuovi Agenti

Per estendere il sistema con nuovi agenti (ad esempio, un Architetto di Sistema o un Esperto di Sicurezza), modifica il file `agents.py` aggiungendo nuove funzioni per creare gli agenti desiderati.

### Aggiungere Nuovi Task

Per aggiungere nuovi task per gli agenti, modifica il file `tasks.py` aggiungendo nuove funzioni per creare i task desiderati.

## Contribuire

Sei invitato a contribuire a questo progetto! Puoi farlo nei seguenti modi:

1. Segnalando bug o problemi
2. Proponendo nuove funzionalità
3. Inviando pull request con miglioramenti o correzioni

## Licenza

Questo progetto è distribuito con licenza MIT.