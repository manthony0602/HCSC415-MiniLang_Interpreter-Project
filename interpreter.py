from ast_nodes import Block, Assign, Print, Literal, Variable, BinOp

class Environment:
    def __init__(self):
        self.stack = [{}]

    def push(self):
        self.stack.append({})

    def pop(self):
        self.stack.pop()

    def set(self, name, val):
        for scope in reversed(self.stack):
            if name in scope:
                scope[name] = val
                return
        self.stack[-1][name] = val  # fallback: define in current scope

    def get(self, name):
        for scope in reversed(self.stack):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable {name} not found")

def eval_expr(expr, env):
    if isinstance(expr, Literal):
        return expr.value
    elif isinstance(expr, Variable):
        return env.get(expr.name)
    elif isinstance(expr, BinOp):
        left = eval_expr(expr.left, env)
        right = eval_expr(expr.right, env)
        return eval_binary_op(expr.op, left, right)

def eval_binary_op(op, left, right):
    if op == '+': return left + right
    if op == '-': return left - right
    if op == '*': return left * right
    if op == '/': return left / right
    raise RuntimeError(f"Unknown operator {op}")

def interpret(node, env):
    if isinstance(node, Block):
        env.push()
        for stmt in node.stmts:
            interpret(stmt, env)
        env.pop()
    elif isinstance(node, Assign):
        val = eval_expr(node.expr, env)
        env.set(node.name, val)
    elif isinstance(node, Print):
        val = eval_expr(node.expr, env)
        print(val)