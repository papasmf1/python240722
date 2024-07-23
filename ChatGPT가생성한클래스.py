# 클래스 정의
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def run_tests():
    # 테스트 1: Person 클래스 생성 및 출력
    print("Test 1:")
    person1 = Person(1, "Alice")
    person1.printInfo()
    print()
    
    # 테스트 2: Manager 클래스 생성 및 출력
    print("Test 2:")
    manager1 = Manager(2, "Bob", "Team Lead")
    manager1.printInfo()
    print()
    
    # 테스트 3: Employee 클래스 생성 및 출력
    print("Test 3:")
    employee1 = Employee(3, "Charlie", "Python Developer")
    employee1.printInfo()
    print()
    
    # 테스트 4: Person 클래스의 다른 인스턴스
    print("Test 4:")
    person2 = Person(4, "David")
    person2.printInfo()
    print()
    
    # 테스트 5: Manager 클래스의 또 다른 인스턴스
    print("Test 5:")
    manager2 = Manager(5, "Eva", "Project Manager")
    manager2.printInfo()
    print()
    
    # 테스트 6: Employee 클래스의 다른 인스턴스
    print("Test 6:")
    employee2 = Employee(6, "Frank", "Data Scientist")
    employee2.printInfo()
    print()
    
    # 테스트 7: Manager 클래스의 printInfo 메서드 호출
    print("Test 7:")
    manager3 = Manager(7, "Grace", "HR Manager")
    manager3.printInfo()
    print()
    
    # 테스트 8: Employee 클래스의 printInfo 메서드 호출
    print("Test 8:")
    employee3 = Employee(8, "Hank", "Software Engineer")
    employee3.printInfo()
    print()
    
    # 테스트 9: Person 클래스의 인스턴스와 다른 클래스 인스턴스 비교
    print("Test 9:")
    print(isinstance(person1, Person))  # True
    print(isinstance(manager1, Manager))  # True
    print(isinstance(employee1, Employee))  # True
    print(isinstance(person1, Manager))  # False
    print()
    
    # 테스트 10: 상속 관계 확인
    print("Test 10:")
    print(issubclass(Manager, Person))  # True
    print(issubclass(Employee, Person))  # True
    print(issubclass(Person, Manager))  # False

# 테스트 실행
run_tests()
