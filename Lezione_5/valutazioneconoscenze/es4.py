def blackjack_hand_total(cards: list[int]) -> int:
    sumCard: int = 0
    for item in cards:

        sumCard += item

        if sumCard > 21:

            if item == 11:

                sumCard -= 11
                sumCard += 1
    
    return sumCard


    