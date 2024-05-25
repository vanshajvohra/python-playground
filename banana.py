# BANANA
def func(s):
    kb = {"B": 0, "A": 0, "N": 0}
    for c in s:
        if c in kb:
            kb[c] += 1
    return min(kb["A"]//3, kb["N"]//2, kb["B"])
        
func("QABA")