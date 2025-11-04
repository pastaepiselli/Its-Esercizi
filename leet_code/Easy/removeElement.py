class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i: int = 0
        n: int = len(nums)
        while i < n:
            if nums[i] == val:
                # se trovo val sostituisco con l'ultimo elemento della lista (cotrollo prossima iterazione)
                nums[i] = nums[n - 1]
                # diminuisco la lunghezza della lista
                n -= 1
            else:
                # solo in questo caso mi muovo ad un altro elemetto
                i += 1

        return n