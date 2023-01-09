#!/usr/bin/env python3

import sys
import os 
import subprocess 
import shutil 
import re 
import argparse 
from antlr4 import *
from MLTLMVisitor import MLTLMVisitor
from MLTLMListener import MLTLMListener
from MLTLMLexer import MLTLMLexer
from MLTLMParser import MLTLMParser
#from MyExpression3 import MyExpression3
from MyVisitor5 import MyVisitor5,addPrefactors
from moduloReduction4 import moduloReduction4


def main(mltlm):
    if (os.path.isfile(mltlm)):
        MLTLM = open(mltlm,"r").read()
    else:
        MLTLM = mltlm
    print("Input: \n")
    print(MLTLM)
    file = open("ptest.MLTLM","w")
    lexer = MLTLMLexer(InputStream(MLTLM))
    stream = CommonTokenStream(lexer)
    parser = MLTLMParser(stream)
    tree = parser.program()
    statements = tree.statement()

    vv = MyVisitor5()
    for statement in statements:
        expression = statement.expr()
        isProp = vv.visit(expression)
        out = ""
        if vv.isProp is False:
           file.write(expression.getText())
        else:
            out = "G[0,0,d](" + expression.getText() + ")"
            file.write(out)
        file.write(";\n")
    file.close()


if __name__ == "__main__":
    main(sys.argv[1])
