from MLTLMVisitor import MLTLMVisitor
from MLTLMParser import MLTLMParser
from MyExpression3 import MyExpression3
from moduloReduction import moduloReduction

class MyVisitor(MLTLMVisitor):
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
                self.stackedExps[nowSize - 1].right = moduloReduction(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
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
        if (len(self.stackedExps) == nowSize + 2):
            # if size is greater, we are not at the leaves
            # Check if both sides of binary operator have the
            # same time name
            # if (self.stackedExps[nowSize].timeName != self.stackedExps[nowSize + 1].timeName):
            #     print("Both sides of binary operator must have the same time name.")

            self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                self.stackedExps[nowSize - 1].left = self.stackedExps[nowSize].reconstruct2()
            else:
                self.stackedExps[nowSize - 1].left = moduloReduction(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            if (self.stackedExps[nowSize+1].timeName == self.stackedExps[nowSize+1].fromTimeName):
                self.stackedExps[nowSize - 1].right = self.stackedExps[nowSize+1].reconstruct2()
            else:
                self.stackedExps[nowSize - 1].right = moduloReduction(self.stackedExps[nowSize + 1], self.stackedExps[nowSize + 1].fromTimeName)
                self.stackedExps[nowSize+1].timeName = self.stackedExps[nowSize+1].fromTimeName
                self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize+1].timeName
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
            lensub20 = len(subs2[0].children)
            lensub21 = len(subs2[1].children)
            if not leftIncreasedQ:
                # left side is atomic.
                if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                    self.stackedExps[nowSize - 1].right = self.stackedExps[nowSize].reconstruct2()
                else:
                    self.stackedExps[nowSize - 1].right = moduloReduction(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                    self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                    self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            elif not rightIncreaseQ:
                # right side is atomic.
                if (self.stackedExps[nowSize].timeName == self.stackedExps[nowSize].fromTimeName):
                    self.stackedExps[nowSize - 1].left = self.stackedExps[nowSize].reconstruct2()
                else:
                    self.stackedExps[nowSize - 1].left = moduloReduction(self.stackedExps[nowSize], self.stackedExps[nowSize].fromTimeName)
                    self.stackedExps[nowSize].timeName = self.stackedExps[nowSize].fromTimeName
                    self.stackedExps[nowSize - 1].fromTimeName = self.stackedExps[nowSize].timeName
            else:
                print("something wrong ?!?")
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
    



if __name__ == "__main__":
    ex = MyVisitor()
    print(ex)
