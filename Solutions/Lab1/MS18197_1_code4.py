a=1
import numpy as np
def SingleEp(a):
    epsilon=np.single(1)
    machine=np.single(1)
    while epsilon + machine != epsilon:
        last_machine=machine
        machine = machine/np.single(2)   
    return last_machine

def DoubleEp(a):
    epsilon=1
    machine=1
    while epsilon + machine != epsilon:
        last_machine=machine
        machine = machine/2
    return last_machine

print("machine epsilon for single precision: {}".format(SingleEp(1)))
print("machine epsilon for double precision: {}".format(DoubleEp(1)))