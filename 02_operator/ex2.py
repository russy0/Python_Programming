# 비트 연산자
a = 5  # 0000 0101
b = 3  # 0000 0011
print(a & b)  # 0000 0001
print(a | b)  # 0000 0111
print(a ^ b)  # 0000 0110
print(a << b)  # 5 -> 10 -> 20 -> 40
print(40 >> b)  # 5
print(~a)  # 1111 1010

# 멤버십 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a>b? a:b
max_num = a if a > b else b

# a값이 짝수면 "짝수", 홀수면 "홀수" 출력
a = 11
print("짝수" if a % 2 == 0 else "홀수")

score = 85
# 90이상 A
# 80 -> B
# 70 -> C

print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D')
