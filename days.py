def func(s, k):
    new_k = k % 7
    kb = {1: "Mon", 2: "Tues", 3: "Wed", 4: "Thurs", 5: "Fri", 6: "Sat", 7: "Fri"}
    for key, val in kb.items():
        if val == s:
            new_key = key + new_k
        break
    print(kb[new_key])