# Relazione Tecnica - Negozio triste

## Introduzione
IL mio progetto si occupa di un negozio che vende prodotti(inizialmente vestiti) estratti dall'api, con la possibilità di aggiungerre, rimuovere o confermare (checkout) i prodotti nel carrello.
## Tecnologie Utilizzate

Python: Linguaggio di programmazione utilizzato per lo sviluppo del backend.

Flask: Framework web leggero e flessibile per la creazione di applicazioni web in Python.

Flask-SQLAlchemy: Estensione di Flask che semplifica l'interazione con database SQL in Flask.

SQLite: Motore di database SQL leggero e incorporato utilizzato come database di sviluppo.

HTML e CSS: Linguaggi di markup e di stile utilizzati per la struttura e la presentazione delle pagine web.

Werkzeug: Libreria utilizzata per hashare le password

janji2: Libreria utilizzata per generare pagine html, utilizzato principalmente per il render_template

Requests: Libreria Python per effettuare richieste HTTP.

## Architettura del Sistema
Componenti Principali:
Frontend (Client Web):
Interfaccia utente attraverso la quale gli utenti interagiscono con il sistema.
Implementato utilizzando HTML, CSS e JavaScript, eventualmente con framework come React, Angular o Vue.js.
Comunica con il backend tramite richieste HTTP.
Backend (Server Web):
Gestisce la logica di business e fornisce servizi all'applicazione frontend.
Implementato utilizzando un framework web come Flask o Django in Python.
Si interfaccia con il database e altri servizi esterni.
Database:
Archivia i dati utilizzati dall'applicazione.
Utilizza un database relazionale come SQLite, PostgreSQL o MySQL, o un database NoSQL come MongoDB, a seconda delle esigenze del sistema.

## Database
Dato un negozio avevo creato una tabella utenti con eventuali credenziali e l email come pk essendo unica, successivamente ho creato una tabella prodotti che verranno salvati nel Cart_items temporanemante, infatti, dopo aver fatto il checkout, i dati dei prodotti vengono eliminati nella cart_items, vien calcolato il total amount, viene creato un id_orders, viene presa l email utente, e inserite quelle informazioni nella tabella Orders

## Sviluppo del Software
Pianificazione e Analisi dei Requisiti: In questa fase vengono identificati i requisiti del software e pianificato il processo di sviluppo. Gli stakeholder sono coinvolti per definire le funzionalità desiderate e i vincoli del progetto.
Progettazione: Durante questa fase, si definisce l'architettura del software e si elaborano dettagliate specifiche tecniche. Si decidono le tecnologie da utilizzare e si stabiliscono le interfacce utente e i flussi di lavoro.
Implementazione: Qui avviene la scrittura effettiva del codice sorgente in base alle specifiche stabilite durante la fase di progettazione. È importante scrivere codice pulito e documentato per garantire la manutenibilità nel tempo.
Test e Validazione: Vengono eseguiti test per verificare che il software funzioni correttamente e soddisfi i requisiti definiti. Questo include test di unità, test di integrazione, test funzionali e test di accettazione utente.
Rilascio: ovvero il Deployment, questa fase è fondamentale nel ciclo di vita del software, in quanto porta il codice sorgente dall'ambiente di sviluppo all'ambiente di produzione, rendendolo accessibile agli utenti finali

## User Stories e Requisiti
Registrazione Utente:
Gli utenti possono registrarsi inserendo un username, una password e un'email.
Criteri di accettazione: Tutti i campi (username, password, email) devono essere obbligatori. L'email deve essere univoca nel sistema.
Accesso Utente:
Gli utenti possono effettuare l'accesso inserendo le proprie credenziali (username e password).
Criteri di accettazione: L'accesso è consentito solo se le credenziali inserite corrispondono a un utente registrato nel sistema.
Logout Utente:
Gli utenti possono effettuare il logout dal proprio account.
Criteri di accettazione: L'utente viene reindirizzato alla pagina principale dopo il logout e perde l'accesso alle funzionalità riservate.
Visualizzazione dei Prodotti:
Gli utenti possono visualizzare l'elenco dei prodotti disponibili.
Criteri di accettazione: La lista dei prodotti è mostrata sulla pagina principale del sito.
Aggiunta al Carrello:
Gli utenti possono aggiungere prodotti al proprio carrello.
Criteri di accettazione: L'aggiunta al carrello avviene con successo solo se l'utente è autenticato e il prodotto esiste nel database.
Visualizzazione del Carrello:
Gli utenti possono visualizzare i prodotti presenti nel proprio carrello.
Criteri di accettazione: Il carrello mostra l'elenco dei prodotti aggiunti, la quantità e il prezzo totale.
Rimozione dal Carrello:
Gli utenti possono rimuovere prodotti dal proprio carrello.
Criteri di accettazione: La rimozione avviene con successo solo se l'utente è autenticato e il prodotto è presente nel carrello.
Checkout:
Gli utenti possono procedere al checkout per confermare e pagare gli acquisti nel carrello.
Criteri di accettazione: Durante il checkout, l'utente visualizza un riepilogo dell'ordine e conferma l'acquisto.
Gestione degli Ordini:
Gli utenti possono visualizzare lo storico dei propri ordini.
Criteri di accettazione: L'utente può accedere alla lista degli ordini effettuati con i relativi detta


