# Generated from MLTLM.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MLTLMParser import MLTLMParser
else:
    from MLTLMParser import MLTLMParser

# This class defines a complete listener for a parse tree produced by MLTLMParser.
class MLTLMListener(ParseTreeListener):

    # Enter a parse tree produced by MLTLMParser#program.
    def enterProgram(self, ctx:MLTLMParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLTLMParser#program.
    def exitProgram(self, ctx:MLTLMParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLTLMParser#statement.
    def enterStatement(self, ctx:MLTLMParser.StatementContext):
        pass

    # Exit a parse tree produced by MLTLMParser#statement.
    def exitStatement(self, ctx:MLTLMParser.StatementContext):
        pass


    # Enter a parse tree produced by MLTLMParser#contract.
    def enterContract(self, ctx:MLTLMParser.ContractContext):
        pass

    # Exit a parse tree produced by MLTLMParser#contract.
    def exitContract(self, ctx:MLTLMParser.ContractContext):
        pass


    # Enter a parse tree produced by MLTLMParser#unary_expr.
    def enterUnary_expr(self, ctx:MLTLMParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by MLTLMParser#unary_expr.
    def exitUnary_expr(self, ctx:MLTLMParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by MLTLMParser#binary_expr.
    def enterBinary_expr(self, ctx:MLTLMParser.Binary_exprContext):
        pass

    # Exit a parse tree produced by MLTLMParser#binary_expr.
    def exitBinary_expr(self, ctx:MLTLMParser.Binary_exprContext):
        pass


    # Enter a parse tree produced by MLTLMParser#bool_expr.
    def enterBool_expr(self, ctx:MLTLMParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by MLTLMParser#bool_expr.
    def exitBool_expr(self, ctx:MLTLMParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by MLTLMParser#atom_expr.
    def enterAtom_expr(self, ctx:MLTLMParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by MLTLMParser#atom_expr.
    def exitAtom_expr(self, ctx:MLTLMParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by MLTLMParser#parens_expr.
    def enterParens_expr(self, ctx:MLTLMParser.Parens_exprContext):
        pass

    # Exit a parse tree produced by MLTLMParser#parens_expr.
    def exitParens_expr(self, ctx:MLTLMParser.Parens_exprContext):
        pass


    # Enter a parse tree produced by MLTLMParser#binding.
    def enterBinding(self, ctx:MLTLMParser.BindingContext):
        pass

    # Exit a parse tree produced by MLTLMParser#binding.
    def exitBinding(self, ctx:MLTLMParser.BindingContext):
        pass


    # Enter a parse tree produced by MLTLMParser#mapping.
    def enterMapping(self, ctx:MLTLMParser.MappingContext):
        pass

    # Exit a parse tree produced by MLTLMParser#mapping.
    def exitMapping(self, ctx:MLTLMParser.MappingContext):
        pass



del MLTLMParser