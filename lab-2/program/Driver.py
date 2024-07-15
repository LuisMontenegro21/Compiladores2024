import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        #print("visitAssign called")
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        print(f"Assigned {id} = {value}")
        return value

    def visitPrintExpr(self, ctx):
        #print("visitPrintExpr called")
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitMulDiv(self, ctx):
        #print("visitMulDiv called")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            result = left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError(f"Error: cannot divide {left} by zero") # adding some defensive programming
            result = left / right
        print(f"MulDiv: {left} {op} {right} = {result}")
        return result

    def visitAddSub(self, ctx):
        #print("visitAddSub called")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            result = left + right
        else:
            result = left - right
        print(f"AddSub: {left} {op} {right} = {result}")
        return result

    def visitInt(self, ctx):
        #print("visitInt called")
        value = int(ctx.INT().getText())
        print(f"Int: {value}")
        return value
    
    # for comparison operators, just 2 included for the moment
    def visitComparison(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == "==":
            result = left == right
        elif op == "!=":
            result = left != right
        print(f"Comparison: {left} {op} {right} = {result}")
        return result

    def visitId(self, ctx):
        #print("visitId called")
        id = ctx.ID().getText()
        if id not in self.memory:
            raise NameError(f"Warning: Variable {id} was not declared") # in case the id was not declared
        value = self.memory.get(id, 0)
        print(f"Id: {id} = {value}")
        return value

    def visitParens(self, ctx):
        #print("visitParens called")
        return self.visit(ctx.expr())
    
    # to handle if conditions
    def visitIfStat(self, ctx):
        #print("visitIfStat called")
        condition = self.visit(ctx.expr())
        if condition:
            for stat in ctx.stat():
                self.visit(stat)
        return 0

    # to handle while conditions
    def visitWhileStat(self, ctx):
        #print("visitWhileStat called")
        while self.visit(ctx.expr()):
            for stat in ctx.stat():
                self.visit(stat)
        return 0

    # to handle function 
    def visitFuncDef(self, ctx):
        #print("visitFuncDef called")
        func_name = ctx.ID().getText()
        func_body = ctx.stat()
        self.functions[func_name] = func_body
        print(f"Defined function {func_name}")
        return 0
    
    # to call functions
    def visitCallFunc(self, ctx):
        print("visitCallFunc called")
        func_name = ctx.ID().getText()
        if func_name in self.functions:
            func_body = self.functions[func_name]
            for stat in func_body:
                self.visit(stat)
        else:
            raise NameError(f"Error: Function '{func_name}' is not defined")
        return 0
    
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog() # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

    
    #print(tree.toStringTree(recog=parser))

    eval = EvalVisitor()
    eval.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
