#------------------------------------------------------------------------------------#
# Author:      Matt Cauwels
# Date:        April 16th, 2020
# File Name:   genInputs.py
# Description: A Python 3 script used to generate inputs for various test cases used
#              for R2U2 regression testing. Note that this script is built using the 
#              old Matlab script, "genInputs.m", as a template.
#------------------------------------------------------------------------------------#
import shutil
import numpy as np
import csv
import sys
import os

nRow = 2000
nCol = 5

__AbsolutePath__ = os.path.dirname(os.path.abspath(__file__))+'/'
__InputDir__     = __AbsolutePath__+'inputFiles/'

def makeInputs():
    global nRow, nCol
    #------------------------------------------------------------------------------------#
    # 0.) Both all zeros test cases
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input0'
    f = open(__InputDir__ + filename + '.csv','wb')
    
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            Array[i].append(0.0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 1.) Both all ones test cases
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input1'
    f = open(__InputDir__ + filename + '.csv','wb')
    
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 2.) First Input All True, Second Input All False
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input2'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 3.) First Input All False, Second Input All True
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input3'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 4.) First Input All True, Second Input Oscillating between false and true
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input4'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            elif(j == 1):
                if(np.mod(i,2) == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 5.) First Input All True, Second Input Oscillating between true and false
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input5'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            elif(j == 1):
                if(np.mod(i,2) == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 6.) First Input All False, Second Input Oscillating between false and true
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input6'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(0)
            elif(j == 1):
                if(np.mod(i,2) == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 7.) First Input All False, Second Input Oscillating between true and false
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input7'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            elif(j == 1):
                if(np.mod(i,2) == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 8.) First Input Oscillating between false and true, Second Input All True
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input8'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                if(np.mod(i,2) == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 9.) First Input Oscillating between true and false, Second Input All True
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input9'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                if(np.mod(i,2) == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 10.) First Input Oscillating between false and true, Second Input All False
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input10'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                if(np.mod(i,2) == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 11.) First Input Oscillating between true and false, Second Input All False
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input11'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
        for j in range(0,nCol):
            if(j == 0):
                if(np.mod(i,2) == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 12.) First Input Five Time Step Pulse Wave, Second Input All True
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input12'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 13.) First Input Five Time Step Pulse Wave, Second Input All False
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input13'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 14.) First Input Five Time Step Pulse Wave, Second Input All True
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input14'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 15.) First Input Five Time Step Pulse Wave, Second Input All False
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input15'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 16.) First Input All True, Second Input Five Time Step Pulse Wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input16'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 17.) First Input All False, Second Input Five Time Step Pulse Wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input17'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(0)
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 18.) First Input All True, Second Input Five Time Step Inverse Pulse Wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input18'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(1)
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 19.) First Input All False, Second Input Five Time Step Inverse Pulse Wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input19'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
            
        for j in range(0,nCol):
            if(j == 0):
                Array[i].append(0)
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 20.) Both Inputs are 5 time step pulse waves
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input20'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
        
        for j in range(0,nCol):
            if(flip):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 21.) First Input 5 time step Inverse Pulse Wave. Second Input 5 time step pulse wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input21'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
        
        for j in range(0,nCol):
            if(flip):
                if(j == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                if(j == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 22.) First Input 5 time step Inverse Pulse Wave. Second Input 5 time step pulse wave
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input22'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
        
        for j in range(0,nCol):
            if(flip):
                if(j == 0):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                if(j == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 23.) Both Inputs are 5 time step pulse waves
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input23'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = False
    for i in range(0,nRow):
        Array.append([])
        # Toggle 'flip' every 5 rows
        if(np.mod(i,5) == 0):
            flip = not(flip)
        
        for j in range(0,nCol):
            if(flip):
                Array[i].append(1)
            else:
                Array[i].append(0)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 24.) Both Inputs are five time step pulses, with the second input shifted right by 3
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input24'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = True
    flip2 = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input
        if(np.mod(i,5) == 0):
            flip1 = not flip1
        # Toggle flag for the second input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 25.)  Both Inputs are five time step pulses, with the second input shifted right by 3
    #       First Input Wave is inverse wave.
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input25'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = True
    flip2 = False
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input
        if(np.mod(i,5) == 0):
            flip1 = not flip1
        # Toggle flag for the second input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 26.)  Both Inputs are five time step pulses, with the second input shifted right by 3
    #       Second Wave is Inverse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input26'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = True
    flip2 = False
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input
        if(np.mod(i,5) == 0):
            flip1 = not flip1
        # Toggle flag for the second input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 27.) Both Inputs are five time step pulses, with the second input shifted right by 3
    #      First and second waves are Inverse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input27'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = True
    flip2 = False
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input
        if(np.mod(i,5) == 0):
            flip1 = not flip1
        # Toggle flag for the second input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip2 = not flip2
            
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 28.) Both Inputs are five time step pulses, with the first input shifted right by 3
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input28'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = False
    flip2 = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip1 = not flip1
        # Toggle flag for the second input
        if(np.mod(i,5) == 0):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 29.)  Both Inputs are five time step pulses, with the first input shifted right by 3
    #       Scond Input Wave is inverse wave.
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input29'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = False
    flip2 = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip1 = not flip1
        # Toggle flag for the second input
        if(np.mod(i,5) == 0):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 30.)  Both Inputs are five time step pulses, with the first input shifted right by 3
    #       First Wave is Inverse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input30'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = False
    flip2 = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip1 = not flip1
        # Toggle flag for the second input
        if(np.mod(i,5) == 0):
            flip2 = not flip2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 31.) Both Inputs are five time step pulses, with the second input shifted right by 3
    #      First and second waves are Inverse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input31'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip1 = False
    flip2 = True
    for i in range(0,nRow):
        Array.append([])
        # Toggle flag for the first input, offset by 3 time stamps
        if(np.mod(i-3,5) == 0 and i > 3):
            flip1 = not flip1
        # Toggle flag for the second input
        if(np.mod(i,5) == 0):
            flip2 = not flip2
            
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip1):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip2):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 32.) Figure 4.39
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input32'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
            
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if((i >= 1) and (i <= 5)):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if((i >= 4) and (i <= 8)):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 33.) Example for TACAS14 Paper
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input33'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
            
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if((i >= 11) and (i <= 25)) :
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(((i >= 3) and (i <= 10)) or (i == 13) or ((i >= 15) and (i <= 18)) or ((i >= 21) and (i <= 24)) or ((i >= 26) and (i <= 28))):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 34.) test AND operation
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input34'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    for i in range(0,nRow):
        Array.append([])
            
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if((i >= 5) and (i <= 30)) :
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if((i >= 2) and (i <= 30)):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 35.) First Input all True; Second Input Increasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input35'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 36.) First Input all True; Second Input Increasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input36'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 37.) First Input all True; Second Input Increasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input37'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 38.) First Input all True; Second Input Increasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input38'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 39.) Second Input all True; First Input Increasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input39'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 40.) Second Input all True; First Input Increasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input40'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 41.) Second Input all True; First Input Increasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input41'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 42.) Second Input all True; First Input Increasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input42'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 1
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter * 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 43.) First Input all True; Second Input Decreasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input43'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 44.) First Input all True; Second Input Decreasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input44'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(1)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 45.) First Input all True; Second Input Decreasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input45'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 46.) First Input all True; Second Input Decreasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input46'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                Array[i].append(0)
            # The second input
            elif(j == 1):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 47.) Second Input all True; First Input Decreasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input47'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 48.) Second Input all True; First Input Decreasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input48'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 49.) Second Input all True; First Input Decreasing Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input49'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 50.) Second Input all True; First Input Decreasing Inverse Pulse
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input50'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 16) or (i == 24)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(flip):
                    Array[i].append(0)
                else:
                    Array[i].append(1)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 51.) 
    #------------------------------------------------------------------------------------#
    # Create the file
    filename = 'input51'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
        # Toggle the input
        if(np.mod(i,counter) == 0):
            flip = not flip
        # Double the counter at these times
        if((i == 4) or (i == 12)):
            counter = counter / 2
        
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if(i == 0):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                Array[i].append(1)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()
    #------------------------------------------------------------------------------------#
    # 52.) Pei Test Input
    #------------------------------------------------------------------------------------#
    # Create the file
    #filename = 'tacas'
    #nRow = 39
    filename = 'input52'
    f = open(__InputDir__ + filename + '.csv','wb')
    Array = []
    flip = True
    counter = 4
    for i in range(0,nRow):
        Array.append([])
       
        for j in range(0,nCol):
            # The first input
            if(j == 0):
                if((i >= 10) and (i <= 24) or (i >= 31)):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            # The second input
            elif(j == 1):
                if(((i >= 3) and (i <= 10)) or (i == 13) or ((i >= 15) and (i <= 18)) or ((i >= 21) and (i <= 24)) or ((i >= 26) and (i <= 28)) or (i >= 31)):
                    Array[i].append(1)
                else:
                    Array[i].append(0)
            else:
                Array[i].append(1)

    # Save the array to a .csv file
    np.savetxt(f,Array,fmt="%d",delimiter=",")
    f.close()

    #------------------------------------------------------------------------------------#
    # 53.) Pei Test Input
    #------------------------------------------------------------------------------------#
    # Create the file
    #nRow = 31
    filename = 'input53'
    f = open(__InputDir__ + filename + '.csv','wb')
    mat = np.random.randint(2,size=(nRow,nCol))
    np.savetxt(f,mat,fmt="%d",delimiter=",")
    f.close()

#------------------------------------------------------------------------------------#
# Main function call
#------------------------------------------------------------------------------------#
# If there are no arguements
if len(sys.argv) == 1:
    print("ERROR: Missing input arguement")
    print("Use '-h' flag for more information")
    exit()

# See if inputFiles directory exists; if not make, items
__AbsolutePath__ = os.path.dirname(os.path.abspath(__file__))+'/'

if(not os.path.isdir(__InputDir__)):
    os.mkdir(__InputDir__)

# for removing the formula files
if(sys.argv[1] == '-r'):
    shutil.rmtree(__InputDir__)
            
# for generating the formula files
elif(sys.argv[1] == '-m'):
    makeInputs()
    print('Inputs are located in the '+__InputDir__+' directory')
 
else:
    print("Invalid input arguement")
    print("-m to make the formula files")
    print("-r to remove them")  
