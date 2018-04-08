def extend(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            extend(perm, n)
            perm.pop()
                print(perm)

#n = input('Please enter :')

extend(perm = [], n = 4)
