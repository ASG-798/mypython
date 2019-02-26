class addfr:
    def __init__(self,a,b):
        self.num=a
        self.den=b
    def add(t1,t2):
        f1=addfr(t1[0],t1[1])
        f2=addfr(t2[0],t2[1])
        fnum=f1.num*f2.den+f1.den*f2.num
        fden=f1.den*f2.den
        return fnum,fden
