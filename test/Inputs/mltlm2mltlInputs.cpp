#include <Eigen/Eigen>
#include <fstream>
#include <iostream>
#include <math.h>
using namespace std;
using namespace Eigen;
typedef Matrix<int, Dynamic, Dynamic> MatI;
typedef Matrix<double, Dynamic, Dynamic> MatD;
const static Eigen::IOFormat CSVFormat(Eigen::StreamPrecision, DontAlignCols,
                                       ", ", "\n");

int main() {
  ifstream f("../inputMLTLM.csv");
  string line;
  int N = 0;
  while (getline(f, line)) {
    N++;
  }
  f.close();
  f.open("../inputMLTLM.csv");
  N1 = N /24;
  MatI I1(N,4);
  for (int i = 0; i < N1;i++){
      getline(f,line);
      
      I1()
  }
  return 0;
}