def rle(s: str) -> list[tuple[str,int]]:
    if not s:
        return []
    cons = []
    for i in range(len(s)):
        try:
            if s[i] == s[i + 1]:
                try:
                    cons[s[i]][1] += 1
                except TypeError:
                    cons.append((s[i], 1))
        except IndexError:
            pass
            
    return cons

print(rle('Ciaao come staaai'))
    