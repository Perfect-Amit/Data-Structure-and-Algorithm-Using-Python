class OrderedStream:

    def __init__(self, n):
        self.arr=[""]*(n+1)
        self.ptr=1

    def insert(self, idKey, value):
        self.arr[idKey]=value
        res=[]

        while self.ptr<len(self.arr) and self.arr[self.ptr]!="":
            res.append(self.arr[self.ptr])
            self.ptr+=1

        return res