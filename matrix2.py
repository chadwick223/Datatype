class matrix:
    
    def __init__(self,m,n,data=None):
        self.__m=m
        self.__n=n
        self.__data=None

        if data is None:
            self.__createzeromatrix()
        else:
            self.set_data(data)
    def __createzeromatrix(self):
        self.__data=[]
        for i in range(self.__m):
            row=[]
            for j in range(self.__n):
                row.append(0)
            self.__data.append(row)
    
    def __validatedata(self,data):

        if not isinstance(data,list):
            return ("data must be in list format")
        if len(data) !=self.__m:
            return(f"Matrix must have {self.__m} rows")
        for rows in data:
            if len(rows)!=self.__n:
                return (f"matrix must have {self.__n} columns")
            
    def set_data(self,data):

        validation_result=self.__validatedata(data)

        if validation_result is not None:
            return validation_result
        else:
            self.__data= data
            return ("data set successfully")
    def set_rows(self,new_row):
        if type(new_row)==int:
            self.__m=new_row
        else:
            print("Not Allowed")
           
    def set_cols(self,new_cols):
        if type(new_cols)==int:
            self.__n=new_cols
        else:
            print("Not Allowed")

    def get_data(self):
        return self.__data
    def get_rows(self):
        return self.__m
    def get_cols(self):
        return self.__n
    def __str__(self):
        result=""
        for row in self.__data:
            row_string= ""
            for value in row:
                row_string += str(value) + " "
            result+= row_string.rstrip() + "\n"
        return result.rstrip()
    
    def __add__(self,other):
        if not isinstance(other,type(self)) or self.__m != other.__m or self.__n !=other.__n:
            return("Unsupproted format")
        else:
            matrix_addition=[]
            for i in range (self.__m):
                row=[]
                for j in range(self.__n):
                    temp=self.__data[i][j] +other.__data[i][j]
                    row.append(temp)
                matrix_addition.append(row)
            
            ## A+B  should return the same type as A and B . both A and B are matrix, so A+b should also be matrix

            return matrix(self.__m,self.__n,matrix_addition)
    def __sub__(self,other):
        if not isinstance(other,type(self)) or self.__m!=other.__m or self.__n!=other.__n:
            return("Unsupported format")
        else:
            matrix_substraction=[]
            for i in range (self.__m):
                row=[]
                for j in range(self.__n):
                    temp=self.__data[i][j]-other.__data[i][j]
                    row.append(temp)
                matrix_substraction.append(row)
            return matrix(self.__m,self.__n,matrix_substraction)
    def __mul__(self,other):
        if not isinstance(other,type(self)) or self.__n!=other.__m:
            return ("matrix multiplication not possible")
        else:
            multiplied_matrix=[]
            for i in range(self.__m):
                row=[]
                for j in range(other.__n):
                    sum_val=0
                    for k in range(self.__n):
                        sum_val+=self.__data[i][k]*other.__data[k][j]
                    row.append(sum_val)
                multiplied_matrix.append(row)
            return matrix(self.__m,other.__n,multiplied_matrix)




A=matrix(1,3,[[3,1,4]])
B=matrix(3,2,[[4,3],[2,5],[6,8]])
print(A*B)

    



