class student:
    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks
    def talk(self):
        print("my name is  ", self.name)
        print("my rno is  ", self.rno)
        print("my marks are  ", self.marks)
try:
    rno = int(input("Enter rno "))
    if rno <= 0:
        raise Exception("rno should not be -ve")
    name = input("enter name ")
    if not name.isalpha() or len(name) < 2:
        raise Exception("name should contain minimum 2 alphabets")
    marks = int(input("Enter marks "))
    if marks < 0 and marks > 100:
        raise Exception("rno should not be -ve")
except ValueError:
    print("Invalid rno/marks")
except Exception as e:
    print(e)
else:
    s = student(rno, name, marks)
    s.talk()
