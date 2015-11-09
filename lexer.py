from rply import LexerGenerator

lg = LexerGenerator()

lg.add('NUMBER', r'\d+(\.\d+)?')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('EQUALS', r'=')
lg.add('SYMBOL', r'[^\s0-9][^\s]*')

lg.ignore(r'\s+')

lexer = lg.build()