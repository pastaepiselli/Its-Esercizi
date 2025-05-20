def text_analysis(text: str) -> None:

    parole: list[str] = text.split()
    new_dict: dict[str: int] = {}

    for elem in parole:

        if elem not in new_dict:

            new_dict[elem] = 1

        else:

            new_dict[elem] += 1

    ripetizione: str = max(new_dict.items())
    print(f'La parola che si ripete piu spesso e {ripetizione[0]} ripetuta ben {ripetizione[1]} volte')


text_analysis('Le palle delle palle di cutolo')