class parent:
    parentAttr = 100
    def __init__(self):
        print("calling parent costructor")
    def parentMethod(self):
        print("calling parent method")
    def setAttr(self,attr):
        parent.parentAttr= attr
    def getAttr(self):
        print("parent attribute:",parent.parentAttr)

class child(parent):
    def __init__(self):
        print("calling child constructor")
        parent.__init__(self)
    def childMethod(self):
        print("calling child method")
c=child()
c.childMethod()
c.parentMethod()
c.setAttr(100)
c.getAttr()
