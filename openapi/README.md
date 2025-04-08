# OpenAPI Specification per Project Analyzed

Questo documento contiene la specifica OpenAPI (precedentemente conosciuta come Swagger) per le API di Project Analyzed. La specifica è stata creata per facilitare lo sviluppo del frontend dell'applicazione.

## Struttura delle API

Le API sono organizzate in due gruppi principali:

1. **Projects**: API per la gestione dei progetti
   - Ottenere tutti i progetti
   - Ottenere un progetto specifico
   - Creare un nuovo progetto
   - Aggiornare un progetto esistente
   - Disabilitare un progetto (soft delete)

2. **Business Requests**: API per la gestione delle business requests
   - Ottenere tutte le versioni di una business request per un progetto
   - Ottenere una versione specifica di una business request
   - Creare una nuova versione di una business request

## Utilizzo della specifica OpenAPI per il frontend

La specifica OpenAPI può essere utilizzata in diversi modi per sviluppare il frontend dell'applicazione:

### 1. Generazione automatica di client API

Puoi utilizzare strumenti come [OpenAPI Generator](https://openapi-generator.tech/) per generare automaticamente client API in vari linguaggi di programmazione:

```bash
# Esempio per generare un client TypeScript-Fetch
npx @openapitools/openapi-generator-cli generate -i ./swagger.json -g typescript-fetch -o ./frontend/src/api
```

### 2. Visualizzazione e test con Swagger UI

Puoi utilizzare Swagger UI per visualizzare e testare le API:

```bash
# Installare swagger-ui-express se stai utilizzando Node.js
npm install swagger-ui-express
```

### 3. Integrazione con framework frontend

Per React, puoi utilizzare librerie come:
- [swagger-typescript-api](https://github.com/acacode/swagger-typescript-api)
- [orval](https://orval.dev/)

Per Vue.js, puoi utilizzare:
- [swagger-typescript-api](https://github.com/acacode/swagger-typescript-api)
- [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen)

## Esempio di utilizzo con React e TypeScript

1. Genera i tipi TypeScript e i client API:

```bash
npx swagger-typescript-api -p ./swagger.json -o ./src/api -n ProjectAnalyzedApi.ts
```

2. Utilizza i client generati nel tuo codice React:

```typescript
import { ProjectsApi } from './api/ProjectAnalyzedApi';

const ProjectsList = () => {
  const [projects, setProjects] = useState([]);
  const api = new ProjectsApi();

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await api.getAllProjects();
        setProjects(response);
      } catch (error) {
        console.error('Errore nel recupero dei progetti:', error);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div>
      <h1>Progetti</h1>
      <ul>
        {projects.map(project => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </div>
  );
};
```

## Note aggiuntive

- La specifica è basata su OpenAPI 3.0.0
- Il server di sviluppo è configurato su `http://localhost:8000`
- Tutti gli endpoint restituiscono e accettano dati in formato JSON