from lexer import lexer as l
from kparser import parser as p

def eval(exp):
    return p.parse(l.lex(exp)).eval()