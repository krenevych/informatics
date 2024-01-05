cur = 0

def mydec(func):
    def _mydec(*args, **kw):
        global cur
        cur += 1
        print(cur)
        func(*args)
    return _mydec



@mydec
def func(*args):
    print(args)



def f(filename):
    file = open(filename, "r")
    for line in file:
        func(line)
    file.close()
    


f("test.txt")


        

        
    
