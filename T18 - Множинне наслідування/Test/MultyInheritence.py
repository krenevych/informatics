class Class1:         
    def f_func0(self):
        print("Метод f_func0() класу Class1")
    def f_func1(self):
        print("Метод f_func1() класу Class1")
        
 
class Class2(Class1): 
    def f_func2(self):
        print ("Метод f_func2() класу Class2")
 
class Class3(Class1):
    def f_func1(self):
        print ("Метод f_func1() класу Class3")
    def f_func2(self):
        print ("Метод f_func2() класу Class3")
    def f_func3(self):
        print ("Метод f_func3() класу Class3")
    def f_func4(self):
        print ("Метод f_func4() класу Class3")
 
class Class4(Class2, Class3): 
    def f_func4(self):
        print ("Метод f_func4() класу Class4")
 
c1 = Class4()

c1.f_func1()            
c1.f_func2()
c1.f_func3()              
c1.f_func4()
c1.f_func0()

print (Class4.__mro__ )

