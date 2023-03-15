import numpy as np
from step01 import Variable
from step02 import Function, Square


class Exp(Function):
    def forward(self, x):
        return np.exp(x)


if __name__ == "__main__":
    # Composite functions
    x = Variable(0.5)
    A = Square()
    B = Exp()
    C = Square()

    a = A(x)
    b = B(a)
    c = C(b)
    print(c.data)

    # Or compute all at once
    print(C(B(A(x))).data)
