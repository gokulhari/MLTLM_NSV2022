#!/usr/bin/env python3

# %%
import matplotlib.pyplot as plt
import sys
import os
import subprocess
import shlex
import shutil
import re
import argparse
import numpy as np
from numpy.core.numeric import ones
import pyparsing
import matplotlib
from formulaLengths import formulaLengths
# %%

os.chdir("/Users/gokul/Nok/r2u2ref/r2u2/mltlm2mltl/Python") 
matplotlib.rcParams['font.family'] = "CMU Serif"
plt.style.use(['presentation.mplstyle', 'grayscale'])

def fileOpenAndEvaluate(file):
    os.system("./main.py " + file)
    os.system("./main2.py " + file)
    os.system("./main3.py " + file)
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    lengths4 = formulaLengths(file)
    #var = input("wait")
    lengths1 = formulaLengths("test_1.MLTL") 
    # var = input("wait")
    lengths2 = formulaLengths("test_2.MLTL") 
    # var = input("wait")
    lengths3 = formulaLengths("test_3.MLTL") 
    # var = input("wait")

    mat = np.hstack((lengths1, lengths2,  lengths3, lengths4))
    return mat

def formulawiseNumberOfInstructionAndMemory(inFile):
    try:
        with open(inFile, 'r') as f:
            f1 = f.read()
    except FileNotFoundError:
        print('Formula file does not exist in one\n')
        os.system("say failed")

    formulas = f1.split("\n")
    while not formulas[-1]:
        formulas.pop()
    tempArray = np.zeros((len(formulas), 1))
    tempArray2 = np.zeros((len(formulas), 1))
    
    
    for (i, formula) in enumerate(formulas):
        #print("Formula: " + formula)
        #print("Command: " + "python3 tools/r2u2prep.py \"" + formula + "\" ")
        os.system("python3 tools/r2u2prep.py \"" + formula + "\" ")
        try:
            with open("tools/gen_files/binary_files/ft.asm", "r") as f:
                f1 = f.read()

        except FileNotFoundError:
            print("ft.asm does not exist.")
            os.system("say failed")
            var= input()

        temp = f1.split("\n")
        while not temp[-1]:
            temp.pop()
        tempArray[i] = len(temp)
        
        try:
            with open("tools/gen_files/binary_files/ftscq.asm", "r") as f:
                f1 = f.read()
        except FileNotFoundError:
            print("ftscq does not exist.")
            os.system("say failed")
            var = input()
        temp = f1.split("\n")
        while not temp[-1]:
            temp.pop()
        lastline = temp.pop()
        lastlinelist = lastline.split(" ")
        tempArray2[i] = int(lastlinelist[1]) + 1
    return [tempArray,tempArray2]

