from time import sleep
from _thread import start_new_thread
def factorial(x):
    t=0
    if x<1:
        t=1
    else:
        ret_val = x*factorial(x-1)
        print("{} != {}".format(str(x), str(ret_val)))
        t=ret_val
    return t

n = int(input("Enter the number to compute factorial:"))
start_new_thread(factorial,(n,))
sleep(1)


