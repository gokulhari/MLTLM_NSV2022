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

MatI Neg(MatI R) {
  MatI out(R.rows(), 1);
  for (int i = 0; i < R.rows(); i++) {
    out(i, 0) = (R(i, 0) == 0) ? 1 : 0;
  }
  return out;
}

MatI Until(MatI L, MatI R, int lb, int ub) {
  MatI out(L.rows() - ub, 1);

  for (int i = 0; i < L.rows() - ub; i++) {
    out(i, 0) = 0;
    for (int j = i + lb; j <= i + ub; j++) {
      if (R(j, 0) == 1) {
        bool y = true;
        for (int k = i + lb; k < j; k++) {
          y = y && L(k, 0);
        }
        if (y) {
          out(i, 0) = 1;
          break;
        }
      }
    }
  }
  return out;
}

MatI And(MatI L, MatI R) {
  MatI out(R.rows(), 1);
  for (int i = 0; i < R.rows(); i++) {
    out(i, 0) = (R(i, 0) == 1 && L(i, 0) == 1) ? 1 : 0;
  }
  return out;
}

MatI Or(MatI L, MatI R) { return Neg(And(Neg(L), Neg(R))); }

MatI Future(MatI R, int lb, int ub) {
  MatI temp = MatI::Ones(R.rows(), 1);
  return Until(temp, R, lb, ub);
}

MatI Global(MatI R, int lb, int ub) { return Neg(Future(Neg(R), lb, ub)); }

MatI Modred(MatI R, int stride) { return R(seq(0, last, stride), 0); }

int main() {
  int N = 100;
  MatI I1(N, 4), I2(3 * N, 3), I3(8 * N, 2), I4(12 * N, 1);
  MatD D1(N, 4), D2(3 * N, 3), D3(8 * N, 2), D4(12 * N, 1);
  D1 = floor(1.0 + MatD::Random(N, 4).array());
  I1 = D1.cast<int>();
  D2 = floor(1.0 + MatD::Random(3 * N, 3).array());
  I2 = D2.cast<int>();
  D3 = floor(1.0 + MatD::Random(8 * N, 2).array());
  I3 = D3.cast<int>();
  D4 = floor(1.0 + MatD::Random(12 * N, 1).array());
  I4 = D4.cast<int>();

  ofstream f("../input1MLTLM.csv");
  f << I1.format(CSVFormat) << "\n";
  f << I2.format(CSVFormat) << "\n";
  f << I3.format(CSVFormat) << "\n";
  f << I4.format(CSVFormat) << "\n";

  f.close();
  f.open("../input1MLTL.csv");

  MatI K4(N, 1), K3(4 * N, 1), K2(12 * N, 1), K1(24 * N, 1);
  K4 << I1(all, last);
  K3 << I1(all, last - 1), I2(all, last);
  K2 << I1(all, last - 2), I2(all, last - 1), I3(all, last);
  K1 << I1(all, last - 3), I2(all, last - 2), I3(all, last - 1), I4(all, last);

  MatI K(24 * N, 4);

  K(all, 0) = K1;
  for (int i = 0; i < 24 * N; i++) {
    K(i, 1) = K2(i / 2, 0);
    K(i, 2) = K3(i / 6, 0);
    K(i, 3) = K4(i / 24, 0);
  }
  f << K.format(CSVFormat) << "\n";
  f.close();

  MatI C_tr = K3(seq(0, last, 4), 0);
  MatI B_tr = K2(seq(0, last, 12), 0);
  MatI D_tr_r(100, 1);

  for (int i = 0; i < 100; i++) {
    if (C_tr(i, 0) || B_tr(i, 0)) {
      D_tr_r(i, 0) = 1;
    } else {
      D_tr_r(i, 0) = 0;
    }
  }

  cout << "The norm:) " << (D_tr_r - Or(C_tr, B_tr)).norm() << endl;

  MatI D_tr_l = K1(seq(0, last, 24), 0);
  //  MatI F = Until(D_tr_l, D_tr_r, 4, 6);
//G[0,1,c](G[1,2,a](a0) & G[1,2,b](a1));
  MatI F =   Global(And( Modred(Global(K2,1,2),3), Modred(Global(K1,1,2),6) ),0,1);

  cout << "F : \n";
  cout << F << endl;
  f.open("tracer.txt");
  f << F << endl;
  f.close();

  return 0;
}