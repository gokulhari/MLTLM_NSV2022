// Author: Zach Lewis (zlewis@iastate.edu)

#ifndef OPERATOR_QUEUE_H
#define OPERATOR_QUEUE_H

#include <vector>
#include <optional>
#include <memory>
#include "ClassUtil.hpp"
#include "ClassLib.hpp"

using namespace std;

class OperatorQueue {

    public:
        vector<shared_ptr<ClassLib>> queue;
        OperatorQueue();
        bool empty(int index);
        bool exists(int index);
        shared_ptr<ClassLib> get(int index);
        void add(shared_ptr<ClassLib> item);
        int size();
        void incTime(int t);
        void run(FILE * file);
};

#endif /* OPERATOR_QUEUE_H */ 