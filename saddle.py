A=[[1,8,2],[7,1,0],[4,8,3]]
for i in range(len(A)):
    min_row=A[i][0]
    col_ind=0
    for j in range(3):
        if (min_row > A[i][j]):
            min_row = A[i][j]
            col_ind =j
            if(j<=2):
                break
for k in range (2):
    if (min_row > A[k][col_ind]):
        print("saddle point is:",min_row)
        break
    else:
        print("saddle point is not present")