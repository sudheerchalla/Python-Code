class employee:
    'class employee having name and age'
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def disp(self):
        print("name=",self.name,"age=",self.age)
#class docuentation:
print("employee.__doc__:",employee.__doc__)
#class name
print("employee.__name__:",employee.__name__)
#module name in which class is defined
print("employee.__module__:",employee.__module__)
#base classes
print("employee.__bases__:",employee.__bases__)
#dictionary containing class name space
print("employee.__dict__:",employee.__dict__)
