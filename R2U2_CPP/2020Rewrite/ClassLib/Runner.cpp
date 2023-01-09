// Author: Zach Lewis (zlewis@iastate.edu)

#include "ClassLib.hpp"
#include "ClassUtil.hpp"
#include "TimestepReader.hpp"
#include "OperatorQueue.hpp"
#include "BinParser.hpp"
#include <iostream>
#include <stdio.h>
#include <list>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

int main(int argc, char* argv[])
{
    // Opens an output file
    FILE * file = fopen("output.txt", "w");

    if(true) 
    {

        string line;
        stringstream sstream;
        // Reads the inputs from atomic.csv
        ifstream atomic_file ("atomic.csv");

        // This contains a 2D matrix of timestep pointers, 
        // called atomic_list
        shared_ptr<vector<shared_ptr<vector<TimeStep>>>> atomic_list(new vector<shared_ptr<vector<TimeStep>>>{});

        if(atomic_file.is_open())
        {
            int time = 1;
            // gets the first line in the atomic_file
            getline(atomic_file, line);            

            sstream.str(line);
            while(sstream.good())
            {
                string substr;
                getline(sstream, substr, ',');
                int value = stoi(substr);
                TimeStep current;
                if(value==1)
                {
                    current = {true, time};
                }
                else
                {
                    current = {false, time};
                }
                atomic_list->push_back(make_shared<vector<TimeStep>>(vector<TimeStep>{current}));
            }

            time++;

            while(getline(atomic_file, line))
            {
                sstream.str(line);
                sstream.clear();
                int counter = 0;

                while(sstream.good())
                {
                    string substr;
                    getline(sstream, substr, ',');
                    int value = stoi(substr);
                    TimeStep current;
                    if(value == 1)
                    {
                        current = {true, time};
                    }
                    else
                    {
                        current = {false, time};
                    }
                    atomic_list->at(counter)->push_back(current);

                    counter++;
                }
                time++;
            }
        }

        shared_ptr<OperatorQueue> operptr(new OperatorQueue());
        
        // The first {1,3,4} refer to lower bounds, and the 
        // second {3,5,8} refer to upper bounds.
        vector<vector<int>> intervalList = {{1,3,4}, {3,5,8}};

        // Takes input atomic_list, operptr and intervalList.
        BinParser parser (atomic_list, operptr, intervalList);

        parser.parseOperator("op.txt");
        

        if(file == NULL)
        {
            cout << "Problem opening file" << endl;
        }
        else
        {
            for(int t = 1; t <= 10; t++){

                fprintf(file, "--- Time: %d ---\n", t);
                
                operptr->incTime(t);
                operptr->run(file);

                fprintf(file, "\n");
            }
        }

    }
    else
    {
        cout << "Not enough arguments" << endl;
    }

    fclose(file);

    return 0;
};
