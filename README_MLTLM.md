# MLTLM extension in R2U2

Compile R2U2 normally according to [README.md](README.md).

The translators are located in mltlm2mltl/Python/

The translators use [Antlr](https://www.antlr.org) to parse MLTLM formulas. You need the runtime Python libraries of Antlr to run them. We have tested this implementation on Linux and Mac platforms with python3.7 and python 3.8. 

Translators 1, 2 and 3 can be invoked using the scripts [main.py](mltlm2mltl/Python/main.py), [main2.py](mltlm2mltl/Python/main2.py), and [main3.py](mltlm2mltl/Python/main3.py) respectively with arguments as either an MLTLM formula, as in, 
```
python3 main3.py "G[0,0,a] a0;"
```
or a file containing MLTLM formulas,
```
python3 main3.py "formulas.mltlm"
``` 
Proof of correctness of the translators is found in [TranslatorProof.md](mltlm2mltl/TranslatorProof.md), which will also give you insight into the proof of the main theorem in the paper.

To directly reproduce the plots in the paper, run the [generatePlots.py](mltlm2mltl/Python/generatePlots.py). This script runs the MLTL monitor for translated MLTL formulas, runs the equivalent MLTLM formulas, and produces the plots. 

You can verify that the translators and the native implementation produce the same verdicts using the script [testTranslators.py](mltlm2mltl/Python/testTranslators.py).

The scripts use the formulas listed in [randomTest5.mltlm](mltlm2mltl/Python/randomTest5.mltlm). As the translated MLTL formulas can take a long time to evaluate, we normally test formulas one at a time. 

You can generate you own random formulas using the script [generateRandomFormulasNewSem.pl](mltlm2mltl/Python/generateRandomFormulasNewSem.pl) and [generateRandomFormulasNewSemProb.pl](mltlm2mltl/Python/generateRandomFormulasNewSemProb.pl), where the former $P = 0.5$ and the latter gives you the freedom to vary $P$, where $P$ is the probability of choosing a temporal operator. 

