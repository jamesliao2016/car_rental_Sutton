# poisson probability
import numpy as np
from math import *
# Poisson probability density
def poisProbDen(lambdax,nx,bound):
    if nx<bound:
        probRlt = pow(lambdax,nx)*exp(-lambdax)/factorial(nx)
    else:
        probRlt = 1 - poisProbAcc(lambdax,nx,bound)
    return probRlt

# Poisson accumulate probability
def poisProbAcc(lambdax,nx,bound):
    probAccRlt = 0.0
    for qq in range(nx+1):
        probAccRlt+=poisProbDen(lambdax,qq,bound)
    return probAccRlt

# Return the arrival number based on the poisson distribution
def retPoiNum(lambdax,bound):
    jj = np.random.uniform()
    rlt = 0
    for kk in range(100):
        dd1 = poisProbAcc(lambdax,kk,bound)
        dd2 = poisProbAcc(lambdax,(kk+1),bound)

        if jj > dd1 and jj < dd2:
            rlt = kk
            # print(' %f %f %f' % (dd1, dd2, jj))
            break
    return rlt

if __name__ == '__main__':
    for jj in range(10):
        print(poisProbDen(3,jj,20))
        print(jj)
