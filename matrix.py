#addition of matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[4,5,6],[1,2,3],[7,8,9]]
R=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        R[i][j]=A[i][j]+B[i][j];
for r in range(len(R[0])):
    print(R[r])

#multliplication of matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[4,5,6],[1,2,3],[7,8,9]]
R=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            R[i][j]+=A[i][j]*B[i][j];
for r in range(len(R[0])):
    print(R[r])

#subtraction of matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[4,5,6],[1,2,3],[7,8,9]]
R=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        R[i][j]=A[i][j]-B[i][j];
for r in range(len(R[0])):
    print(R[r])

#transpose of matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
R=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(R[0])):
        R[j][i]=A[i][j]
for r in range(len(A[0])):
    print(R[r])