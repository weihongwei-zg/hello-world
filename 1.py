import numpy as np
import tensorflow as tf
#定义前行传播
def sig(m,x,w,y):
    for i in range(0,m):
        z = np.matmul(w,np.matrix(x[i])) + b[i]
        a = tf.sigmoid(z)
        J += -( y[i]*np.log(a) + (1 - y[i])* np.log(1-a) )
        dz = a - y[i]
        dw1 += x[i][0]*dz
        dw2 += x[i][1]*dz
        db += dz
    J /= m
    dw1 /= m
    dw2 /= m
    db /= m
    w[] = w1-A*dw1
    w2 = w2-A*dw2
    b = b-A*db
#主函数
if __name__ == '__main__':
    #初始化数据
    J = dw1 = dw2 = db =0
    m = 10
    A = 0.001
    x = np.random.randint(0,10,(m,2))
    w = np.random.randint(0,10,(1,2))
    y = np.random.rand(m,1)
    #定义反向传播
    for j in range(0,300):
        
        sig(m,x,w,y)
