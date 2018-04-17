import cProfile
import random
import time
start=time.time()
def create1(t):
    s1=random.randint(1,10)
    s2=random.randint(1,10)
    s3=random.choice(['+','-','*','/'])
    calcul(s1,s2,s3,t)
def create2(t):
    s1=random.randint(1,10)
    s2=random.randint(s1,11)
    s3=random.randint(1,10)
    s4=random.randint(s3,11)
    s5=random.choice(['+','-'])
    sr="第"+str(t)+"题："+str(s1)+'÷'+str(s2)+s5+str(s3)+'÷'+str(s4)+'='
    l1.append(sr)
    if s5=='+':
        l2.append(s1/s2+s3/s4)
    else:
        if s1/s2-s3/s4>0:
            l2.append(s1/s2-s3/s4)
        else:
            sr="第"+str(t)+"题："+str(s3)+'÷'+str(s4)+s5+str(s1)+'÷'+str(s2)+'='
            l2.append(s3/s4-s1/s2)
def calcul(s1,s2,s3,t):
    sr="第"+str(t)+"题："+str(s1)+s3+str(s2)+'='
    if s3=='+':
        l2.append(s1+s2)
    elif s3=='-':
        if s1>=s2:
            l2.append(s1-s2)
        else:
            sr="第"+str(t)+"题："+str(s2)+s3+str(s1)+'='
            l2.append(s2-s1)
    elif s3=='*':
        sr="第"+str(t)+"题："+str(s1)+'x'+str(s2)+'='
        l2.append(s1*s2)
    elif s3=='/':
        sr="第"+str(t)+"题："+str(s1)+'÷'+str(s2)+'='
        l2.append(s1/s2)
    l1.append(sr)
t=1
l1=[]
l2=[]
score=0
while t<=10:
    if t<=5:
        create1(t)
    elif t<=10:
        create2(t)
    print(l1[t-1])
    n=eval(input())
    if l2[t-1]==n:
        score+=10
        print("回答正确！")
    else:
        print("回答错误！")
    t+=1
print("你的得分为：%d"%score)
cProfile.run('calcul')
cProfile.run('create1')
cProfile.run('create2')
end=time.time()
print(end-start)