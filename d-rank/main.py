f1 = input()
print(f1, type(f1))

f2 = int(input())
print(f2, type(f2))

f3 = input().split()
print(f3, type(f3))

f4 = list(map(int, input().split()))
print(f4, type(f4))

f5, f6 = map(int, input().split())
beat = abs(f5 - f6)
print(beat)

f7 = input().strip()
result = f7[:-8] + "!!"
print(result)

f8 = input().strip()
print(f8)
print("^" * len(f8))
