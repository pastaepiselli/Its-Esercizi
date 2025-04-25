def aggrega_voti(voti: list[dict]) -> dict[str, list[int]]:
    sumvoti: dict[str, list[int]] = {}

    for elem in voti:
        if elem['nome'] not in sumvoti:

            sumvoti[elem['nome']] = [elem['voto']]

        else:

            sumvoti[elem['nome']].append(elem['voto'])
    return sumvoti