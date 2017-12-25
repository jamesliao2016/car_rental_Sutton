import poisEventFun as pef
import numpy as np
import reallotFun as rllt

import retValFun as rvf

def polImprove(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal,cm1,cm2,rm1,rm2):
    # Simulation START here
    # carPolRlt = [[0 for x in range(upCarNum + 1)] for y in range(upCarNum + 1)]
    carPolRlt = carPol.copy()

    for numCar1 in range(upCarNum):
        for numCar2 in range(upCarNum):
            iniRaw = [numCar1,numCar2]
            iniCars = [numCar1, numCar2]
            oldVal = valVec[numCar1][numCar2]
            optVal = valVec[numCar1][numCar2]
            # optAction = carPol[numCar1][numCar2]
            for action in range(-5,6):
                iniCarsUp, mvNumAbs, polTmp = rllt.moveCar(iniCars, action, upCarNum)
                valBellTmp = 0.0
                if (action >= 0 and numCar1 >= action) or (action < 0 and numCar2 >= abs(action)):
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
                                        tmpArr = [con1,con2]
                                        tmpRep = [ret1,ret2]
                                        iniCarsTmp, rentVec = rllt.reallot(iniCarsUp, tmpArr, tmpRep, upCarNum)
                                        joinProb = cm1[con1] * cm2[con2] * rm1[ret1] * rm2[ret2]

                                        vt = rllt.calVal(rentVec, mvNumAbs)
                                        valBellTmp += joinProb * (vt + rhoVal * valVec[iniCarsTmp[0]][iniCarsTmp[1]])
                    if valBellTmp > (optVal):
                        optVal = valBellTmp
                        # optAction = action
                        carPolRlt[numCar1][numCar2] = polTmp
    return carPolRlt

