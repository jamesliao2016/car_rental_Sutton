if __name__ == '__main__':
    import poisEventFun as pef
    import numpy as np
    import reallotFun as rllt
    import retValFun as rvf
    import policyImproveFun as pif

    import time

    start_time = time.time()

    # Parameters
    locNum = 2
    conArr = [3, 4]
    repArr = [3, 2]
    upCarNum = 20
    rhoVal = 0.9
    epsEval = 0.1

    # Policy
    w, h = upCarNum, upCarNum;
    carPol = [[0 for x in range(w + 1)] for y in range(h + 1)]
    valVec = [[(0.0) for x in range(w)] for y in range(h)]

    # Simulation parameters
    simPeriod = 2
    iniCars = [10, 10]
    lostSale = [(i - i) for i in range(len(iniCars))]
    vt = 0
    mvNumAbs = 0
    epsDltBase = 1e-2
    epsDlt = 100
    ww = 1
    vtHist = [2]

    # Generate distribution
    arrBound = 10
    cm1 = [pef.poisProbDen(conArr[0],jj,arrBound) for jj in range(arrBound)]
    cm2 = [pef.poisProbDen(conArr[1], jj, arrBound) for jj in range(arrBound)]
    rm1 = [pef.poisProbDen(repArr[0], jj, arrBound) for jj in range(arrBound)]
    rm2 = [pef.poisProbDen(repArr[1], jj, arrBound) for jj in range(arrBound)]

    # Simulation START here
    yy = 0
    while yy<10:

        valVec = rvf.returnVal(valVec, carPol, iniCars, epsDltBase, conArr, repArr, upCarNum, rhoVal,cm1,cm2,rm1,rm2)
        print(valVec)
        print("--- %s seconds ---" % (time.time() - start_time))

        carPolNew = pif.polImprove(valVec, carPol, iniCars, epsDltBase, conArr, repArr, upCarNum, rhoVal,cm1,cm2,rm1,rm2)
        print(carPolNew)
        print("--- %s seconds ---" % (time.time() - start_time))
        if carPolNew == carPol:
            break
        carPol = carPolNew
        yy += 1
