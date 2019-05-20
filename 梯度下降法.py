import numpy as np
#import tensorflow as tf
#定义前行传播
def sig(m,x,w,b,y):
    J = dw1 = dw2 = db =0    
    for i in range(0,m):
        z = np.matmul(w,np.matrix(x[i])) + b[i]
        #a = tf.sigmoid(z)
        a = 1/(1+np.e**(-1*z))
        
        J += -( y[i]*np.log(a) + (1 - y[i])* np.log(1-a) )
        dz = a - y[i]
        dw1 += x[i][0]*dz
        dw2 += x[i][1]*dz
        db += dz
    J /= m
    dw1 /= m
    dw2 /= m
    db /= m
    w[0] = w[0]-A*dw1
    w[1] = w[1]-A*dw2
    b = b-A*db
#主函数
if __name__ == '__main__':
    #初始化数据
    m = 10
    A = 0.001
    x = np.random.randint(0,10,(m,2))
    w = np.random.randint(1,10,(1,2))
    y = np.random.rand(m,1)
    b = np.random.randint(1,10,(1,1))
    #定义反向传播
    for j in range(0,100):
        sig(m,x,w,b,y)
        if j % 10 == 0:
            print(w,b)
