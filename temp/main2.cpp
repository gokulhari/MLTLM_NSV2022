// A translator from MLTLM to MLTL
// Designed specifically for the modulo-reduction function.
// We assume that the base time name is "a".
// Other time names are relative to "a".
//
// Presentation pros:
// How would a user input the projection function?
//
// Gokul Hariharan (gokul@iastate.edu)

#include "MLTLMBaseListener.h"
#include "MLTLMBaseVisitor.h"
#include "MLTLMLexer.h"
#include "MLTLMParser.h"
#include "MLTLMVisitor.h"
#include "MyExpression.h"
#include "MyVisitor.h"
#include "antlr4-runtime.h"
#include <iostream>
#include <sstream>
#include <stack>
#include <streambuf>

using namespace antlrcpp;
using namespace antlr4;
using namespace std;

string moduloReduction(const MyExpression &mye, const string &fromTime) {
  // Now define mapping from a to b, b to c, and c to d
  int a2b = 2;
  int b2c = 3;
  int c2d = 4;
  int a2c = a2b * b2c;
  int a2d = a2b * b2c * c2d;
  int b2d = b2c * c2d;

  string out("(");
  int param;
  if (fromTime == "a" && mye.timeName == "b") {
    param = a2b;
  } else if (fromTime == "b" && mye.timeName == "c") {
    param = b2c;
  } else if (fromTime == "c" && mye.timeName == "d") {
    param = c2d;
  } else if (fromTime == "a" && mye.timeName == "c") {
    param = a2c;
  } else if (fromTime == "a" && mye.timeName == "d") {
    param = a2d;
  } else if (fromTime == "b" && mye.timeName == "d") {
    param = b2d;
  } else {
    cout << "Unknown time conversion" << endl;
    throw "Unknown time conversion \n";
  }

  if (mye.opName == "U") {
    for (int i = param * mye.bounds[0]; i < param * mye.bounds[1] + 1;
         i = i + param) {
      for (int j = param * mye.bounds[0]; j < i; j = j + param) {
        out += "G[" + to_string(j) + "," + to_string(j) + "]" + "(" + mye.left +
               ")" + " & ";
      }

      out += "G[" + to_string(i) + "," + to_string(i) + "]" + "(" + mye.right +
             ")";
      out += ") | (";
    }
    out.pop_back();
    out.pop_back();
    out.pop_back();
    out.pop_back();
    // out += ";\n";
  } else if (mye.opName == "G") {
    for (int i = param * mye.bounds[0]; i < param * mye.bounds[1] + 1;
         i = i + param) {
      out += "G[" + to_string(i) + "," + to_string(i) + "]" + +"(" + mye.right +
             ")";
      out += ") & (";
    }
    out.pop_back();
    out.pop_back();
    out.pop_back();
    out.pop_back();
    // out += ";\n";
  } else if (mye.opName == "F") {
    for (int i = param * mye.bounds[0]; i < param * mye.bounds[1] + 1;
         i = i + param) {
      out += "G[" + to_string(i) + "," + to_string(i) + "]" + "(" + mye.right +
             ")";
      out += ") | (";
    }
    out.pop_back();
    out.pop_back();
    out.pop_back();
    out.pop_back();
    // out += ";\n";
  } else if (mye.opName == "R") {
    MyExpression temp = mye;
    temp.opName = "R";
    temp.left = "!(" + temp.left + ")";
    temp.right = "!(" + temp.right + ")";
    out = "!" + moduloReduction(temp, fromTime);
  } else {
    cout << "Unknown operator." << mye.opName << " \n";
    throw "Unknown operator.\n";
  }
  return out;
};

int main(int argc, char **argv) {
  // std::string s(argv[1]);
  ofstream file;
  ifstream ifile(argv[1]);
  file.open("test.MLTL");
  // moduloReduction()

  std::string s((std::istreambuf_iterator<char>(ifile)),
                std::istreambuf_iterator<char>());
  std::cout << "Input: " << std::endl << s << std::endl;
  ANTLRInputStream input(s);
  MLTLMLexer lexer(&input);
  CommonTokenStream tokens(&lexer);
  tokens.fill();

  MLTLMParser parser(&tokens);
  // tree::ParseTree *tree = parser.program();

  MLTLMParser::ProgramContext *tree = parser.program();
  auto statements = tree->statement();

  MyVisitor vv;
  // Now translate:
  for (auto statement : statements) {
    auto expression = statement->expr();
    vv.visit(expression);

    // for (auto mem : vv.stackedExps) {
    //   cout << "mem: " << mem.opName << ", " << mem.left << ", " << mem.right
    //        << ", " << mem.timeName << ", [";
    //   for (auto bds : mem.bounds) {
    //     cout << bds << ",";
    //   }
    //   cout << "], " << mem.fromTimeName << "\n";
    // }

    // if stackedExps is empty, that means that the
    // statement has no temporal or logical operators, then simply
    // output as is
    string out;
    if (vv.stackedExps.empty()) {
      file << expression->getText();
    } else {
      if (vv.stackedExps[0].timeName == vv.stackedExps[0].fromTimeName) {
        out = vv.stackedExps[0].reconstruct2();
      } else {
        out =
            moduloReduction(vv.stackedExps[0], vv.stackedExps[0].fromTimeName);
      }
      file << out;
    }
    file << ";\n";
    vv.stackedExps.clear();
  }

  file.close();
  ifile.close();
  return 0;
}