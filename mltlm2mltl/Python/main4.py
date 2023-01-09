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
from MyVisitor4 import MyVisitor4,addPrefactors
from moduloReduction4 import moduloReduction4


def main(mltlm):
    if (os.path.isfile(mltlm)):
        MLTLM = open(mltlm,"r").read()
    else:
        MLTLM = mltlm
    print("Input: \n")
    print(MLTLM)
    file = open("test_3.MLTL","w")
    lexer = MLTLMLexer(InputStream(MLTLM))
    stream = CommonTokenStream(lexer)
    parser = MLTLMParser(stream)
    tree = parser.program()
    statements = tree.statement()

    vv = MyVisitor4()
    for statement in statements:
        expression = statement.expr()
        vv.visit(expression)
        out = ""
        if not vv.stackedExps:
           file.write(expression.getText())
        else:
            if(vv.stackedExps[0].timeName == vv.stackedExps[0].fromTimeName):
               out = vv.stackedExps[0].reconstruct2()
            else:
                pack = moduloReduction4(
                    vv.stackedExps[0], vv.stackedExps[0].fromTimeName)
                out = pack.prefactor + pack.string
            file.write(out)
        file.write(";\n")
        vv.stackedExps.clear()
    file.close()


if __name__ == "__main__":
    main(sys.argv[1])
