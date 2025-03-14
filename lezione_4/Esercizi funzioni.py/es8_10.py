lista_mess: list[str] = ["Ciao","Ehy","Come va?"]


def send_messages(messaggi: list[str]):
    sent_messages: list = []
    for mess in messaggi[:]: # copia della lista
        print(mess)
        invio = messaggi.pop()
        sent_messages.append(invio)
    return sent_messages

sent = send_messages(lista_mess) # lista dei messaggi inviati sent
print(lista_mess)
print(sent)