#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  if (argc == 1)
    cout << "\n\tHello World\n\n";
  else
    for (size_t i = 1; i < argc; i++)
      cout << "\t" << argv[i] << endl;
  
  return 0;
}
