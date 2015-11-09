from rply.token import BaseBox
import operator

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class UnaryOp(BaseBox):
    def __init__(self, op, arg):
        self.arg = arg
        self.op = op
    
    def eval(self):
        return self.op(self.arg.eval())

class Positive(UnaryOp):
    def __init__(self, arg):
        super(Positive, self).__init__(operator.pos, arg)

class Negative(UnaryOp):
    def __init__(self, arg):
        super(Negative, self).__init__(operator.neg, arg)

class BinaryOp(BaseBox):
    def __init__(self, op, left, right):
        self.left = left
        self.right = right
        self.op = op
    
    def eval(self):
        return self.op(self.left.eval(), self.right.eval())

class Add(BinaryOp):
    def __init__(self, left, right):
        super(Add, self).__init__(operator.add, left, right)

class Sub(BinaryOp):
    def __init__(self, left, right):
        super(Sub, self).__init__(operator.sub, left, right)

class Mul(BinaryOp):
    def __init__(self, left, right):
        super(Mul, self).__init__(operator.mul, left, right)

class Div(BinaryOp):
    def __init__(self, left, right):
        super(Div, self).__init__(operator.div, left, right)
