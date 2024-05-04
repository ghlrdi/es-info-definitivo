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
Descrizione dell'architettura generale del sistema, inclusi componenti principali, moduli e pattern architetturali utilizzati.
## Database
Dato un negozio avevo creato una tabella utenti con eventuali credenziali e l email come pk essendo unica, successivamente ho creato una tabella prodotti che verranno salvati nel Cart_items temporanemante, infatti, dopo aver fatto il checkout, i dati dei prodotti vengono eliminati nella cart_items, vien calcolato il total amount, viene creato un id_orders, viene presa l email utente, e inserite quelle informazioni nella tabella Orders

## Sviluppo del Software
Descrizione del processo di sviluppo seguito, inclusi metodi, tecniche e strumenti utilizzati per la gestione del codice sorgente e il controllo delle modifiche.

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

## Documentazione del Codice
Indicazioni su come accedere e utilizzare la documentazione del codice sorgente, inclusi commenti nel codice e documentazione generata automaticamente.

## Test e Validazione
Descrizione dei test effettuati sul sistema per verificare il corretto funzionamento e la conformità ai requisiti specificati.

## Deploy e Manutenzione
Descrizione del processo di deploy del sistema, inclusi eventuali passaggi necessari per configurare l'ambiente di produzione e gestire la manutenzione del sistema.

## Conclusioni
il progetto, in conclusione, ha avuto un esito positivo ma non ho completato tutti gli obiettivi: non ho utilizzato GitHub per questo progetto principalmente perchè a causa del problema dell'api col proxy, ho lavorato quasi solamente su una macchina, altro motivo è stato anche il fatto che quando provavo a committare mi dava problemi con le brenches e, avendo il pc per un tempo limitato e non essendo fondamentale per lo sviluppo del mio progetto ho deciso di procastinare il problema. 

un altro problema è stato un typing problem nell'output del bottone nel file index.html, che inviava un campo .id inesistente alla funzione add_to_cart che, quindi lo inoltrava come response alle request della user story add_to_cart nel file py, essendo però vuoto, rendendo così la ricerca del prodotto impossibile, rilasciando l errore 404, prodotto non trovato.


