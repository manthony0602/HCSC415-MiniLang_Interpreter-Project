from lexer import tokenize
from parser import Parser
from interpreter import interpret, Environment

if __name__ == '__main__':
    with open('test_program.txt') as f:
        code = f.read()

    tokens = list(tokenize(code))
    for token in tokens:
        print(token)  # Debug: print tokens to verify input

    parser = Parser(tokens)
    ast = parser.parse()
    env = Environment()
    interpret(ast, env)