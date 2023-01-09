// Author: Zach Lewis (zlewis@iastate.edu)

#include "OperatorQueue.hpp"
#include "ClassLib.hpp"
#include <optional>
#include <memory>

using namespace std;

OperatorQueue::OperatorQueue()
{
    queue = {};
};

bool OperatorQueue::empty(int index){
    if (index >= queue.size()) {
        return true;
    }
    else {
        return false;
    }
}

void OperatorQueue::add(shared_ptr<ClassLib> item){
    queue.push_back(item);
}

shared_ptr<ClassLib> OperatorQueue::get(int index)
{
    return queue.at(index);
}

int OperatorQueue::size()
{
    return queue.size();
}

void OperatorQueue::incTime(int t)
{
    for(int i = 0; i < queue.size(); i++)
    {
        queue[i]->time = t;
    }
}

void OperatorQueue::run(FILE * file)
{
    for(int i = 0; i < queue.size(); i++)
    {
        queue[i]->run(file);
    }
}