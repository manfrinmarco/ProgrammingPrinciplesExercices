Creare una classe, che gestisce una collezione di film costituita dal file movies.json.
Il file condiviso è già popolato con una decina di film, da usare come riferimento.
Ogni film è caratterizzato dai campi title e director che sono stringhe, year che è un numero intero e genre che è una lista di stringhe.
La classe, dovrà chiamarsi MovieLibrary e dovrà essere definita all’interno del file movie_library.py.
La classe dovrà avere due attributi di istanza, inizializzati nel metodo costruttore.
Il primo va chiamato json_file, e deve essere inizializzato passando, in fase di creazione oggetto, 
il percorso assoluto del file movies.json sul vostro pc.
Il secondo va chiamato movies e rappresenta la collezione di film. Deve essere inizializzato col contenuto del file json de-serializzato.
In pratica sarà una lista di dizionari, dove ogni dizionario rappresenta un film.
Ogni modifica che viene effettuata a movies, in qualsiasi metodo, deve immediatamente riflettersi sul file movies.json.

ESERCIZI:
01. Crea un metodo chiamato get_movies che restituisce l’intera collezione di film.
02. Crea un metodo chiamato add_movie che ha i parametri 
    title e director di tipo stringa, year di tipo intero e genres di tipo lista (di stringhe).
    Il metodo aggiunge il film alla collezione e aggiorna il file json.
03. Crea un metodo chiamato remove_movie che ha il parametro title.
    Il metodo rimuove dalla collezione il film che ha titolo corrispondente (NON case sensitive) a title.
    Il metodo aggiorna il file json e restituisce il film rimosso.
04. Crea un metodo chiamato update_movie che ha il parametro title
    e i parametri opzionali director, year e genres.
    Il metodo ricerca nella collezione il film che ha titolo corrispondente (NON case sensitive) a title.
    Quindi modifica il film, applicando il valore di ciascun parametro opzionale non nullo.
    Il metodo aggiorna il file json e restituisce il film coi valori aggiornati.
05. Crea un metodo chiamato get_movie_titles
    che restituisce una lista contenente tutti i titoli dei film nella collezione.
06. Crea un metodo chiamato count_movies
    che restituisce il numero totale dei film nella collezione.
07. Crea un metodo chiamato get_movie_by_title che ha il parametro title.
    Il metodo restituisce il film che ha titolo corrispondente (NON case sensitive) a title.
08. Crea un metodo chiamato get_movies_by_title_substring che ha il parametro substring.
    Il metodo restituisce una lista di tutti i film che contengono, nel titolo, una sottostringa corrispondente 
    (case sensitive) a substring.
09. Crea un metodo chiamato get_movies_by_year che ha il parametro year.
    Il metodo restituisce una lista di tutti i film con anno corrispondente a year.
10. Crea un metodo chiamato count_movies_by_director che ha il parametro director.
    Il metodo restituisce un numero intero che rappresenta, quanti film del director scelto sono presenti nella collezione. Il director va confrontato in modo NON case sensitive.
11. Crea un metodo chiamato get_movies_by_genre che ha il parametro stringa genre.
    Il metodo restituisce una lista di tutti i film che hanno genere corrispondente a genre.
    Il genre va confrontato in modo NON case sensitive.
12. Crea un metodo chiamato get_oldest_movie_title
    che restituisce il titolo del film più antico della collezione.
13. Crea un metodo chiamato get_average_release_year
    che restituisce un float rappresentante la media aritmetica degli anni di pubblicazione
    dei film della collezione.
14. Crea un metodo chiamato get_longest_title che restituisce il titolo più lungo della collezione di film.
15. Crea un metodo chiamato get_titles_between_years che ha due parametri: start_year e end_year.
    Il metodo restituisce una lista contenente i titoli dei film pubblicati dall’anno start_year fino all’anno end_year (estremi compresi).
16. Crea un metodo chiamato get_most_common_year 
    che restituisce l’anno che si ripete più spesso fra i film della collezione.
    Non considerare il caso in cui vi siano pari merito.
17. Modifica il metodo costruttore affinché,
    se nel percorso json_file non viene trovato alcun file,
    venga sollevata l’eccezione FileNotFoundError
    col messaggio personalizzato “File not found: ” seguito dal percorso json
18. Modifica i metodi remove_movie e update_movie affinché,
    se non viene trovato alcun film avente come titolo title,
    venga sollevata l’eccezione personalizzata MovieNotFoundError,
    avente il messaggio “Movie was not found”
    Tale eccezione va definita all’interno della classe MovieLibrary.