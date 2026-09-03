# for문

# for(int i=0;i<=10;i++)
# for i in iterable 객체:

# 0 ~4
for i in range(5):
    print(i, end = "")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1~5
for i in range(1, 6):
    print(i, end = "")
print()

# 0 ~10 짝수
for i in range(0, 11, 2):
    print(i, end = "")
print()

# 5,4,3,2,1
for i in range(5, 0, -1):
    print(i, end = "")
print()

# 1~10까지의 합
tot = 0
for i in range(1, 10):
    tot += i
print(tot)

print(sum(range(1, 11)))

s = "hi12!@한글人📜"
for c in s:
    print(c, end = " ")
print()
print(len(s))

# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i:2d} x {j:2d} = {i * j:2d}", end = "\t")
    print()
else:
    print('end')
