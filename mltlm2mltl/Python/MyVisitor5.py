from MLTLMVisitor import MLTLMVisitor
from MLTLMParser import MLTLMParser
from MyExpression3 import MyExpression3
import sys
import math
import pytest
from moduloReduction4 import moduloReduction4

def addPrefactors(prefactora, prefactorb):

    if (prefactora and prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])

        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
    elif (not prefactora) and (not prefactorb):
        vala1 = 0
        vala2 = 0
        valb1 = 0
        valb2 = 0
    elif not prefactora:
        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
        vala1 = 0
        vala2 = 0
    else:
       valas = prefactora[2:]
       valas = valas.split(",")
       vala1 = int(valas[0])
       vala2 = valas[1].split("]")
       vala2 = int(vala2[0])
       valb1 = 0
       valb2 = 0
    val1 = vala1 + valb1
    val2 = vala2 + valb2
    if (val1 == 0) and (val2 == 0):
        return ""
    else:
        return "G[" + str(val1) + "," + str(val2) + "]"

def minusPrefactors(prefactora,prefactorb):
    if (prefactora and prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])

        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
    elif (not prefactora) and (not prefactorb):
        vala1 = 0
        vala2 = 0
        valb1 = 0
        valb2 = 0
    elif (not prefactora):
        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
        vala1 = 0
        vala2 = 0
    elif (not prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])
        valb1 = 0
        valb2 = 0
    val1 = vala1 - valb1
    val2 = vala2 - valb2
    
    if (val1 < 0) or (val2 < 0):
        sys.exit("Internal indices are negative")
    elif (val1 == 0) and (val2 == 0):
        return ""
    else:
        return "G[" + str(val1) + "," + str(val2) + "]"


class MyVisitor5(MLTLMVisitor):
    def __init__(self, stackedExps=[]):
        self.stackedExps = stackedExps
        self.isProp = False
    def visitProgram(self, ctx: MLTLMParser.ProgramContext):
        return super().visitProgram(ctx)
    def visitUnary_expr(self, ctx: MLTLMParser.Unary_exprContext):
        temp = MyExpression3()
        sub2 = ctx.expr()
        tempi = ctx.Number()
        
        if not tempi:
            self.isProp = True
        else:
            self.isProp = False
        return 0

    def visitBinary_expr(self, ctx: MLTLMParser.Binary_exprContext):
        temp = MyExpression3()
        subs2 = ctx.expr()
        tempi = ctx.Number()
        if not tempi:
            #if empty, it is a propositional binary operator
            # print(ctx.op.text)
            temp.opName = ctx.op.text
            self.isProp = True
        else:
            self.isProp = False
        return 0


def test_addPrefactors():
    assert addPrefactors("", "G[4,4]") == "G[4,4]"
    assert addPrefactors("G[4,4]","") == "G[4,4]"
    assert addPrefactors("G[4,4]","G[6,6]") == "G[10,10]"
    assert addPrefactors("","") == ""
    assert addPrefactors("G[5,10]","G[2,4]") == "G[7,14]"
    assert addPrefactors("", "G[2,4]") == "G[2,4]"
    assert addPrefactors("G[5,10]", "") == "G[5,10]"

def test_minusPrefactors():
    assert minusPrefactors("G[4,4]","") == "G[4,4]"
    assert minusPrefactors("G[6,6]","G[4,4]") == "G[2,2]"
    assert minusPrefactors("G[7,6]","G[3,2]") == "G[4,4]"
    assert minusPrefactors("","") == ""


if __name__ == "__main__":
    ex = MyVisitor5()
    addPrefactors("", "G[4,4]") == "G[4,4]"
    print(ex)


