# built in in python
import curses # serve per colorare la roba che printiamo sul terminale
from curses import wrapper # questo e per inizializzare il modulo e alla fine lo chiude e fa tornare il terminale apposto
import time # per calcolare il wpm
import random

def start_screen(stdscr):
    stdscr.clear() # pulisce tutto quello che ce sul terminale
    # i 2 numeri sarebbero le coordinate in cui piazziamo il testo ... tornera utile per sovrascrivere il testo verde (corretto) o rosso (sbagliato)
    stdscr.addstr(0, 1,'Welcome to the Speed Typing Test!') # con questo aggiungo testo nel terminale, con color_pair a seconda del numero cambia la combinazione di colori
    stdscr.addstr(0, 1  ,'\n Press any key to start!')
    stdscr.refresh() # poi ricarico lo schermo
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0): # test
    stdscr.addstr(target) # il testo da scrivere
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # iteriamo nella lista delle lettere e le printiamo a schermo
    for i,char in enumerate(current): # enumerate ci permette di avere sia index che valore

        correct_char = target[i] # valore che deve avere la lettera con index i 
        color = curses.color_pair(1) # verde

        if char != correct_char: # se il carattere inserito ed errato viene printato in rosso
            color = curses.color_pair(2) # rosso
        # 0, i e dove vengolo posizionati i caratteri

        stdscr.addstr(0, i, char, color) # printo la lettere ... colore 1

# ogni partita un testo differente scelto dal file testi.txt
def load_text():
    with open('testi.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip() # .strip() rimuove il \n alla fine della riga



def wpm_test(stdscr):
    target_text = load_text() # il testo da scrivere
    current_text = [] # in questa lista vengono inseriti i caratteri che vengono scritti
    wpm = 0 
    start_time = time.time() # viene salvato il tempo di inizio della prova
    stdscr.nodelay(True) # non aspettare che l'utente prema un tasto
    
    while True: # con questo loop chiediamo l'input dell' utente

        # uso max con 1 per evitare divisione con zero
        time_elapsed = max(time.time() - start_time, 1) # il tempo passato e uguale al tempo di adesso - inizio
        # calcolo del wpm:
        #     caratteri scritti    tempo passato da dividere per 60 per capire quanti minuti passati, uso round per non avere numeri con la virgola

        wpm = round(len(current_text) / (time_elapsed / 60) / 5)

        # si puo fare anche con la moltiplicazione
        # wpm = len(current_text) * (60 / time_elapsed)

        stdscr.clear() # se non ci fosse il clear current_text verrebbe printato ogni iterazione
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh() # ricontrolla le lettere inserita
        
        # join converte una lista in stringa ... detro gli apici puoi inserire caratteri o spazi tra un elemento e l'altro
        if target_text == "".join(current_text):
            stdscr.nodelay(False)
           # cosi aspetta l'input dell'utente per la prossima partita
            break

        # questa lineae causa un exption perche stdscr.nodelay(True) # non aspettare che l'utente prema un tasto (qua per proseguire e necessario inserire un tasto)
        try:
            key = stdscr.getkey()
        except: # nel caso non premiamo nessun tasto continua a calcolare wpm
            continue

        if key == '\x1b': # quando premo (esc) cureses ritorna ^[
            break   

        if key in ('KEY_BACKSPACE', '\b', '\x7f', ): # controlla se il tasto premuto sia uguale a delete
            if len(current_text) > 0: # nel caso non sia stato scritto nienet non cancella niente
                current_text.pop() # .pop rimuove l'ultimo carattere della lista

        elif len(current_text) < len(target_text): # controllo per non scrivere di piu rispetto alla lunghezza del target
            current_text.append(key)
        

def main(stdscr): # std = standard output
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # 1 rappresenta la coppia verde (testo), bianco (sfondo)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        # quando viene completata la frase
        stdscr.addstr(2, 0, 'You completed the test!! Press any key to continue...')
        key = stdscr.getkey()

        if ord(key) == 27:
            break


wrapper(main) # passo la funzione main nel wrapper cosi che inizializzi tutta la roba di curses