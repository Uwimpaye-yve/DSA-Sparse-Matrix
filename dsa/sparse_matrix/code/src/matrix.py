import os
#Function of getting number of rows,columns and tuples

def getTuples(location):
    if not os.path.exists(location):
        raise ValueError("invalid file location") # if the file doesnt exist return this
    with open(location, 'r') as file:
        try:
            #number of rows and cols from file
            rows = int(file.readline().strip().split("=")[1])+1
            cols = int(file.readline().strip().split("=")[1])+1
        except:
            raise ValueError("Invalid file format") # when format is invalid return this
        tuples = []
        for line in file:
            if line.startswith("(") and line.endswith(")\n"):
                values = line.strip("()\n").split(",")
                if len(values) != 3:
                    raise ValueError("Input file has wrong format")
                tuples.append(tuple(map(int, values)))
            else:
                raise ValueError("Input file has wrong format")
        return rows, cols, tuples

# Function to create zero matrix
def Zeromatrix(r,c):
    matrix=[]
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(0)
        matrix.append(row)
    return matrix

#converting tuples into sparse matrix
def Sparcematrix(tuples,rows,cols):
    matrix=Zeromatrix(rows,cols)
    for tuple in tuples:
        r,c,v=tuple
        if r<rows and c<cols:
         matrix[r][c]=v
        else:
            raise ValueError(f"tuple {tuple} is out of range of rows={rows} columns={cols}")
    return matrix
#function to get number of rows and columns
def getRandC(Matrix):
    r=len(Matrix)
    c=len(Matrix[0])
    return r,c
#function to add two matrix
def Add(A,B):
    i,j=getRandC(A)
    x,y=getRandC(B)
    if i==x and j==y:
        Sum=[]
        for r in range(i):
            row=[]
            for c in range(j):
                row.append(A[r][c]+B[r][c])
            Sum.append(row)
        return Sum
    else:
        raise ValueError("can't Add the matrix, number of rows and columns of 1st matrix must be equal to that of 2nd matrix")
#function to subtract two matrix   
def Subs(A,B):
    i,j=getRandC(A)
    x,y=getRandC(B)
    if i==x and j==y:
        sub=[]
        for r in range(i):
            row=[]
            for c in range(j):
                row.append(A[r][c]-B[r][c])
            sub.append(row)
        return sub
    else:
        raise ValueError("can't subtract the matrix, number of rows and columns of 1st matrix must be equal to that of 2nd matrix")
#function to multiply two matrix   
def Mult(A,B):
    i,j=getRandC(A)
    x,y=getRandC(B)
    if j==x:
        Result=[]
        for r in range(i):
            row=[]
            for c in range(y):
                sum=0
                for k in range(j):
                    sum+=A[r][k]*B[k][c]
                row.append(sum)
            Result.append(row)
        return Result
    else:
        raise ValueError("matrice can't be multiplied, rows of first matrix must be equal to columns of second matrix")
#function to convert into tuples
def toTuples(A):
    rows=len(A)
    cols=len(A[0])
    tuples=[]
    for i,row in enumerate(A):
        for j,value in enumerate(row):
            if value != 0:
                tuples.append((i,j,value))
    return rows,cols,tuples
#function to write matrix to file in tuples
def toFile(A,location):
    r,c,tuples=toTuples(A)
    with open(location,'w') as file:
        file.write(f"rows = {r}\n")
        file.write(f"columns = {c}\n")
        for tuple in tuples:
            file.write(f"{tuple}\n") 
#define input and output locations
base_dir=os.path.dirname(__file__)
input_loc=os.path.join(base_dir,"../../sample_inputs")
output_loc=os.path.join(base_dir,"../../sample_outputs")
#define file locat
matrix1_loc=os.path.join(base_dir,f"{input_loc}/easy_sample_01_2.txt")
matrix2_loc=os.path.join(base_dir,f"{input_loc}/easy_sample_02_2.txt")

i,j,A=getTuples(matrix1_loc)
x,y,B=getTuples(matrix2_loc)
#convert tuple to sparse matrix
M1=Sparcematrix(A,i,j)
M2=Sparcematrix(B,x,y)
#perform addition of matrix
summation=Add(M1,M2)
toFile(summation,f"{output_loc}/summation.txt")
#substraction of matrix
subtraction=Subs(M1,M2)
toFile(subtraction,f"{output_loc}/subtraction.txt")
#multiplication of matrix
Multiplication=Mult(M1,M2)
toFile(Multiplication,f"{output_loc}/Multiplication.txt")
