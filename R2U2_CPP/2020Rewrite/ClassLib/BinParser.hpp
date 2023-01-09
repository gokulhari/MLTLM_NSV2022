// Author: Zach Lewis (zlewis@iastate.edu)

#ifndef BIN_PARSER_H
#define BIN_PARSER_H

#include "OperatorQueue.hpp"
#include "ClassUtil.hpp"
#include <vector>
#include <memory>

class BinParser {

	private:
		shared_ptr<vector<shared_ptr<vector<TimeStep>>>> atomic_list;
		shared_ptr<OperatorQueue> opQueue;
		vector<vector<int>> intervalList;
	
	public:
		BinParser(shared_ptr<vector<shared_ptr<vector<TimeStep>>>> _atomic_list, shared_ptr<OperatorQueue> _opQueue, vector<vector<int>> _intervalList);
		void parseOperator(string filename);
		shared_ptr<OperatorQueue> getOperators();

};


#endif




