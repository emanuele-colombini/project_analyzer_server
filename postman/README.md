# Collezione Postman per ProjectModel Analyzed

Questo file contiene una collezione Postman per testare le API del progetto ProjectModel Analyzed.

## Come utilizzare la collezione

### Importare la collezione in Postman

1. Apri Postman
2. Clicca su "Import" in alto a sinistra
3. Seleziona il file `project_analyzed_collection.json` da questa cartella
4. Clicca su "Import"

### Configurare l'ambiente

La collezione utilizza una variabile d'ambiente `baseUrl` che è preimpostata su `http://localhost:8000`. Se il tuo server è in esecuzione su un host o una porta diversa, puoi modificare questa variabile:

1. Clicca sull'icona a forma di occhio in alto a destra in Postman
2. Clicca su "Edit" accanto all'ambiente attivo
3. Modifica il valore della variabile `baseUrl`
4. Clicca su "Save"

## Endpoint disponibili

La collezione include i seguenti endpoint:

### Projects

- **GET /projects**: Ottiene tutti i progetti, con opzione per filtrare solo quelli abilitati
- **GET /projects/{project_id}**: Ottiene un progetto specifico tramite il suo ID
- **POST /projects**: Crea un nuovo progetto
- **PUT /projects/{project_id}**: Aggiorna un progetto esistente
- **PATCH /projects/{project_id}/disable**: Disabilita un progetto (soft delete)

### Business Requests

- **GET /business-requests/project/{project_id}/versions**: Ottiene tutte le versioni di una business request per un progetto, ordinate dalla più recente
- **GET /business-requests/{br_id}**: Ottiene una versione specifica di una business request tramite il suo ID
- **POST /business-requests**: Crea una nuova versione di una business request caricando un file markdown (diventa automaticamente la versione attiva)
- **POST /business-requests/{br_id}/questions**: Ottiene domande per una business request
- **GET /business-requests/{br_id}/content**: Scarica il file markdown di una business request

### Analysis

- **POST /analysis/{br_id}**: Crea un'analisi per una specifica business request

## Esempi di utilizzo

### Creare un nuovo progetto

1. Seleziona la richiesta "Create ProjectModel"
2. Modifica il corpo della richiesta con i dati del tuo progetto
3. Clicca su "Send"
4. Copia l'ID del progetto creato dalla risposta

### Ottenere un progetto specifico

1. Seleziona la richiesta "Get ProjectModel By ID"
2. Inserisci l'ID del progetto nella variabile di percorso
3. Clicca su "Send"

### Aggiornare un progetto

1. Seleziona la richiesta "Update ProjectModel"
2. Inserisci l'ID del progetto nella variabile di percorso
3. Modifica il corpo della richiesta con i nuovi dati
4. Clicca su "Send"

### Disabilitare un progetto

1. Seleziona la richiesta "Disable ProjectModel"
2. Inserisci l'ID del progetto nella variabile di percorso
3. Clicca su "Send"

### Ottenere le versioni di una business request per un progetto

1. Seleziona la richiesta "Get Versions By Project ID"
2. Inserisci l'ID del progetto nella variabile di percorso
3. Clicca su "Send"

### Ottenere una versione specifica di una business request

1. Seleziona la richiesta "Get Version By ID"
2. Inserisci l'ID della business request nella variabile di percorso
3. Clicca su "Send"

### Creare una nuova versione di una business request

1. Seleziona la richiesta "Create Version"
2. Modifica il corpo della richiesta con l'ID del progetto e il contenuto della business request
3. Clicca su "Send"