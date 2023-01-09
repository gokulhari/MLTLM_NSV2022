// Author: Zach Lewis (zlewis@iastate.edu)

#include "ClassUtil.hpp"
#include "TimestepReader.hpp"
#include <vector>
#include <optional>
#include <memory>

using namespace std;

TimestepReader::TimestepReader():current(0){
    timestepQueue = {};
};

TimestepReader::TimestepReader(shared_ptr<vector<TimeStep>> _timestepQueue):current(0),timestepQueue(_timestepQueue)
{};

bool TimestepReader::isEmpty()
{
    if(current >= timestepQueue->size())
    {
        return true;
    } 
    else
    {
        return false;
    }
};

int TimestepReader::size()
{
    return timestepQueue->size();
}

optional<TimeStep> TimestepReader::next()
{
    if(isEmpty())
    {
        return nullopt;
    }
    else
    {
        return timestepQueue->at(current);
    }
};

optional<TimeStep> TimestepReader::get(int index)
{
    if(index >= timestepQueue->size())
    {
        return nullopt;
    }
    else
    {
        return timestepQueue->at(index);
    }
};

optional<TimeStep> TimestepReader::getCurrent()
{
    return get(current);
}

void TimestepReader::setCounter(int index)
{
    current = index;
};

void TimestepReader::inc(int desiredTimestep)
{
    while(!isEmpty() && getCurrent().value().time_stamp < desiredTimestep)
    {
        current++;
    }
};