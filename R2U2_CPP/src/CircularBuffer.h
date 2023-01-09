/*
 * CircularBuffer.h
 *
 *  Created on: Jul 25, 2017
 *      Author: PEI
 */
#ifndef SRC_CIRCULARBUFFER_H_
#define SRC_CIRCULARBUFFER_H_

#define circularQueue_size 32
#include "common.h"
#include <vector>

class CircularBuffer {
public:
	//CircularBuffer(int size);
	CircularBuffer(int size_);

	int inc_ptr(int ptr);
	int dec_ptr(int ptr);
	void add(Evaluation newData);
	Evaluation pop(int rd_ptr);
	bool isEmpty(int& rd_ptr, int desired_time_stamp);

private:
	std::vector<Evaluation> queue; //dynamically allocated queue
	int size;
	int wr_ptr=0;
};


#endif /* SRC_CIRCULARBUFFER_H_ */
