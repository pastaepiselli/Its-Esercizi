class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_list: list[int] = []
        for n in nums:
            if n in new_list:
                continue
            new_list.append(n)
        return len(new_list)
        
prova = [1, 1, 2]
a = Solution()

risposta = a.removeDuplicates(prova)

print(risposta)