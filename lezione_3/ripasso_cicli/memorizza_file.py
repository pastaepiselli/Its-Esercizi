def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    for item in files:

        compressed = float((item * 80) / 100)
        blocchi = round(complex / 512, 0)
        if spazio_totale_blocchi - blocchi > 0:

            print(f'File di {item} byte compresso in {compressed} e memorizzato. Blocchi usati {blocchi}. Blocchi rimanenti {spazio_totale_blocchi}')
           
        else:
            print(f'Non è possibile memorizzare il file di {item} byte. Spazio insufficiente')

    