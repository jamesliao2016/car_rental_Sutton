
input_x = list(range(10))
input_y = [1,1,1,-1,-1,-1,1,1,1,-1]

def pred_fun(val_x,val_t):
    if val_x < val_t:
        return 1
    else:
        return -1

def valid_fun(val_x,val_y,val_t):
    if pred_fun(val_x,val_t) == val_y:
        return 0
    else:
        return 1

def err_rt(wt,data_x,data_y):
    rlt = 0
    ii = 0
    for wti in wt:
        val_x = data_x[ii]
        val_y = data_y[ii]
        rlt = rlt + wti * valid_fun(val_x,val_y,val_t)
        ii += 1
    return rlt

wt = [0.1 + ii - ii for ii in range(10)]
val_t = 2.5

val_err_rt = (err_rt(wt,input_x,input_y))

import numpy as np

def fun_wt(val_err_rt):
    return 0.5 * np.log((1 - val_err_rt)/val_err_rt)

val_fun_wt = fun_wt(val_err_rt)

def update_wt(wt,val_t,data_x,data_y,val_fun_wt):
    rlt = []
    ii = 0
    for wti in wt:
        val_x = data_x[ii]
        val_y = data_y[ii]
        tmp1 = wti * np.exp(-val_fun_wt * val_y * pred_fun(val_x,val_t))
        rlt.append(tmp1)
        ii += 1
    sum_rlt = sum(rlt)
    rlt2 = [tmp_val/sum_rlt for tmp_val in rlt]
    return rlt2

wt =  update_wt(wt,val_t,input_x,input_y,val_fun_wt)
print(wt)


