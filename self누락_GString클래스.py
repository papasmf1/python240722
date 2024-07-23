#전역변수 
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수 
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #모호한 것보다는 명확한 것이 좋다!
        print(self.strName)

#인스턴스 생성
d = DemoString()
d.set("First Message")
d.print()
