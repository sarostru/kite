from rply import ParserGenerator
from ast import *

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['SYMBOL', 'NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'EQUALS', '$end'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV']),
        ('left', ['EQUALS'])
    ]
)

@pg.production('main : statement $end')
def main_statement(state, p):
    return p[0]
    
@pg.production('expression : NUMBER')
def expression_number(state, p):
    return Number(float(p[0].getstr()))
    
@pg.production('expression : SYMBOL')
def expression_symbol(state, p):
    return Symbol(p[0].getstr())

@pg.production('statement : SYMBOL EQUALS expression')
def statement_assign(state, p):
    return Assign(p[0].getstr(), p[2])

@pg.production('statement : expression')
def statement_expr(state, p):
    return p[0]

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(state, p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
def expression_binop(state, p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MUL':
        return Mul(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

@pg.production('expression : PLUS expression')
@pg.production('expression : MINUS expression')
def expression_unaryop(state, p):
    arg = p[1]
    if p[0].gettokentype() == 'PLUS':
        return Positive(arg)
    elif p[0].gettokentype() == 'MINUS':
        return Negative(arg)

@pg.error
def error_handler(state, token):
    token_type = None
    try:
        token_type = token.gettokentype()
    except:
        raise Exception("Parser Error = %s" % token)
    raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())


parser = pg.build()
