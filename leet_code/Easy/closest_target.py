class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        res = 1000000
        trovato = False
        for i in range(len(words)):
            if words[i] == target:
                trovato =True
                # distanza muovendosi da destra 
                d_dis = abs(startIndex - i)

                # distanza muovendosi da sinistra
                s_dis = len(words) - d_dis
                
                # ritorna la distanza piu corta
                res = min(res, d_dis, s_dis)
    
    
        if trovato: 
            return res
        return -1
