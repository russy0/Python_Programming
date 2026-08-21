# 입출력

a = input()

print(a) # 자동으로 줄바꿈 됨
print(a, end = '') # end를 통해 자동 개행를 변경 할 수 있음

print(type(a))
print(a, type(a)) # 한 줄에 여러개 출력 가능 (자동으로 사이에 띄어쓰기가 들어감)
print(a,type(a), sep = '') # 자동 띄어쓰기도 변경 할 수 있음

# 정수 변환
a = input()
a = int(a)
print(a, type(a))

a = int(input()) # 한 줄에 할 수도 있음
print(a, type(a))

a = float(input()) # 실수형도 가능
print(a, type(a))

# 정수 2개 입력
a = int(input())
b = int(input())
print(a, b)

# 100 200 입력
a = input().split() # split()을 통해 분할 가능
print(a, type(a)) # split()을 쓰면 list형으로 저장됨

a,b,c = map(int, input().split()) # map({함수}, {list 객체}) => {list 객체}의 값들을 각각 {함수}에 실행해 반환값들을 map 형식으로 반환
print(a, type(a))

# list()형태로 변환
a = list(map(int, input().split())) # list로 형변환
print(a,type(a))