import poisEventFun as pef
import numpy as np
import reallotFun as rllt
import queueFun as qf

def returnVal(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal,cm1,cm2,rm1,rm2):
    # Simulation START here
    tt = 0
    while tt < 100:
    # while True:
        gg=[]
        tt+=1
        # (numCar1,numCar2): the current cars of the two sites
        for numCar1 in range(upCarNum):
            for numCar2 in range(upCarNum):
                iniRaw = [numCar1,numCar2]
                iniCars = [numCar1, numCar2]
                oldVal = valVec[numCar1][numCar2]
                iniCarsUp, mvNumAbs, polTmp = rllt.moveCar(iniCars, carPol[numCar1][numCar2], upCarNum)
                valBellTmp = 0.0
                for con1 in range(len(cm1)):
                    for con2 in range(len(cm2)):
                        returnValConstant = True
                        if returnValConstant:
                            ret1 = repArr[0]
                            ret2 = repArr[1]
                            tmpArr = [con1, con2]
                            tmpRep = [ret1, ret2]
                            iniCarsTmp, rentVec = rllt.reallot(iniCarsUp, tmpArr, tmpRep, upCarNum)
                            joinProb = cm1[con1] * cm2[con2]
                            vt = rllt.calVal(rentVec, mvNumAbs)
                            valBellTmp += joinProb * (vt + rhoVal * valVec[iniCarsTmp[0]][iniCarsTmp[1]])
                        else:
                            for ret1 in range(len(rm1)):
                                for ret2 in range(len(rm2)):
                                    tmpArr = [con1, con2]
                                    tmpRep = [ret1, ret2]
                                    iniCarsTmp, rentVec = rllt.reallot(iniCarsUp, tmpArr, tmpRep, upCarNum)
                                    joinProb = cm1[con1] * cm2[con2] * rm1[ret1] * rm2[ret2]

                                    vt = rllt.calVal(rentVec, mvNumAbs)
                                    valBellTmp += joinProb * (vt + rhoVal * valVec[iniCarsTmp[0]][iniCarsTmp[1]])
                valVec[iniRaw[0]][iniRaw[1]] = valBellTmp
                    # Policy improvement
                diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
                gg.append(diffVal)
        if (max(gg) < epsDltBase) and (max(gg)>=0):
            break
    return valVec

if __name__ == '__main__':
    import poisEventFun as pef
    import numpy as np
    import reallotFun as rllt
    import retValFun as rvf
    import queueFun as qf
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
    valVec = [[(0.0) for x in range(w + 1)] for y in range(h + 1)]

    # Simulation parameters
    simPeriod = 2
    iniCars = [10, 10]
    lostSale = [(i - i) for i in range(len(iniCars))]
    vt = 0
    mvNumAbs = 0
    epsDltBase = 10
    epsDlt = 100
    ww = 1
    vtHist = [2]

    # Transition matrix
    # tm1 = qf.transitFull(1000, upCarNum, conArr[0], repArr[0])
    # tm2 = qf.transitFull(1000, upCarNum, conArr[1], repArr[1])
    arrBound = 10
    cm1 = [pef.poisProbDen(conArr[0],jj,arrBound) for jj in range(arrBound)]
    # sumtm1 = np.sum(tm1)
    cm2 = [pef.poisProbDen(conArr[1], jj, arrBound) for jj in range(arrBound)]
    rm1 = [pef.poisProbDen(repArr[0], jj, arrBound) for jj in range(arrBound)]
    rm2 = [pef.poisProbDen(repArr[1], jj, arrBound) for jj in range(arrBound)]

    # Simulation START here

    valVec = rvf.returnVal(valVec, carPol, iniCars, epsDltBase, conArr, repArr, upCarNum, rhoVal)
    print(valVec)
    print("--- %s seconds ---" % (time.time() - start_time))

#
# def returnVal(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal,tm1,tm2):
#     # Simulation START here
#     tt = 0
#     while tt < 100:
#         gg=[]
#         tt+=1
#         # (numCar1,numCar2): the current cars of the two sites
#         for numCar1 in range(upCarNum):
#             for numCar2 in range(upCarNum):
#                 iniRaw = [numCar1,numCar2]
#                 iniCars = [numCar1, numCar2]
#                 oldVal = valVec[numCar1][numCar2]
#                 iniCarsUp, mvNumAbs = rllt.moveCar(iniCars, carPol[numCar1][numCar2], upCarNum)
#                 valBellTmp = 0.0
#                 # if (np.sum(tm1[iniCarsUp[0]]) + np.sum(tm2[iniCarsUp[1]]) ==0.0):
#                 #     continue
#                 # (reqCar1,reqCar2): the updated cars of the two sites
#                 for sevCar1 in range(upCarNum):
#                     for sevCar2 in range(upCarNum):
#                         # if (np.sum(tm1[iniCarsUp[0]][sevCar1]) + np.sum(tm2[iniCarsUp[1]][sevCar2]) == 0.0):
#                         #     continue
#                         for leftCar1 in range(upCarNum):
#                             for leftCar2 in range(upCarNum):
#                                 arrProb1 = tm1[iniCarsUp[0]][sevCar1][leftCar1]
#                                 arrProb2 = tm2[iniCarsUp[1]][sevCar2][leftCar2]
#                                 joinProb = arrProb1 * arrProb2
#                                 if joinProb == 0:
#                                     continue
#                                 rentVec = [sevCar1,sevCar2]
#                                 vt = rllt.calVal(rentVec, mvNumAbs)
#                                 valBellTmp += joinProb * (vt + rhoVal * valVec[leftCar1][leftCar2])
#                 valVec[iniRaw[0]][iniRaw[1]] = valBellTmp
#                     # Policy improvement
#                 diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
#                 gg.append(diffVal)
#         if (max(gg) < epsDltBase) and (max(gg)>=0):
#             break
#     return valVec
