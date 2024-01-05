class Class1:
    def __init__(self):
        # self.member1 = 111
        pass

    def f_func0(self):
        print("Метод f_func0() класу Class1")
    def f_func1(self):
        print("Метод f_func1() класу Class1")
        
 
class Class2():
    
    def __init__(self):
        super().__init__()
        self.member2 = 222
        self.member1 = 9000000000
 #       self.member23 = 222333
        
    def f_func2(self):
        print ("Метод f_func2() класу Class2")
 
class Class3():
    def __init__(self):
        super().__init__()
        self.member3 = 333
        self.member1 = 222222222200000
#        self.member23 = 333222
        
    def f_func1(self):
        print ("Метод f_func1() класу Class3")
    def f_func2(self):
        print ("Метод f_func2() класу Class3")
    def f_func3(self):
        print ("Метод f_func3() класу Class3")
    def f_func4(self):
        print ("Метод f_func4() класу Class3")
 
class Class4(Class2, Class3):

    def __init__(self):
        super().__init__()
      #  Class2.__init__(self)
      #  Class3.__init__(self)
        self.member4 = 444
    
    def f_func4(self):
        print ("Метод f_func4() класу Class4")
  #      for f in Class4.__bases__:
  #          f().f_func2()
  #      super().f_func2()
 
c1 = Class4()

print (c1.member1)
print (c1.member2)
print (c1.member3)
print (c1.member4)
#print (c1.member23)


#print (Class4.__mro__ )

