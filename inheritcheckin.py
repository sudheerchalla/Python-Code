class parent:
    pv=10
    def __init__(self):
        print("parent")
    def disp(self):
        print("parent class")
class parent1:
    def disp1(self):
        print("parent1 class")
class child(parent,parent1):
    def __init__(self):
        parent. __init__(self)
        print("child")

h=child()
print(h.pv)
h.disp()
h.disp1()
print(issubclass(child,parent))
