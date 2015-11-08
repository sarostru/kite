from rply import LexerGenerator
lg = LexerGenerator()

lg.add('NUMBER', r'\d+')

lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')

lg.ignore(r'\s+')