class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Painting")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.talent() #example 1

class A:
    def show(self):
        print("From A")

class B:
    def show(self):
        print("From B")

class C(A, B):
    pass

obj = C()
obj.show()    #example 2

class A:
    def show(self):
        print("From A")

class B:
    def show(self):
        print("From B")

class C(B, A):
    pass

obj = C()
obj.show()    #example 3

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        super().greet()

obj = C()
obj.greet() #example 4