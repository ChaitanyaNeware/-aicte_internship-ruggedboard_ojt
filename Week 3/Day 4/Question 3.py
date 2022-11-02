class Dist: 
def_init_(self): 
self.dist 1=0 
self.dist 2=0 
def read(self): 
self.dist 1=int(input(“Enter distance 1”)) 
self.dist 2=int(input(“Enter distance 2”)) 
def disp(self): 
print(“distance 1” , self.dist 1) 
print(“distance 2” , self.dist 2) 
def add(self): 
print(“Total distances” , self.dist 1+self.dist 2) 
def sub(self): 
print(“Subtracted distance” , self.dist 1-self.dist 2)  
d=Dist( ) 
choi = “y” 
while(choi == “y”): 
print(” 1. accept \n 2. Display \n 3. Total \n 4. Subtract”) 
ch = int(input(“Enter your choice”)) 
if(ch==l): 
d.read( ) 
elif(ch==2): 
d.disp( ) 
elif(ch==3):
d.add( ) 
elif(ch==4): 
d.sub( ) 
else:  
print(“Invalid Input…”)
choi = input(“Do you want to continue”)