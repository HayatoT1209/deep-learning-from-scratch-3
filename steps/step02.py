import numpy as np
from step01 import Variable


# Base class of functions
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        # The forward method must be implemented for each specific function
        raise NotImplementedError()


# Squares the input
class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y


if __name__ == "__main__":
    x = Variable(np.array(2))
    f = Square()
    y = f(x)
    print(y.data)

    f = Function()
    y = f(x)
