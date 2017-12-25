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
