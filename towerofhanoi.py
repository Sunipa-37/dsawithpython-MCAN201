def toh(n, beg, end, aux):
    if n == 1:
        print(f"Move disk  from {beg} to {end}")
        return 1
    c1 = toh(n - 1, beg, aux, end)
    print(f"Move disk from {beg} to {end}")
    c2 = toh(n - 1, aux, end, beg)

    return c1 + 1 + c2
n=int(input("enter number of disk: "))
moves = toh(n, "beg", "end", "aux")
print("Total :", moves)
