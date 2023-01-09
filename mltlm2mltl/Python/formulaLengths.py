#!/usr/bin/env python3
import re
import pyparsing
import numpy as np

def formulaLengths(inFile):
    try:
        with open(inFile, 'r') as f:
            f1 = f.read()
    except FileNotFoundError:
        print('Formula file does not exist in one\n')
        os.system("say failed")
        return
    commentFilter = pyparsing.pythonStyleComment.suppress()
    newTest = commentFilter.transformString(f1)
    newTest = re.sub(r"\n","",newTest)
    newTest = newTest.split(";")
    numFormula = len(newTest)
    lengths = np.zeros((numFormula,1))
    for i,formula in enumerate(newTest,start=0):
        newString = re.sub(r'\[[^]]*\]', '', formula)
        newString = re.sub(r'\(', '', newString)
        newString = re.sub(r'\)', '', newString)
        newString = re.sub(r' ', '', newString)
        newString = re.sub(r'[0-9+]', '', newString)
        #print(newString)
        lengths[i] = len(newString)
    return lengths


if __name__ == "__main__":
    formulaLengths("randomTest4.mltlm")
