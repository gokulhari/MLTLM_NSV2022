#ifndef COMMON_H_
#define COMMON_H_

#include <string>
using namespace std;
typedef	struct{
	bool verdict;
	int time_stamp;
}Evaluation;

typedef struct{
	int rdPtr_mem;
	int rdPtr2_mem;
	Evaluation result_mem;
}MemoryPtrs;

#endif
