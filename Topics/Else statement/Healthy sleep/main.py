A = int(input())
B = int(input())
H = int(input())

if H > B:
    print("Excess")
else:
    if A <= H <= B:
        print("Normal")
    else:
        print("Deficiency")
