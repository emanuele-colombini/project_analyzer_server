Voglio creare una applicazione che ha lo scopo di scaricare una moltitudine di immagini e video da più siti. 
I siti sono pubblici e mi permettono di avere delle REST API da chiamare dalle quali, a seconda del sito, 
posso identificare le immagini da scaricare. 
I media scaricati sono relativi ad una auto, a seconda del sito una auto può avere identificativi diversi o uguali (capita quando l'id è una stringa e non un numero)
Le informazioni delle auto fanno parte di un'area dell'applicazione che è da generare che potrebbe essere messa a disposizione
per una implementazione successiva di un frontend ad hoc. Per ora limitarsi alle API fondamentali.

L'applicazione dovrebbe avere dei job che eseguono in background per ogni sito configurato. 
Per ogni sito dovrebbe essere disponibile una sua implementazione custom con le seguenti funzionalità:
 
1. ogni job eseguito ha una implementazione di riferimento, ogni volta che parte deve memorizzar le informazioni base come id esecuzione, data avvio, data fine e media scaricati. 
2. ogni implementazione carica le auto che sono relative a quell'implementazione.
3. data implementazione e auto, vengono chiamate le API e il risultato viene parsato per identificare i media da scaricare
4. successivamente vengono scaricati tutti i media, tenendo traccia di delle varie colonne come ID esecuzione, auto di riferimento, implementazione sito, data avvio, data completamento, successo, errore. 
5. i job devono essere configurabili in stile cron ed eseguiti ogni ora (ma questo dettaglio dovrà essere configurabile a posteriori) 

L'applicazione dovrebbe anche mettere a disposizione REST API per il controllo dei job e delle auto:
1. avvio immediato dei job
2. pausa/ripristino dell'esecuzione di un job
3. lista delle esecuzioni (ordinato dall'ultima alla prima)
4. dettaglio di una singola esecuzione, dove sono elencati i media scaricati (un job gestisce un solo sito da cui scaricare i media)
5. lista auto per ogni implementazione
6. operazioni di crud sulle auto, comprese enable/disable per la temporanea sospensione dallo scaricamento

Per iniziare considera le seguenti informazioni:
1. considerare inizialmente di implementare solo un sito, ma tenere la possibilità di implementarne altri facilmente
2. I job devono essere eseguiti una volta all'ora, al minuti 50 di ogni ora, ma deve essere configurabile facilmente
3. si prevede di scaricare molti media quando si aggiunge una auto nuova, e poi poche decine al giorno 

Vorrei che utilizzassi librerie che risultano essere standard de-facto quali:
- SQLAlchemy ORM
- Pydantic
- APScheduler

Vorrei inoltre che l'applicazione fosse scritta con una modalità enterprise-line e production-ready, possibilmente usando uno stile di programmazione molto strutturato dove per i singoli modelli sono indicate le singole responsabilità (stile SOLID, KISS). 
Usa un db sqlite per lo sviluppo.
