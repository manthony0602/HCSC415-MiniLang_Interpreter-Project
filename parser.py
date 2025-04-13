from lexer import tokenize
from ast_nodes import Block, Assign, Print, Literal, Variable, BinOp

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def match(self, kind):
        if self.peek()[0] == kind:
            self.pos += 1
            return self.tokens[self.pos - 1][1]
        raise SyntaxError(f'Expected {kind} but got {self.peek()}')

    def parse(self):
        return self.parse_block()

    def parse_block(self):
        self.match('LBRACE')
        stmts = []
        while self.peek()[0] != 'RBRACE':
            stmts.append(self.parse_stmt())
        self.match('RBRACE')
        return Block(stmts)

    def parse_stmt(self):
        print("Current token in parse_stmt:", self.peek())  # Debug

        if self.peek() == ('KEYWORD', 'print'):
            self.match('KEYWORD')
            self.match('LPAREN')
            expr = self.parse_expr()
            self.match('RPAREN')
            self.match('END')
            return Print(expr)

        elif self.peek()[0] == 'KEYWORD':
            typename = self.match('KEYWORD')
            name = self.match('ID')
            self.match('ASSIGN')
            expr = self.parse_expr()
            self.match('END')
            return Assign(name, expr)

        elif self.peek()[0] == 'ID':
            name = self.match('ID')
            self.match('ASSIGN')
            expr = self.parse_expr()
            self.match('END')
            return Assign(name, expr)

        elif self.peek()[0] == 'LBRACE':
            return self.parse_block()

        else:
            raise SyntaxError('Invalid statement')

    def parse_expr(self):
        left = self.parse_term()
        while self.peek()[1] in ('+', '-'):
            op = self.match('OP')
            right = self.parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek()[1] in ('*', '/'):
            op = self.match('OP')
            right = self.parse_factor()
            left = BinOp(left, op, right)
        return left

    def parse_factor(self):
        kind, value = self.peek()
        if kind == 'INT':
            self.match('INT')
            return Literal(int(value))
        elif kind == 'FLOAT':
            self.match('FLOAT')
            return Literal(float(value))
        elif kind == 'STRING':
            self.match('STRING')
            return Literal(value.strip('"'))
        elif kind == 'ID':
            return Variable(self.match('ID'))
        elif kind == 'LPAREN':
            self.match('LPAREN')
            expr = self.parse_expr()
            self.match('RPAREN')
            return expr
        else:
            raise SyntaxError(f'Unexpected token: {value}')