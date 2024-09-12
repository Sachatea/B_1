import numpy as py

def pseudo(A, b):
    Ar = py.linalg.pinv(A)
    xh = Ar @ b
    eps = b.T @ b - b.T @ A @ Ar @ b 
    return Ar, xh, eps

def start():
    A = py.array([[1,2],[1,2]])
    b = py.array([10,20])

    print(py.column_stack((A,b)))

    ATA = py.linalg.det(A.T @ A)

    print( )

    if ATA > 0:
        print("визначник (1.7) -", ATA)
        print()
        Ar, xh, eps = pseudo(A, b)
        print("єдиний розвязок", xh)
        print()
        print("з точністю (1.8)", float(round(eps, 4)))

    else:
        rang = py.linalg.matrix_rank(A)
        if rang == py.linalg.matrix_rank(py.column_stack((A,b))):
            print("визначник (1.7) -", ATA)
            print()
            Ar, xh, eps = pseudo(A, b)
            v = py.array([0, 0])
            print("існує багато розвязків, один з яких", xh + v - Ar @ (A @ v))
            print()
            print("з точністю (1.8)", float(round(eps, 4)))

        else:
            print("визначник (1.7) -", ATA)
            print()
            Ar, xh, eps = pseudo(A, b)
            v = py.array([0, 0])
            print("не існує точного розвязку, лише", xh + v - Ar @ (A @ v))
            print()
            print("з точністю (1.8)", float(round(eps, 4)))


if __name__ == "__main__":
   start()