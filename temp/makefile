
mltlm2mltl:
	g++ -Wall -g -std=C++11 mltlm2mltl.cpp -o mltlm2mltl 

format:
	clang-format -i includes/*.hpp examples/*.cpp test/*.cpp paper/paper1/src/*.cpp -style='{BasedOnStyle: llvm, Standard: Cpp11}'

antlr: 
	antlr4 -Dlanguage=Cpp MLTLM.g4