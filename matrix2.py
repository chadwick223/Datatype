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

A=matrix(4,4,[[4,3],[5,6]])
print(A.get_data())
            
    



