# Author: Matt Cauwels
# Date: November 10th, 2020

**genOracle.py** will automatically generate the oracle files for regression testing. The command "python3 genOracle.py -m" will make the files; "python3 genOracle.py -r" will remove them.

**FT_Oracle**: manually handmade oracle files. Readme in directory explains which formulas and input is used. Formulas can be found in the TL_formula/genFormula.py script.

**FT_PT_Oracle**: manually handmade oracle files. Readme in the directory maps formula numbers to the formula. Also explains what the input is.

**LargeFtOracle**: autogenerated oracles for a 10,000 time stamp, randomly generated two-input stream. Formulas can be found in the LargeTestFT_Oracle.xlsx file. Other files were generated from that one and the formulaOracle.py parsing script (parses *.csv files to *.txt).

**LargePtOracle**: autogenerated oracles for a 10,000 time stamp, randomly generated two-input stream. Formulas can be found in the LargeTestPT_Oracle.xlsx file. Other files were generated from that one and the formulaOracle.py parsing script (parses *.csv files to *.txt).