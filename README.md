# Projekt: Reddit Bot
**Funktion**: Durchsucht die 25 neuesten Kommentare im 'test' Subreddit nach dem String "Lebron" und antwortet auf passende Kommentare.

## Wie es funktioniert:
- Nutzt die Python Reddit API Wrapper (PRAW), um mit der Reddit-API zu interagieren.
- Loggt sich bei Reddit ein, indem es Anmeldedaten verwendet, die in einer separaten `config.py` Datei gespeichert sind.
- Ruft die 25 neuesten Kommentare aus dem 'test' Subreddit ab.
- Überprüft jeden Kommentar auf den String "Lebron" und stellt sicher, dass der Autor des Kommentars nicht der Bot selbst ist.
- Wenn beide Bedingungen erfüllt sind, antwortet der Bot auf den Kommentar.
- Behält den Überblick, auf welche Kommentare es bereits geantwortet hat, indem es deren IDs in einer Datei namens `comments_replied_to.txt` speichert.

## Einrichtung:
- Klone das Repository.
- Installiere die benötigten Python-Pakete.
- Erstelle eine `config.py` Datei mit deinen Reddit-Anmeldedaten.
- Führe den Bot mit `python reddit_bot.py` aus.

## Lizenz: MIT-Lizenz