## Test e Validazione
Test di integrazione API esterne:
Obiettivo: Verificare l'integrazione corretta con l'API esterna per il recupero dei prodotti.
Procedure:
Effettuare una richiesta all'API esterna.
Confrontare i dati ottenuti con i dati memorizzati nel database.
Risultato atteso: I dati recuperati dall'API esterna devono corrispondere ai dati memorizzati nel database.
Test di registrazione utente:
Obiettivo: Verificare il corretto funzionamento della registrazione di un nuovo utente.
Procedure:
Inserire dati validi nel form di registrazione.
Verificare che i dati siano correttamente salvati nel database.
Risultato atteso: Dopo la registrazione, l'utente deve essere autenticato e reindirizzato alla homepage.
Test di accesso al carrello:
Obiettivo: Verificare il corretto funzionamento dell'accesso al carrello dell'utente.
Procedure:
Effettuare l'accesso con un utente valido.
Verificare che l'utente abbia accesso al proprio carrello.
Risultato atteso: L'utente autenticato deve poter visualizzare il proprio carrello con i prodotti aggiunti.
Test di aggiunta al carrello:
Obiettivo: Verificare il corretto funzionamento dell'aggiunta di prodotti al carrello.
Procedure:
Aggiungere un prodotto al carrello di un utente autenticato.
Verificare che il prodotto sia correttamente aggiunto al carrello dell'utente.
Risultato atteso: Dopo l'aggiunta, il prodotto deve essere presente nel carrello dell'utente con la quantità specificata.
Test di checkout:
Obiettivo: Verificare il corretto funzionamento del processo di checkout.
Procedure:
Effettuare il checkout con un utente autenticato.
Verificare che l'ordine sia correttamente creato nel database e che il carrello sia svuotato.
Risultato atteso: Dopo il checkout, l'ordine dell'utente deve essere registrato nel database e il carrello deve essere vuoto.
Test di logout:
Obiettivo: Verificare il corretto funzionamento del logout dell'utente.
Procedure:
Effettuare il logout con un utente autenticato.
Verificare che l'utente venga correttamente disconnesso.
Risultato atteso: Dopo il logout, l'utente deve essere reindirizzato alla homepage e non deve essere più autenticato.


## Deploy e Manutenzione
ho provato a fare il deployment su pythonAnywhere, creato la webapp e configurato il virtualenvironment, installato le librerie e copiato i file che avevo sul progetto di github, dandomi errori però sul codice, anche se lo script è corretto.

## Conclusioni
il progetto, in conclusione, ha avuto un esito positivo ma non ho completato tutti gli obiettivi: non ho utilizzato GitHub per questo progetto principalmente perchè a causa del problema dell'api col proxy, ho lavorato quasi solamente su una macchina, altro motivo è stato anche il fatto che quando provavo a committare mi dava problemi con le brenches e, avendo il pc per un tempo limitato e non essendo fondamentale per lo sviluppo del mio progetto ho deciso di procastinare il problema. 
Un altro problema è stato un typing problem nell'output del bottone nel file index.html, che inviava un campo .id inesistente alla funzione add_to_cart che, quindi lo inoltrava come response alle request della user story add_to_cart nel file py, essendo però vuoto, rendendo così la ricerca del prodotto impossibile, rilasciando l errore 404, prodotto non trovato.


