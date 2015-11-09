from rply.token import BaseBox
import operator

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value

class Symbol(BaseBox):
    def __init__(self, name):
        self.name = name
    
    def eval(self, env):
        return env[self.name]

class Assign(BaseBox):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
    
    def eval(self, env):
        env[self.name] = self.exp.eval(env)
        return env[self.name]
        
class UnaryOp(BaseBox):
    def __init__(self, op, arg):
        self.arg = arg
        self.op = op
    
    def eval(self, env):
        return self.op(self.arg.eval(env))

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
    
    def eval(self, env):
        return self.op(self.left.eval(env), self.right.eval(env))

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
