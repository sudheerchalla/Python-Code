class demo:
    cv=0
    def __init__(self,m):
      self.iv=m
      demo.cv+=1
    def disp(self):
        print("class variable",demo.cv)
        print("instance variable",self.iv)

demo1=demo(30)
demo1.disp()
demo2=demo(45)
demo2.disp()

demo3=demo(90)
demo3.disp()
