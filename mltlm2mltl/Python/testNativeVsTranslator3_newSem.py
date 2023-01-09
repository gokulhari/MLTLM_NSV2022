#!/usr/bin/env python3

# This script tests that the translator 
# and native implementation produce the same verdicts

import sys
import os
import subprocess
import shlex
import shutil
import re
import argparse
import numpy as np
import pyparsing
from antlr4 import *
from MLTLMVisitor import MLTLMVisitor
from MLTLMListener import MLTLMListener
from MLTLMLexer import MLTLMLexer
from MLTLMParser import MLTLMParser
from ForHeadTime import ForHeadTime
from math import ceil
from math import floor

def expandComputation(times, verdicts):
    vec = []
    j = 0
    for i in range(len(times)):
        while j < times[i]+1:
            vec.append(verdicts[i])
            j = j+1
    return np.array(vec)

def fToTimeVerdict(f):
    flines = f.splitlines()
    times = []
    verdicts = []
    for line in flines:
        timeVerdict = line.split(",")
        times.append(int(timeVerdict[0]))
        if (timeVerdict[1] == "F"):
            verdicts.append(0)
        else:
            verdicts.append(1)
    return [times, verdicts]

# You would need to change these to specify the absolute path to MLTLM version of R2U2:
PathToR2U2 = "/Users/gokul/Nok/r2u2ref/r2u2_MLTLM_Publish/"
# Specify python path, only tested on Python 3.7.7, OSX.
PathToPython = "/Users/gokul/anaconda3/bin/python"
PathToTranslator = PathToR2U2 + "mltlm2mltl/Python"

def main():
    print("Testing native vs translated versions")
    print("Using translator 3")
    fail = False
    
    os.chdir(PathToTranslator)

    # Generate translated versions: 
    # Translated formulas will be in the file test_3.MLTL.
    os.system(PathToPython + " main3.py randomTest5.mltlm")
    
    try:
        with open("randomTest5.mltlm", 'r') as f:
            f1 = f.read()
    except FileNotFoundError:
        print('Formula file does not exist in one\n')
        os.system("say failed")
        return
    commentFilter = pyparsing.pythonStyleComment.suppress()
    newTest = commentFilter.transformString(f1)
    newTest = newTest.split(";")
    numFormula = len(newTest)-1
    lexer = MLTLMLexer(InputStream(f1))
    stream = CommonTokenStream(lexer)
    parser = MLTLMParser(stream)
    tree = parser.program()
    statements = tree.statement()
    numFormula = len(statements)
    
    os.chdir("../../")

    logfile_a = open("logfile_a.txt", "w")
    args = shlex.split(PathToPython + " tools/r2u2prep.py mltlm2mltl/Python/test_3.MLTL")
    subprocess.run(args, stdout=logfile_a, stderr=logfile_a)
    args = shlex.split("./R2U2_C/bin/r2u2 " + PathToR2U2 + "tools/gen_files/binary_files/ " + PathToR2U2 + "test/Inputs/inputMLTL.csv")
    subprocess.run(args, stdout=logfile_a, stderr=logfile_a)
    os.system("mv R2U2.log R2U2_1.log")
    subprocess.run(["./tools/split_verdicts.sh","R2U2_1.log"], stdout=logfile_a)

    logfile_b = open("logfile_b.txt", "w")
    args = shlex.split(PathToPython + " tools/r2u2prep.py mltlm2mltl/Python/randomTest5.mltlm")
    subprocess.run(args, stdout=logfile_b, stderr=logfile_b)
    args = shlex.split("./R2U2_C/bin/r2u2 " + PathToR2U2 + "tools/gen_files/binary_files/ " + PathToR2U2 + "test/Inputs/inputMLTL.csv")
    subprocess.run(args, stdout=logfile_b, stderr=logfile_b)
    os.system("mv R2U2.log R2U2_2.log")
    subprocess.run(["./tools/split_verdicts.sh","R2U2_2.log"], stdout=logfile_b)

    logfile_a.close()
    logfile_b.close()
    # Next we need to tally the two split verdicts from the two logs
    # open the files:

    performulanorm = []
    for (i,statement) in enumerate(statements):
        forHeadTime = ForHeadTime()
        forHeadTime.visit(statement)
        if (forHeadTime.timeName == "a"):
            stride = 1
        elif (forHeadTime.timeName == "b" ):
            stride = 2
        elif (forHeadTime.timeName == "c"):
            stride = 6
        elif (forHeadTime.timeName == "d"):
            stride = 24
            
        try:
            with open("R2U2_1_formula" + str(i) + ".txt", 'r') as f:
                f1 = f.read()
        except FileNotFoundError:
            print('Formula file does not exist in one\n')
            os.system("say failed")
            return
        try:
            with open("R2U2_2_formula" + str(i) + ".txt", 'r') as f:
                f2 = f.read()
        except FileNotFoundError:
            print('Formula file does not exist in two\n')
            os.system("say failed")
            return

        [times, verdicts] = fToTimeVerdict(f1)
        vec1 = expandComputation(times, verdicts)
        vec1 = vec1[::stride]
        # print(vec1[330:338])
        [times, verdicts] = fToTimeVerdict(f2)
        vec2 = expandComputation(times, verdicts)
        if (len(vec1) > len(vec2)):
            extra = len(vec1) - len(vec2)
            while (extra!=0):
                vec1 = vec1[:-1]
                extra = extra - 1
        elif (len(vec1) < len(vec2)):
            extra = len(vec2) - len(vec1)
            while (extra != 0):
                vec2 = vec2[:-1]
                extra = extra - 1            
        print(i,": ",np.linalg.norm(vec1-vec2))
        performulanorm.append(np.linalg.norm(vec1-vec2))

    if np.linalg.norm(np.array(performulanorm)) != 0:
        fail = True

    if (fail):
        print("Test failed.")
        os.system("say failed")
        return
    else:
        print("Test passed ")
        os.system("rm R2U2_1_formula*")
        os.system("rm R2U2_2_formula*")
        os.system("rm logfile_a.txt")
        os.system("rm logfile_b.txt")
    os.system("say done")


if __name__ == "__main__":
    main()
