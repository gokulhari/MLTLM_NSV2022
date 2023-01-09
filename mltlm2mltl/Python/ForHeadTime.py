from MLTLMVisitor import MLTLMVisitor
from MLTLMParser import MLTLMParser
from MyExpression3 import MyExpression3

class ForHeadTime(MLTLMVisitor):
    def __init__(self, stackedExps=[]):
        self.stackedExps = stackedExps
        self.timeName = "a"
    
    def visitProgram(self, ctx: MLTLMParser.ProgramContext):
        return super().visitProgram(ctx)
    def visitUnary_expr(self, ctx: MLTLMParser.Unary_exprContext):
        sub2 = ctx.expr()
        tempi = ctx.Number()
        if not tempi:
            opName = ctx.op.text
            super().visit(sub2)
        else:
            opName = ctx.UnaryOperators().getText()
            self.timeName = ctx.Identifier().getText()
        return 0

    def visitBinary_expr(self, ctx: MLTLMParser.Binary_exprContext):
        tempi = ctx.Number()
        if not tempi:
            opName = ctx.op.text
        else:
            opName = ctx.BinaryOperators().getText()
            # Get the time name
            self.timeName = ctx.Identifier().getText()
        return 0
        
