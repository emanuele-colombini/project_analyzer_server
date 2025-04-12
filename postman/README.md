# Collezione Postman per Project Analyzed

Questo file contiene una collezione Postman per testare le API del progetto Project Analyzed.

## Come utilizzare la collezione

### Importare la collezione in Postman

1. Apri Postman
2. Clicca su "Import" in alto a sinistra
3. Seleziona il file `project_analyzed_collection.json` da questa cartella
4. Clicca su "Import"

### Configurare l'ambiente

La collezione utilizza alcune variabili d'ambiente:

- `baseUrl`: URL base dell'API (default: `http://localhost:8000`)
- `project_id`: ID del progetto corrente
- `br_id`: ID della business request corrente

Per configurare l'ambiente:

1. Importa il file `project_analyzed_environment.json`
2. Clicca sull'icona a forma di occhio in alto a destra in Postman
3. Clicca su "Edit" accanto all'ambiente "Project Analyzed Environment"
4. Modifica i valori delle variabili secondo necessità
5. Clicca su "Save"

## Endpoint disponibili

La collezione include i seguenti endpoint:

### Projects

- **GET /projects**: Ottiene tutti i progetti, con opzione per filtrare solo quelli abilitati
- **GET /projects/{project_id}**: Ottiene un progetto specifico tramite il suo ID
- **POST /projects**: Crea un nuovo progetto
- **PUT /projects/{project_id}**: Aggiorna un progetto esistente
- **PATCH /projects/{project_id}/disable**: Disabilita un progetto (soft delete)
- **PATCH /projects/{project_id}/enable**: Abilita un progetto precedentemente disabilitato

### Business Requests

- **GET /business-requests/project/{project_id}/versions**: Ottiene tutte le versioni di una business request per un progetto
- **GET /business-requests/{br_id}**: Ottiene una versione specifica di una business request
- **POST /business-requests**: Crea una nuova versione di una business request (file markdown)
- **POST /business-requests/{br_id}/questions**: Genera domande per una business request
- **GET /business-requests/{br_id}/content**: Scarica il file markdown di una business request

### Analysis

- **POST /functional-analysis/{br_id}**: Crea un'analisi funzionale per una business request

### Architecture

- **POST /architecture/{br_id}**: Crea un'analisi architetturale per una business request

## Esempi di utilizzo

### Creare un nuovo progetto

1. Seleziona la richiesta "Create Project"
2. Modifica il corpo della richiesta con i dati del tuo progetto:
```json
{
  "name": "Nuovo Progetto",
  "description": "Descrizione del nuovo progetto"
}
```
3. Clicca su "Send"
4. Dalla risposta, salva l'ID del progetto nella variabile d'ambiente `project_id`

### Creare una nuova versione di una business request

1. Seleziona la richiesta "Create Version"
2. In "Body" > "form-data":
   - Inserisci il `project_id` del progetto
   - Carica un file markdown (.md) nel campo `file`
3. Clicca su "Send"
4. Dalla risposta, salva l'ID della business request nella variabile d'ambiente `br_id`

### Generare domande per una business request

1. Seleziona la richiesta "Get Questions"
2. Verifica che la variabile `br_id` contenga l'ID della business request
3. Clicca su "Send"

### Creare un'analisi

1. Seleziona "Create Analysis" o "Create Architecture Analysis"
2. Verifica che la variabile `br_id` contenga l'ID della business request
3. Clicca su "Send"