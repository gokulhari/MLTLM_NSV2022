#include <iostream>

using namespace std;

int main() {
  const int has_nukes = 1 << 0;
  const int has_bio_weapons = 1 << 1;
  const int has_chem_weapons = 1 << 2;
  cout << has_nukes << endl;
  cout << has_bio_weapons << endl;
  cout << has_chem_weapons << endl;
}