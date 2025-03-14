lista_mess: list[str] = ["Ciao","Ehy","Come va?"]

def show_message(messaggi: list[str]):
    for mess in messaggi:
        print(mess)

show_message(lista_mess)