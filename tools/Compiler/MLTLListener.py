# Generated from MLTL.g by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MLTLParser import MLTLParser
else:
    from MLTLParser import MLTLParser

# This class defines a complete listener for a parse tree produced by MLTLParser.
class MLTLListener(ParseTreeListener):

    # Enter a parse tree produced by MLTLParser#program.
    def enterProgram(self, ctx:MLTLParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLTLParser#program.
    def exitProgram(self, ctx:MLTLParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLTLParser#statement.
    def enterStatement(self, ctx:MLTLParser.StatementContext):
        pass

    # Exit a parse tree produced by MLTLParser#statement.
    def exitStatement(self, ctx:MLTLParser.StatementContext):
        pass


    # Enter a parse tree produced by MLTLParser#contract.
    def enterContract(self, ctx:MLTLParser.ContractContext):
        pass

    # Exit a parse tree produced by MLTLParser#contract.
    def exitContract(self, ctx:MLTLParser.ContractContext):
        pass


    # Enter a parse tree produced by MLTLParser#PropExpr.
    def enterPropExpr(self, ctx:MLTLParser.PropExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#PropExpr.
    def exitPropExpr(self, ctx:MLTLParser.PropExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#BoolExpr.
    def enterBoolExpr(self, ctx:MLTLParser.BoolExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#BoolExpr.
    def exitBoolExpr(self, ctx:MLTLParser.BoolExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#UnaryTemporalExpr.
    def enterUnaryTemporalExpr(self, ctx:MLTLParser.UnaryTemporalExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#UnaryTemporalExpr.
    def exitUnaryTemporalExpr(self, ctx:MLTLParser.UnaryTemporalExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#UnaryTimescaleExpr.
    def enterUnaryTimescaleExpr(self, ctx:MLTLParser.UnaryTimescaleExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#UnaryTimescaleExpr.
    def exitUnaryTimescaleExpr(self, ctx:MLTLParser.UnaryTimescaleExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#ParensExpr.
    def enterParensExpr(self, ctx:MLTLParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#ParensExpr.
    def exitParensExpr(self, ctx:MLTLParser.ParensExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#AtomExpr.
    def enterAtomExpr(self, ctx:MLTLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#AtomExpr.
    def exitAtomExpr(self, ctx:MLTLParser.AtomExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#BinaryTemporalExpr.
    def enterBinaryTemporalExpr(self, ctx:MLTLParser.BinaryTemporalExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#BinaryTemporalExpr.
    def exitBinaryTemporalExpr(self, ctx:MLTLParser.BinaryTemporalExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#BinaryTimescaleExpr.
    def enterBinaryTimescaleExpr(self, ctx:MLTLParser.BinaryTimescaleExprContext):
        pass

    # Exit a parse tree produced by MLTLParser#BinaryTimescaleExpr.
    def exitBinaryTimescaleExpr(self, ctx:MLTLParser.BinaryTimescaleExprContext):
        pass


    # Enter a parse tree produced by MLTLParser#binding.
    def enterBinding(self, ctx:MLTLParser.BindingContext):
        pass

    # Exit a parse tree produced by MLTLParser#binding.
    def exitBinding(self, ctx:MLTLParser.BindingContext):
        pass


    # Enter a parse tree produced by MLTLParser#mapping.
    def enterMapping(self, ctx:MLTLParser.MappingContext):
        pass

    # Exit a parse tree produced by MLTLParser#mapping.
    def exitMapping(self, ctx:MLTLParser.MappingContext):
        pass


    # Enter a parse tree produced by MLTLParser#setAssignment.
    def enterSetAssignment(self, ctx:MLTLParser.SetAssignmentContext):
        pass

    # Exit a parse tree produced by MLTLParser#setAssignment.
    def exitSetAssignment(self, ctx:MLTLParser.SetAssignmentContext):
        pass


    # Enter a parse tree produced by MLTLParser#filterArgument.
    def enterFilterArgument(self, ctx:MLTLParser.FilterArgumentContext):
        pass

    # Exit a parse tree produced by MLTLParser#filterArgument.
    def exitFilterArgument(self, ctx:MLTLParser.FilterArgumentContext):
        pass


    # Enter a parse tree produced by MLTLParser#formulaIdentifier.
    def enterFormulaIdentifier(self, ctx:MLTLParser.FormulaIdentifierContext):
        pass

    # Exit a parse tree produced by MLTLParser#formulaIdentifier.
    def exitFormulaIdentifier(self, ctx:MLTLParser.FormulaIdentifierContext):
        pass


    # Enter a parse tree produced by MLTLParser#setIdentifier.
    def enterSetIdentifier(self, ctx:MLTLParser.SetIdentifierContext):
        pass

    # Exit a parse tree produced by MLTLParser#setIdentifier.
    def exitSetIdentifier(self, ctx:MLTLParser.SetIdentifierContext):
        pass


    # Enter a parse tree produced by MLTLParser#filterIdentifier.
    def enterFilterIdentifier(self, ctx:MLTLParser.FilterIdentifierContext):
        pass

    # Exit a parse tree produced by MLTLParser#filterIdentifier.
    def exitFilterIdentifier(self, ctx:MLTLParser.FilterIdentifierContext):
        pass


    # Enter a parse tree produced by MLTLParser#atomicIdentifier.
    def enterAtomicIdentifier(self, ctx:MLTLParser.AtomicIdentifierContext):
        pass

    # Exit a parse tree produced by MLTLParser#atomicIdentifier.
    def exitAtomicIdentifier(self, ctx:MLTLParser.AtomicIdentifierContext):
        pass


    # Enter a parse tree produced by MLTLParser#signalIdentifier.
    def enterSignalIdentifier(self, ctx:MLTLParser.SignalIdentifierContext):
        pass

    # Exit a parse tree produced by MLTLParser#signalIdentifier.
    def exitSignalIdentifier(self, ctx:MLTLParser.SignalIdentifierContext):
        pass



del MLTLParser