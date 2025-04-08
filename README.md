# Sistema di Analisi dei Requisiti con CrewAI

Questo progetto implementa un sistema multi-agente basato su CrewAI che analizza requisiti di business e propone soluzioni tecniche appropriate. Il sistema è esposto come API REST tramite FastAPI, permettendo la gestione di progetti e business requests.

## Panoramica

Il sistema utilizza un'architettura basata su agenti AI che collaborano per analizzare requisiti, valutare business requests e generare proposte tecniche. Gli agenti includono analisti di business, architetti software, sviluppatori e altri ruoli specializzati che lavorano insieme per fornire analisi complete.

## Funzionalità Principali

- Gestione di progetti tramite API REST
- Analisi di business requests con CrewAI
- Valutazione automatica dei requisiti
- Generazione di domande per chiarire requisiti ambigui
- Integrazione delle risposte del cliente nei requisiti
- Analisi funzionale e tecnica dei requisiti

## Struttura del Progetto

- `main.py`: File principale per l'avvio del server API
- `core/`: Componenti core del sistema (API server, database manager)
- `projects/`: Gestione dei progetti (endpoint, servizi, modelli)
- `business_requests/`: Gestione delle business requests (endpoint, servizi, modelli)
- `analysis_crew/`: Implementazione del crew per l'analisi dei requisiti
- `design_crew/`: Implementazione del crew per il design della soluzione
- `epic_crew/`: Implementazione del crew per la generazione di epic
- `br_integrator/`: Integrazione delle business requests con le risposte del cliente
- `input/`: File di input per i requisiti e le risposte
- `openapi/`: Documentazione OpenAPI (Swagger)
- `postman/`: Collezione Postman per testare le API

## Prerequisiti

- Python 3.12 o superiore
- Pacchetti Python (vedi sezione Installazione)

## Installazione

1. Clona il repository

```bash
git clone <repository-url>
cd project_analyzer_server
```

2. Installa le dipendenze

```bash
pip install -e .
```

3. Configura le variabili d'ambiente nel file `.env`:

```
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-4-turbo  # o altro modello compatibile
MODEL_TEMPERATURE=0.2
```

## Utilizzo

### Avvio del Server

Avvia il server API con il comando:

```bash
python main.py
```

Il server sarà disponibile all'indirizzo `http://localhost:8000`.

### API Endpoints

#### Progetti

- `GET /projects`: Ottiene tutti i progetti
- `GET /projects/{project_id}`: Ottiene un progetto specifico
- `POST /projects`: Crea un nuovo progetto
- `PUT /projects/{project_id}`: Aggiorna un progetto esistente
- `PATCH /projects/{project_id}/disable`: Disabilita un progetto
- `PATCH /projects/{project_id}/enable`: Riabilita un progetto

#### Business Requests

- `GET /business-requests/project/{project_id}/versions`: Ottiene tutte le versioni di business request per un progetto
- `GET /business-requests/{br_id}`: Ottiene una specifica versione di business request
- `POST /business-requests`: Crea una nuova versione di business request
- `POST /business-requests/{br_id}/questions`: Ottiene domande per una business request

### Documentazione API

La documentazione completa delle API è disponibile in formato Swagger all'indirizzo `http://localhost:8000/docs` quando il server è in esecuzione.

## Personalizzazione

### Aggiungere Nuovi Requisiti

Puoi modificare il file `input/requirements.md` per includere i tuoi requisiti specifici. Assicurati di seguire la struttura del file di esempio, utilizzando i prefissi "RF" per i requisiti funzionali e "RNF" per i requisiti non funzionali.

### Modificare i Crew di Agenti

Per personalizzare il comportamento degli agenti, puoi modificare i file nei vari moduli `*_crew`. Ogni crew è composto da agenti specializzati che collaborano per svolgere compiti specifici.

## Contribuire

Sei invitato a contribuire a questo progetto! Puoi farlo nei seguenti modi:

1. Segnalando bug o problemi
2. Proponendo nuove funzionalità
3. Inviando pull request con miglioramenti o correzioni

## Licenza

Questo progetto è distribuito con licenza MIT.