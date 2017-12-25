
def reallot(iniCars,tmpArr,tmpRep,upCarNum):
    carsRlt=[]
    rentVec = []
    for tt in range(len(iniCars)):
        lstIx = tt
        if (iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx] > 0):
            rentNum = tmpArr[lstIx]
            carsTmp = iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx]
            carsTmp = min(carsTmp,upCarNum-1)
        else:
            carsTmp = 0
            rentNum = iniCars[lstIx] + tmpRep[lstIx]
            # lostSale[lstIx] += -(iniCars[lstIx] - (tmpArr[lstIx]) + tmpRep[lstIx])
        rentVec.append(rentNum)
        carsRlt.append(carsTmp)
    return carsRlt,rentVec

def calVal(rentVec,mvNumAbs):
    vt = 0
    for yy in rentVec:
        vt += yy * 10
    return vt - mvNumAbs * 2

def moveCar(iniCars,action, upCarNum):

    car1 = iniCars[0]
    car2 = iniCars[1]
    if (action > 0):
        moveNum = min(action,car1,(upCarNum-1 - car2))
        car1 = max(car1 - moveNum,0)
        car2 = min(car2 + moveNum,upCarNum-1)
        policy = moveNum

    else:
        moveNum = min(-action, (upCarNum-1 - car1), car2)
        car1 = min(car1 + moveNum, upCarNum-1)
        car2 = max(car2 - moveNum, 0)
        policy = -moveNum

    return [car1,car2], abs(moveNum), policy