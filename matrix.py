class matrix:

    def __init__(self,n,m,data=None):
        self.__m=m #for rows (vertical)
        self.__n=n #m cols (horizontal)

        if data:
            self.data=data
        
        else:
            self.data=[]
            for i in range(self.__m):
                row = []
                for j in range(self.__n):
                    row.append(0)
                self.data.append(row)
                

A=matrix(2,2,[[2,3],[5,4]])
print(A.__m)
