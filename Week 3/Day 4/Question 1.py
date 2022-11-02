class student: 
def_init(self): 
self.name= ” ” 
self.m1=0 
self.m2=0 
self.total=0 
def gdata(self): 
self.name = input(“Enter your name”) 
self.m1 = int(input(“Enter first subject marks:”)) 
self.m2 = int(input(“Enter second subject mark:”))
 self.total = self.m1+self.m2 
 def disp(self): 
 print(self.name) 
 print(self.m1) 
 print(self.m2) 
 print(self.total) 
 mlist = [ ] 
 st = student( ) 
 st.gdata( ) 
 mlist. append(st) 
 for x in mlist: 
 x.disp( )