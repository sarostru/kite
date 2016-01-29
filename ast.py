from rply.token import BaseBox

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
    def __init__(self, arg):
        self.arg = arg
    
    def eval(self, env):
        return self._op(self.arg.eval(env))

class Positive(UnaryOp):

    def _op(self, arg):
        return +arg

class Negative(UnaryOp):
    def _op(self, arg):
        return -arg

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def eval(self, env):
        return self._op(self.left.eval(env), self.right.eval(env))

class Add(BinaryOp):
    def _op(self, left, right):
        return left + right

class Sub(BinaryOp):
    def _op(self, left, right):
        return left - right

class Mul(BinaryOp):
    def _op(self, left, right):
        return left * right

class Div(BinaryOp):
    def _op(self, left, right):
        return left / right
