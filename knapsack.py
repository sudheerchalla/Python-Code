capacity=float(input("enter the capacity"))
capacityRemaining=capacity
n=int(input("enter no. of items"))
items=[]
weight=[]
price=[]
ratio=[]
''' Test Cases
items=['A','B','C','D','E','F']
price=[4,2,1,2,10]
weight=[12,2,1,1,4]
ratio=[0.33,1,1,2,2.5]'''
for i in range(n):
      items.append(input("enter item name"))
      weight.append(float(input("enter item name weight")))
      price.append(float(input("enter item price")))
      ratio.append(price[i]/weight[i])
choice=int(input("enter  1 for minimizing weight \n2 for maximizing price \n3 for maximising density"))
count=0
weightOfBag=0
totalsum=0
while count<n:
      if choice==1:
            mweight=min(weight)
            pos=weight.index(mweight)
      elif choice==2:
            mprice=max(price)
            pos=price.index(mprice)
            mweight=weight[pos]
      else:
            mratio=max(ratio)
            pos=ratio.index(mratio)
            mweight=weight[pos]
      if mweight<=capacityRemaining:
            print(items[pos], "inserted into bag")
            totalsum=totalsum+price[pos]
            weightOfBag=weightOfBag+mweight
            capacityRemaining=capacity-weightOfBag
      del items[pos]
      del weight[pos]
      del price[pos]
      del ratio[pos]
      count=count+1
      if capacity==weightOfBag:
             break
print("total price in bag : ", totalsum,"\ntotal weight of bag : ", weightOfBag)
             
