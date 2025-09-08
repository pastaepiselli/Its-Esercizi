class Solution:
    def romanToInt(self, s: str) -> int:
        somma: int = 0
        numeriRomani: dict[str, int] = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        i = 0
        while i != len(s):

            try:
                if numeriRomani[s[i]] < numeriRomani[s[i + 1]]:
                    somma += numeriRomani[s[i + 1]] - numeriRomani[s[i]]
                    # qua il contatore si aggiorna di due perche andiamo a prenedre 2 valori che diventano uno solo ... guarda IV
                    i += 2
                else:
                    somma += numeriRomani[s[i]]
                    # qua invece si aggiorna di uno perche andiamo in questo caso solo ad aggiungere il valore di una lettera
                    i += 1

            except IndexError:
                somma += numeriRomani[s[i]]

        return somma

            
                
a = Solution()

print(a.romanToInt('MCMXCIV'))