def plotBySort(mat,out,ylabel):
    mat2 = np.matrix([np.ones(60)*mat[:, 0].mean(), np.ones(60)*mat[:, 1].mean(),
                      np.ones(60)*mat[:, 2].mean(), np.ones(60)*mat[:, 3].mean()])
    mat2 = np.transpose(mat2)
    mat3 = np.matrix(mat)
    arr = np.argsort(mat[:, 3])
    mat[:, 0] = mat[arr[:], 0]
    mat[:, 1] = mat[arr[:], 1]
    mat[:, 2] = mat[arr[:], 2]
    mat[:, 3] = mat[arr[:], 3]

    plt.clf()
    plt.plot(mat[:, 0], "*r", mat[:, 1], "ob", mat[:, 2], "dg", mat[:, 3], "xk", mat2[:, 0],
             ":r", mat2[:, 1], "--b", mat2[:, 2], "-.g", mat2[:, 3], "-k", fillstyle="none")
    plt.xlabel("$i$", fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend(["Translator 1", "Translator 2",
                "Translator 3", "MLTLM"], fontsize=18)
    plt.savefig(out, bbox_inches='tight')

def plotBycumsum(mat,out,ylabel):
    mat1 = np.cumsum(mat, axis=0)
    plt.clf()
    plt.semilogy(mat1[:, 0], ":r", mat1[:, 1], "--b", mat1[:, 2],
             "-.g", mat1[:, 3], "-k", fillstyle="none")
    plt.xlabel("Number of Formulas", fontsize=20)
    plt.ylabel("Cumulative " + ylabel, fontsize=20)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend(["Translator 1", "Translator 2",
                "Translator 3", "MLTLM"], fontsize=18)

    out1 = out.split(".")
    plt.savefig(out1[0] + "cum." + out1[1], bbox_inches='tight')
    
def plotterForMe(infile,out):
    mat = fileOpenAndEvaluate(infile)

    plotBySort(mat,out,"Formula Length")
    plotBycumsum(mat, out, "Formula Length")
    
    

    

# %%

# plotterForMe("random/P0.mltlm","PlotsAndPics/some1.svg")
# plotterForMe("random/P02.mltlm","PlotsAndPics/some2.svg")
# plotterForMe("random/P04.mltlm","PlotsAndPics/some3.svg")
# plotterForMe("random/P06.mltlm","PlotsAndPics/some4.svg")
# plotterForMe("random/P08.mltlm","PlotsAndPics/some5.svg")
# plotterForMe("random/P1.mltlm","PlotsAndPics/some6.svg")
# plotterForMe("randomTest5.mltlm", "PlotsAndPics/some10.svg")
# os.system("say done")
# mat1 = fileOpenAndEvaluate("random/P0.mltlm")
#print(mat1)
#var = input("enter \n")
# mat2 = fileOpenAndEvaluate("random/P02.mltlm")
# mat3 = fileOpenAndEvaluate("random/P04.mltlm")
# mat4 = fileOpenAndEvaluate("random/P06.mltlm")
# mat5 = fileOpenAndEvaluate("random/P08.mltlm")
# mat6 = fileOpenAndEvaluate("random/P1.mltlm")


# meanLen1 = np.zeros(6)
# meanLen2 = np.zeros(6)
# meanLen3 = np.zeros(6)
# meanLen4 = np.zeros(6)
# probs = np.array([0.0,0.2,0.4,0.6,0.8,1.0])

# meanLen1[0] = mat1[:,0].mean()
# meanLen1[1] = mat2[:, 0].mean()
# meanLen1[2] = mat3[:, 0].mean()
# meanLen1[3] = mat4[:,0].mean()
# meanLen1[4] = mat5[:,0].mean()
# meanLen1[5] = mat6[:, 0].mean()

# #print(meanLen1)
# #var = input()
# meanLen2[0] = mat1[:, 1].mean()
# meanLen2[1] = mat2[:, 1].mean()
# meanLen2[2] = mat3[:, 1].mean()
# meanLen2[3] = mat4[:, 1].mean()
# meanLen2[4] = mat5[:, 1].mean()
# meanLen2[5] = mat6[:, 1].mean()
# #print(meanLen2)
# #var = input()
# meanLen3[0] = mat1[:, 2].mean()
# meanLen3[1] = mat2[:, 2].mean()
# meanLen3[2] = mat3[:, 2].mean()
# meanLen3[3] = mat4[:, 2].mean()
# meanLen3[4] = mat5[:, 2].mean()
# meanLen3[5] = mat6[:, 2].mean()

# meanLen4[0] = mat1[:, 3].mean()
# meanLen4[1] = mat2[:, 3].mean()
# meanLen4[2] = mat3[:, 3].mean()
# meanLen4[3] = mat4[:, 3].mean()
# meanLen4[4] = mat5[:, 3].mean()
# meanLen4[5] = mat6[:, 3].mean()

# #print(meanLen3)
# #var = input()
# # %%
# plt.clf()
# plt.semilogy(probs, meanLen1, ":r", probs, meanLen2,  "--ob", probs, meanLen3,  "-.dg",probs,meanLen4,  "-xk", fillstyle="none")
# plt.xlabel("Probability of Choosing a Temporal Operator", fontsize=20)
# plt.ylabel("Mean Formula Length", fontsize=20)
# plt.xticks([0,0.2,0.4,0.6,0.8,1], fontsize=18)
# # plt.yticks([0,20,40,60,80,100,120,140,160,180,200], fontsize=18)

# plt.legend(["Translator 1", "Translator 2", "Translator 3","MLTLM"], fontsize=18)
# plt.savefig('PlotsAndPics/some7.svg', bbox_inches='tight')
# plt.clf()
#%%
#print(mat.shape)
# ftas.py 18,
# ftas.py 42
# ftas.py 78
# Measuring number of instructions per formula
# Convert the MLTLM formulas to MLTL using three translators
fileOpenAndEvaluate("randomTest5.mltlm")
os.chdir("../../")
[mltlmInslens,mltlmInsMem] = formulawiseNumberOfInstructionAndMemory("mltlm2mltl/Python/randomTest5.mltlm")
[test1Inslens,test1InsMem] = formulawiseNumberOfInstructionAndMemory("mltlm2mltl/Python/test_1.MLTL")
[test2Inslens,test2InsMem] = formulawiseNumberOfInstructionAndMemory("mltlm2mltl/Python/test_2.MLTL")
[test3Inslens,test3InsMem] = formulawiseNumberOfInstructionAndMemory("mltlm2mltl/Python/test_3.MLTL")
indices = np.linspace(0,len(mltlmInslens)-1,len(mltlmInslens))
os.chdir("mltlm2mltl/Python/")
matlens = np.hstack((test1Inslens,test2Inslens,test3Inslens,mltlmInslens))
matmems = np.hstack((test1InsMem,test2InsMem,test3InsMem,mltlmInsMem))

memdata = np.column_stack((test1InsMem,test2InsMem,test3InsMem,mltlmInsMem))
insdata = np.column_stack((test1Inslens,test2Inslens,test3Inslens,mltlmInslens))
np.savetxt("memdata.csv", memdata, delimiter=", ", fmt="%d", header="Translate 1, Translate 2, Translate 3, MLTLM", comments="")
np.savetxt("insdata.csv", insdata, delimiter=", ", fmt="%d", header="Translate 1, Translate 2, Translate 3, MLTLM", comments="")

plotBySort(matlens,"PlotsAndPics/some8.svg", "Number of Observers")
plotBycumsum(matlens,"PlotsAndPics/some8.svg","Number of Observers")
plotBySort(matmems,"PlotsAndPics/some9.svg","Number of Slots")
plotBycumsum(matmems,"PlotsAndPics/some9.svg","Number of Slots")
# plt.yticks([0,3000,6000,9000,12000,15000,18000,21000,24000, 27000, 30000], fontsize=18)
plt.savefig("PlotsAndPics/some9cum.svg", bbox_inches='tight')
os.system("say done")