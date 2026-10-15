# =========================================================
#  🔥 실습 문제
# =========================================================

# SchoolMember 부모 클래스 작성하기
class SchoolMember:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f"이름: {self.name}, 전화번호: {self.phone}")


# Student 자식 클래스 작성하기
class Student(SchoolMember):
    def __init__(self, name, phone, grade):
        super().__init__(name, phone)
        self.grade = grade

    def learn(self, teacher):
        print(f"{self.name}가 {teacher.name}에게 {teacher.subject} 과목을 배웁니다.")

    def show_info(self):
        super().show_info()
        print(f"학년: {self.grade}학년")


# Teacher 자식 클래스 작성하기
class Teacher(SchoolMember):
    def __init__(self, name, phone, subject):
        super().__init__(name, phone)
        self.subject = subject

    def teach(self, student):
        print(f"{self.name}이 {student.name}에게 {self.subject} 과목을 가르칩니다.")

    def show_info(self):
        super().show_info()
        print(f"과목: {self.subject}")


# 1️⃣ 부모 클래스 인스턴스 변수: name(이름), phone(연락처) -> 생성자 구현

# 2️⃣ 자식 클래스 인스턴스 변수 -> 생성자 구현
# - Student 클래스: grade(학년)
# - Teacher 클래스: subject(과목)


# 3️⃣ 자식 객체 생성: 생성자 호출

s = Student("뽀로로", "111-1111", 1)
t = Teacher("크롱선생님", "222-2222", "파이썬")

# 4️⃣ 인스턴스 및 상속 관계 확인

print(isinstance(s, SchoolMember))  # True
print(isinstance(t, SchoolMember))  # True
print(isinstance(s, Student))  # True
print(isinstance(t, Teacher))  # True

print(issubclass(Student, SchoolMember))  # True
print(issubclass(Teacher, SchoolMember))  # True
print(issubclass(Student, Teacher))  # False

# 5️⃣ 인스턴스 메소드 구현
# - SchoolMember 클래스: show_info() 메소드 구현
# - Student, Teacher 클래스: show_info() 메소드 오버라이딩

s.show_info()  # 이름: 뽀로로, 전화번호: 111-1111
# 학년: 1학년
t.show_info()  # 이름: 크롱선생님, 전화번호: 222-2222
# 과목: 파이썬

# 6️⃣ Student 클래스: learn() 메소드 구현
s.learn(t)  # 뽀로로가 크롱선생님에게 파이썬 과목을 배웁니다.

# 7️⃣ Teacher 클래스: teach() 메소드 구현
t.teach(s)  # 크롱선생님이 뽀로로에게 파이썬 과목을 가르칩니다.
