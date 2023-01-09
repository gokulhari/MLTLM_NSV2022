# Generated from MLTLM.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MLTLMParser import MLTLMParser
else:
    from MLTLMParser import MLTLMParser

# This class defines a complete generic visitor for a parse tree produced by MLTLMParser.

class MLTLMVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLTLMParser#program.
    def visitProgram(self, ctx:MLTLMParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#statement.
    def visitStatement(self, ctx:MLTLMParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#contract.
    def visitContract(self, ctx:MLTLMParser.ContractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#unary_expr.
    def visitUnary_expr(self, ctx:MLTLMParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#binary_expr.
    def visitBinary_expr(self, ctx:MLTLMParser.Binary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#bool_expr.
    def visitBool_expr(self, ctx:MLTLMParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#atom_expr.
    def visitAtom_expr(self, ctx:MLTLMParser.Atom_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#parens_expr.
    def visitParens_expr(self, ctx:MLTLMParser.Parens_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#binding.
    def visitBinding(self, ctx:MLTLMParser.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLTLMParser#mapping.
    def visitMapping(self, ctx:MLTLMParser.MappingContext):
        return self.visitChildren(ctx)



del MLTLMParser