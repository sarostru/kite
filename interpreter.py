import os
from lexer import lexer as l
from kparser import parser as p

# File Descriptor numbers
# TODO:: Should be wrapped in a few simple stream layers
#        why not in Rpython already (??)
STDIN = 0
STDOUT = 1


# TODO:: Environment should be a recursive dict, single layer at the moment
class Environment(dict):
    def __init__(self, parent):
        self.parent = parent

class ParserState(object):
    def __init__(self, root_env):
        self.env = root_env

# Quick shortcut function for line by line testing
def qeval(exp):
    return p.parse(l.lex(exp)).eval()

def eval(exp, state):
    return p.parse(l.lex(exp), state=state).eval()
    
def readline(ins=0, outs=1, prompt=""):
    
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
            
def driver_loop(state):
    prompt = "('-')>>"
    rprompt = "('-')>>>"
    while True:
        line = readline(ins=STDIN, outs=STDOUT, prompt=prompt)
        if line == "quit()":
            print(prompt + " Goodbye cruel world!")
            break
        result = eval(line, state)
        printline(result, rprompt=rprompt)
        
def start():
    global_state = ParserState({})
    driver_loop(global_state)

