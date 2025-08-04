
# big O notation O(n^2)

def twoSum(nums: list[int], target: int) -> list[int]:
    # creo 2 cicli for 
    for i in range(0, len(nums)):
        #  con il secondo parto da index 1 e lo cambio dopo che ho provato tutte le somme
        # i + 1 perche j deve essere sempre diverso e un index in piu rispettoa i 
        for j in range(i + 1, len(nums)):
            
            # se non ritornano true allora aggiorna prima j poi i 
            if nums[j] + nums[i] == target:
                return [j, i]


nums: list[int] = [3, 3]

print(twoSum(nums, 6))

# O(n)

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {} # dizionario dei numeri visti
    for i, num in enumerate(nums): # iteriamo per i e per i valori nella lista di nums
        diff = target - num # differenza con il target
        print(f"i: {i}, num: {num}, diff: {diff}, seen: {seen}")
        if diff in seen: # se la differenza e nel dizionario allora la loro somma sara il target!!
            print(f"Found! {seen[diff]} + {i}")
            return [seen[diff], i] # ritorno l'index della differenza trovata prima, e index di quella trovata adesso
        seen[num] = i # se la differenza non e nel dizionario allora la aggiungo ... chiave: valore in nums ... valore: index
