"""
    A simple Linear Algebra Lib

    Methods
    -------
    MatMult:    Returns product of  two nxn matrices

    TwoDet:     Returns the det of a 2x2 matrix

    LUDecomp:   Returns the Lower and Upper matrices given a nxn matrix A, 
                Method assumes A is viable for LU-Decomp.

    det:        Returns the det of a viable LU-Decomp matrix. 


"""
def MatMult(A: list, B: list, n: int) -> list:
    """Return a  2-dimensional list given two nxn matrices and the size n

    Keyword arguments:
    A -- A nxn 2-dimensional list
    B -- A nxn 2-dimensional list
    n -- The size n for A and B, if n is greater the matrix will be padded
    """
    
    # C is our return matrix
    # We are init a nxn mat with
    # all 0's
    C = [ [0] * n for index in range(n)]
    
    ###
    # iter row of A
    # iter Col of b indexed at 0
    # iter the inside appending the 
    # appropraite scalar value to C. 
    ###
    for row in range(len(A)):
        for col in range(len(B[0])):
            for nestRow in range(len(B)):
                C[row][col] += A[row][nestRow] * B[nestRow][col]

def TwoDet(A: list) -> list:
    """Return the determinant of a 2x2 matrix

    Keyword arguments:
    A -- A nxn 2-dimensional list
    """
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

def LUDecomp(A: list,n: int):
    """Return the LU decomp of a nxn matrix

    Keyword arguments:
    A -- A nxn 2-dimensional list
    n -- size of the square matrix
    """

    # init L and U to be nxn populated with 0's
    L = [ [0] * n for index in range(n)]
    U = [ [0] * n for index in range(n)]
 
    # populate the upper and lower matrices decomped from A
    for row in range(n):
        # Upper
        for nestCol in range(row, n):
            tmpMation = 0
            for col in range(row):
                tmpMation = tmpMation + (L[row][col] * U[col][nestCol])
            # Set U index
            U[row][nestCol] = A[row][nestCol] - tmpMation
        # Lower
        for nestCol in range(row, n):
            if (row == nestCol):
                L[row][row] = 1
            else:
                tmpMation = 0
                for j in range(row):
                    tmpMation = tmpMation + (L[nestCol][col] * U[col][row])
                # Set L index
                L[nestCol][row] = float((A[nestCol][row] - tmpMation) / U[row][row])
    return U,L
    

    
def det(A: list, n:int) -> int:
    """Return the det of an nxn matrix

    Keyword arguments:
    A -- A nxn 2-dimensional list
    n -- size of the square matrix
    """

    # get U and L matrices from A,
    # take the products of each main diag
    # then mult the two values from U and L
    # the scalar will be the det of A.
    #
    # Proof
    # A = LU --> det(A) = det(LU) = det(L) det(U)
    # then we just get the eigenvalues from each
    # d(U) and d(L).
    ###
    U,L = LUDecomp(A,n)
    detU = 1
    mainDUp =[U[i][i] for i in range(n)]
    for index in mainDUp:
        detU *= index

    detL = 1
    mainDLow =[L[i][i] for i in range(n)]
    for w in mainDLow:
        detL *= w

    return detU * detL
     


# def main():
#      3x3 matrix A
#     A =[[1,0,2],[-4,1,1],[3,2,3]]
#   
#     2x2 matrix B
#     B = [[3,-9],
#          [1,4]]
#
#     Size n given as 3
#     n = 3
#     MatMult(A,B,n)
#     U,L = LUDecomp(A,n)
#     det(A,n)
# main()
