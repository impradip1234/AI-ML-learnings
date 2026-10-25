import time
# designing a cheche system if the value is in the cheche then it will
# return from there else it will execute the function, store the value in chache and print it 

# decorater
def chache(funcn):
    chache_c={}
    def wrapper(*args):
        print(chache_c)
        if args in chache_c:
            return chache_c[args]
        result = funcn(*args)
        chache_c[args]=result
        return result
    return wrapper



@chache
def add(a,b):
    time.sleep(4)
    return (a+b)

print(add(5,6))
print(add(4,9))