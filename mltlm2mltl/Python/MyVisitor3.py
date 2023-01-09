from MLTLMVisitor import MLTLMVisitor
from MLTLMParser import MLTLMParser
from MyExpression3 import MyExpression3
import sys
import math
import pytest
from moduloReduction3 import moduloReduction3

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


class MyVisitor3(MLTLMVisitor):
    def __init__(self, stackedExps=[]):
        self.stackedExps = stackedExps
    
    def visitProgram(self, ctx: MLTLMParser.ProgramContext):
        return super().visitProgram(ctx)
    def visitUnary_expr(self, ctx: MLTLMParser.Unary_exprContext):
        temp = MyExpression3()
        sub2 = ctx.expr()
        tempi = ctx.Number()
        
        if not tempi:
            temp.opName = ctx.op.text
        else:
            temp.opName = ctx.UnaryOperators().getText()
            temp.timeName = ctx.Identifier().getText()
        
        for bound in tempi:
            temp.bounds.append(int(bound.getText()))
        
        temp.left = ""
        temp.right = sub2.getText()

        self.stackedExps.append(temp.copy())
        temp.clear()
        nowSize = len(self.stackedExps)

        # print("before \n")
        # for mem in self.stackedExps:
        #     print(mem)
        #     print("\n")
        
        super().visit(sub2)

        # print("after \n")
        # for mem in self.stackedExps:
        #     print(mem)
        #     print("\n")
        if (len(self.stackedExps) > nowSize):
            self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                self.stackedExps[nowSize -
                             1].right = self.stackedExps[nowSize].reconstruct2()
            else:
                pack = moduloReduction3(
                    self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                self.stackedExps[nowSize - 1].right = pack.string
                self.stackedExps[nowSize - 1].prefactor= addPrefactors(self.stackedExps[nowSize - 1].prefactor,pack.prefactor)
                self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                self.stackedExps[nowSize -1].fromTimeName = self.stackedExps[nowSize].timeName
            if not self.stackedExps[nowSize-1].timeName:
                self.stackedExps[nowSize -1].timeName = self.stackedExps[nowSize - 1].fromTimeName
            self.stackedExps.pop()
        else:
            # if size is same we are at the leaves
            self.stackedExps[nowSize-1].fromTimeName = "a"
            if not self.stackedExps[nowSize - 1].timeName:
                self.stackedExps[nowSize -1].timeName = self.stackedExps[nowSize -1].fromTimeName
        return 0

    def visitBinary_expr(self, ctx: MLTLMParser.Binary_exprContext):
        temp = MyExpression3()
        # print("entering Binary")
        # print(ctx.getText())
        # Get the left and right sides of binary operator
        subs2 = ctx.expr()
        # Get the bounds
        tempi = ctx.Number()
        if not tempi:
            #if empty, it is a propositional binary operator
            # print(ctx.op.text)
            temp.opName = ctx.op.text
        else:
            temp.opName = ctx.BinaryOperators().getText()
            # Get the time name
            temp.timeName = ctx.Identifier().getText()
        if (len(tempi) !=0) :
            temp.bounds.append(int(tempi[0].getText()))
            temp.bounds.append(int(tempi[1].getText()))
        temp.left = subs2[0].getText()
        temp.right = subs2[1].getText()
        self.stackedExps.append(temp.copy())
        temp.clear()
        nowSize = len(self.stackedExps)
        # print("before \n")
        # for mem in self.stackedExps:
        #     print(mem)
        #     print("\n")
        super().visit(subs2[0])
        leftIncreasedQ = True if (len(self.stackedExps) > nowSize) else False
        nowSize2 = len(self.stackedExps)
        super().visit(subs2[1])
        rightIncreaseQ = True if (len(self.stackedExps) > nowSize2) else False
        # print("after \n")
        # for mem in self.stackedExps:
        #     print(mem)
        #     print("\n")
        class Container(object):
            prefactor = ""
            string = ""
            num = 0
        if (len(self.stackedExps) == nowSize + 2):
            # if size is greater, we are not at the leaves
            # Check if both sides of binary operator have the
            # same time name
            # if (self.stackedExps[nowSize].timeName != self.stackedExps[nowSize + 1].timeName):
            #     print("Both sides of binary operator must have the same time name.")

            #self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
            #    self.stackedExps[nowSize - 1].left = self.stackedExps[nowSize].reconstruct2()
                pack1 = Container()
                pack1.string = self.stackedExps[nowSize].reconstruct2()
                pack1.num = 0
                pack1.prefactor = ""
            else:
                pack1 = moduloReduction3(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                if (not pack1.prefactor):
                    self.stackedExps[nowSize - 1].left = pack1.prefactor + pack1.string
            if (self.stackedExps[nowSize+1].timeName == self.stackedExps[nowSize+1].fromTimeName):
                #self.stackedExps[nowSize - 1].right = self.stackedExps[nowSize + 1].reconstruct2()
                pack2 = Container()
                pack2.string = self.stackedExps[nowSize+1].reconstruct2()
                pack2.num = 0
                pack2.prefactor = ""
            else:
                pack2 = moduloReduction3(
                    self.stackedExps[nowSize + 1], self.stackedExps[nowSize + 1].fromTimeName)
                if (not pack2.prefactor):
                    self.stackedExps[nowSize - 1].right = pack2.prefactor + pack2.string
            if pack1.num > pack2.num:
                self.stackedExps[nowSize - 1].prefactor = addPrefactors(self.stackedExps[nowSize - 1].prefactor,pack2.prefactor)
                self.stackedExps[nowSize - 1].left = minusPrefactors(pack1.prefactor, pack2.prefactor) + pack1.string
                self.stackedExps[nowSize - 1].right = pack2.string
            elif pack1.num < pack2.num:
                self.stackedExps[nowSize - 1].prefactor = addPrefactors(self.stackedExps[nowSize - 1].prefactor, pack1.prefactor)
                self.stackedExps[nowSize - 1].left = pack1.string
                self.stackedExps[nowSize - 1].right = minusPrefactors(pack2.prefactor, pack1.prefactor) + pack2.string
            elif pack1.num is pack2.num:
                self.stackedExps[nowSize - 1].prefactor = addPrefactors(self.stackedExps[nowSize - 1].prefactor, pack1.prefactor)
                self.stackedExps[nowSize - 1].left = pack1.string
                self.stackedExps[nowSize - 1].right = pack2.string

            self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
            self.stackedExps[nowSize+1].timeName = self.stackedExps[nowSize+1].fromTimeName
            self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            if not self.stackedExps[nowSize - 1].timeName:
                self.stackedExps[nowSize - 1].timeName = self.stackedExps[nowSize - 1].fromTimeName
            self.stackedExps.pop()
            self.stackedExps.pop()
        elif (len(self.stackedExps) == nowSize + 1):
            # One side is a atomic proposition
            # if (self.stackedExps[nowSize].timeName != "a"):
            #     print("Both sides of binary operator must have the same time name. Note that atomic proposition has default time name \"a\" \n")
    
            self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            # find which side is atomic:
            if not leftIncreasedQ:
                # left side is atomic.
                if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                    self.stackedExps[nowSize - 1].right = self.stackedExps[nowSize].reconstruct2()
                else:
                    pack = moduloReduction3(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                    self.stackedExps[nowSize - 1].right = pack.prefactor + pack.string
                    self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                    self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            elif not rightIncreaseQ:
                # right side is atomic.
                if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                    self.stackedExps[nowSize - 1].left = self.stackedExps[nowSize].reconstruct2()
                else:
                    pack = moduloReduction3(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                    self.stackedExps[nowSize - 1].left = pack.prefactor+ pack.string
                    self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                    self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            else:
                print("Something wrong ?!?")
            if not self.stackedExps[nowSize - 1].timeName:
                self.stackedExps[nowSize - 1].timeName = self.stackedExps[nowSize - 1].fromTimeName
            self.stackedExps.pop()
        else:
            # if size is the same, we are at leaves
            self.stackedExps[nowSize - 1].fromTimeName = "a"
            # If the timeName field is empty (for a prop operator)
            # then time is same as fromTime.
            if not self.stackedExps[nowSize - 1].timeName:
                self.stackedExps[nowSize - 1].timeName = self.stackedExps[nowSize - 1].fromTimeName
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
    ex = MyVisitor3()
    addPrefactors("", "G[4,4]") == "G[4,4]"
    print(ex)


