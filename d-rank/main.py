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

f9 = input()
a, op, b = f9.split()
print(int(a) + int(b))

f10 = int(input())

pencils = ["6B", "5B", "4B", "3B", "2B", "B", "HB", "F",
           "H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H"]
print(pencils[f10-1])

f11 = float(input())
us = f11 - 18
uk = f11 - 18.5
print(f"{us:.1f} {uk:.1f}")

f12 = int(input())

for _ in range(f12):
    print("##########")
    print("..........")

f13 = input()
for c in f13:
    print(c)

f14 = input()
print("Mt. " + f14)

f15 = int(input())
rate = int(f15 / 140 * 100)
print(str(rate) + "%", type(rate))

f16 = int(input())
for i in range(10):
    print((f16 + i) % 10)

f17, f18 = map(int, input().split())
diff = t18 - f17
if diff > 0:
    print(f"+{diff}")
elif diff == 0:
    print(0)
else:
    print(diff)

f19 = input().strip()

if f19 in {"C","E","F","G","H","I","J","K","L","M","N","S","T","U","V","W","X","Y","Z"}:
    print(0)
elif f19 in {"A","D","O","P","Q","R"}:
    print(1)
elif f19 == "B":
    print(2)

f20 = int(input())

if f20 < 30:
    print("quiet")
elif f20 < 50:
    print("normal")
elif f20 < 70:
    print("noisy")
else:
    print("very noisy")
