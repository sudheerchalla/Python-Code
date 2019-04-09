class demo:
    cv=0
    def __init__(self):
      demo.cv+=1
    def disp(self):
        print("class variable",demo.cv)
        
        print("instance variable",self.cv)

demo1=demo()
demo2=demo()
demo2.disp()
demo1.disp()
demo3=demo()
demo3.disp()
