// Author: Zach Lewis (zlewis@iastate.edu)

#ifndef TIMESTEP_READER_H
#define TIMESTEP_READER_H

#include "ClassUtil.hpp"
#include <vector>
#include <optional>
#include <memory>

using namespace std;

class TimestepReader {

    private:
        shared_ptr<vector<TimeStep>> timestepQueue;

    public:
        int current;
        TimestepReader();
        TimestepReader(shared_ptr<vector<TimeStep>> _timestepQueue);
        bool isEmpty();
        int size();
        optional<TimeStep> next();
        optional<TimeStep> getCurrent();
        optional<TimeStep> get(int index);
        void setCounter(int index);
        void inc(int desiredTimestep);

};

#endif //TIMESTEP_READER_H