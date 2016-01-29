import os
from lexer import lexer as l
from kparser import parser as p

# File Descriptor numbers
# TODO:: Should be wrapped in a few simple stream layers
#        why not in Rpython already (??)
STDIN = 0
STDOUT = 1


# TODO:: Environment should be a recursive dict, single layer at the moment
#   No dict in RPython, so environment will have to be a {}
# class Environment(dict):
#     pass
def Environment():
    return {}

class ParserState(object):
    pass

def eval(exp, env, pstate):
    return p.parse(l.lex(exp), state=pstate).eval(env)

# Quick shortcut function for line by line testing
def qeval(exp):
    return eval(exp, env={}, pstate=ParserState())

def readline(ins=0, outs=1, prompt=""):
    # Pulled this from the braid repo, you have to use os ops in 
    # rpython.
    os.write(outs, prompt)
        
    res = ''
    while True:
        buf = os.read(ins, 64)
        if not buf:
            return res
        res += buf
        if res[-1] == '\n':
            return res[:-1]

def printline(result, rprompt=">"):
    print(rprompt + str(result))
            
def driver_loop(driver, env, pstate=None):
    prompt = "('-')>> "
    rprompt = "('-')   "
    while True:
        line = readline(ins=STDIN, outs=STDOUT, prompt=prompt)
        # TODO:: Exiting should probably not take up a symbol name
        if line == "quit":
            print(prompt + " Goodbye cruel world!")
            break
        result = eval(exp=line, env=env, pstate=pstate)
        printline(result, rprompt=rprompt)

class MockJitDriver(object):
    def __init__(self,**kw): pass
    def jit_merge_point(self,**kw): pass
    def can_enter_jit(self,**kw): pass
        
def start(driver=None):
    if driver is None:
        driver = MockJitDriver()
    pstate = ParserState()
    env = Environment()
    driver_loop(driver=driver, env=env, pstate=pstate)

