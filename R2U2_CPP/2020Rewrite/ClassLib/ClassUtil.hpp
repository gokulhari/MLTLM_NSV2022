//Authored by: Meaghan McCleary (mlmccle3@gmail.com)

#ifndef CLASS_UTIL
#define CLASS_UTIL

#include <string>
using namespace std;


struct TimeStep {
	bool verdict;
	int time_stamp;
}; //figure out a better name






	
// 	//dummy function; current version relies on queue
	
// }
// current version: makes sure there's stuff in queue to reason over
// bool CircularBuffer::isEmpty(int& rd_ptr, int desired_time_stamp) {
// 	if(rd_ptr==wr_ptr && queue[rd_ptr].time_stamp>=desired_time_stamp) return false;
// 	while(rd_ptr!=wr_ptr && queue[rd_ptr].time_stamp<desired_time_stamp) rd_ptr=inc_ptr(rd_ptr);
// 	if(rd_ptr==wr_ptr) {
// 		rd_ptr = dec_ptr(rd_ptr);
// 		return true;
// 	}
// 	return false;
// }


//program counter: should come form assm file at the moment (I think). Skipping 
//for now

#endif

