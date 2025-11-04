def letter_count(text: str) -> dict[str,int]:
    text = text.lower()
    letters = {}
    for c in text:
        # controlla che il caratterere sia una stringa
        if c.isalpha():
            # Se chiave è presente in letters, restituisce letters[chiave].
            # Se non è presente, restituisce valore_default (0 in questo caso) senza lanciare un errore.
            letters[c] = letters.get(c, 0) + 1 # poi ce il piu uno valido in entrabi i casi

    