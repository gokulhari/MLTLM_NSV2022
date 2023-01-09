# This script tests that the two translators 
# do the same thing.
# This is accomplished in the following manner:
# (future) First a test.MLTLM is generated.
# This is translated by running main1 and main2, and 
# they each generate test_1.MLTL and test_2.MLTL
# The code then generates inputs
# The code then runs r2u2prep for test_1.MLTL
# it generates the binaries, and then it also 
# runs the code r2u2.c and generates output_1.txt
# we do the same with test_2.MLTL.

import sys
import os
import subprocess
import shlex
import shutil
import re
import argparse
import numpy as np
import pyparsing

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
    return [times,verdicts]
        
# You would need to change these to specify the absolute path to MLTLM version of R2U2:
PathToR2U2 = "/Users/gokul/Nok/r2u2ref/r2u2_MLTLM_Publish/"
# Specify python path, only tested on Python 3.7.7, OSX.
PathToPython = "/Users/gokul/anaconda3/bin/python"
PathToTranslator = PathToR2U2 + "mltlm2mltl/Python"
def main():
    print("Testing translators ...")
    fail = False

    os.chdir(PathToTranslator)
    os.system(PathToPython + " main.py randomTest5.mltlm" )
    os.system(PathToPython + " main2.py randomTest5.mltlm")
    os.system(PathToPython + " main3.py randomTest5.mltlm")
    #os.system("python3 main.py test.MLTLM" )
    #os.system("python3 main2.py test.MLTLM")
    #os.system("python3 main3.py test.MLTLM")
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
    os.chdir("../../")
    #os.system("python3")
    print(os.getcwd())
    for j in range(52):
        logfile_a = open("logfile_a" + str(j) + ".txt", "w")
        args = shlex.split(
            PathToPython + " tools/r2u2prep.py mltlm2mltl/Python/test_1.MLTL")
        subprocess.run(args,stdout=logfile_a,stderr=logfile_a)
        args = shlex.split(
            "./R2U2_C/bin/r2u2 " + PathToR2U2 + "tools/gen_files/binary_files/ " + PathToR2U2 + "test/Inputs/inputFiles/input" + str(j) + ".csv")
        subprocess.run(args,stdout=logfile_a,stderr=logfile_a)
        os.system("mv R2U2.log R2U2_1.log")
        subprocess.run(["./tools/split_verdicts.sh","R2U2_1.log"], stdout=logfile_a)

        logfile_b = open("logfile_b" + str(j) + ".txt", "w")
        args = shlex.split(
            PathToPython + " tools/r2u2prep.py mltlm2mltl/Python/test_2.MLTL")
        subprocess.run(args, stdout=logfile_b, stderr=logfile_b)
        args = shlex.split(
            "./R2U2_C/bin/r2u2 " + PathToR2U2 + "tools/gen_files/binary_files/ " + PathToR2U2 + "test/Inputs/inputFiles/input" + str(j) + ".csv")
        subprocess.run(args, stdout=logfile_b, stderr=logfile_b)
        os.system("mv R2U2.log R2U2_2.log")
        subprocess.run(["./tools/split_verdicts.sh", "R2U2_2.log"],stdout=logfile_b)

        logfile_c = open("logfile_c" + str(j) + ".txt", "w")
        args = shlex.split(
            PathToPython + " tools/r2u2prep.py mltlm2mltl/Python/test_3.MLTL")
        subprocess.run(args, stdout=logfile_c, stderr=logfile_c)
        args = shlex.split(
            "./R2U2_C/bin/r2u2 " + PathToR2U2 + "tools/gen_files/binary_files/ " + PathToR2U2 + "test/Inputs/inputFiles/input" + str(j) + ".csv")
        subprocess.run(args, stdout=logfile_c, stderr=logfile_c)
        os.system("mv R2U2.log R2U2_3.log")
        subprocess.run(["./tools/split_verdicts.sh", "R2U2_3.log"], stdout=logfile_c)


        logfile_a.close()
        logfile_b.close()
        logfile_c.close()
        # Next we need to tally the two split verdicts from the two logs
        # open the files:

        performulanorm = []
        for i in range(numFormula):
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

            try:
                with open("R2U2_3_formula" + str(i) + ".txt", 'r') as f:
                    f3 = f.read()
            except FileNotFoundError:
                print('Formula file does not exist in three\n')
                os.system("say failed")
                return

            [times,verdicts] = fToTimeVerdict(f1)
            vec1 = expandComputation(times,verdicts)

            [times, verdicts] = fToTimeVerdict(f2)
            vec2 = expandComputation(times, verdicts)

            [times, verdicts] = fToTimeVerdict(f3)
            vec3 = expandComputation(times, verdicts)

            performulanorm.append(np.linalg.norm(vec1-vec2))
            performulanorm.append(np.linalg.norm(vec2-vec3))
            performulanorm.append(np.linalg.norm(vec3-vec1))
        
        if np.linalg.norm(np.array(performulanorm)) != 0:
            fail = True

        if (fail):
            print("Test failed.")
            os.system("say failed")
            return
        else:
            print("Test passed " + str(j) + "/51.")
            os.system("rm R2U2_1_formula*")
            os.system("rm R2U2_2_formula*")
            os.system("rm R2U2_3_formula*")
            os.system("rm logfile_a" + str(j) + ".txt")
            os.system("rm logfile_b" + str(j) + ".txt")
            os.system("rm logfile_c" + str(j) + ".txt")
    os.system("say done")
    
    


if __name__ == "__main__":
    main()
