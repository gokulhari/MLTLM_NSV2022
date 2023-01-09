// Author: Zach Lewis (zlewis@iastate.edu)

#include "BinParser.hpp"
#include "ClassLib.hpp"
#include "OperatorQueue.hpp"
#include <string>
#include <fstream>
#include <memory>
#include <iostream>

using namespace std;

const int OP_START		    = 0b01011;
const int OP_END			= 0b01100;
const int OP_END_SEQUENCE	= 0b11111;
const int OP_NOP			= 0b11110;
const int OP_NOT			= 0b00011;

const int OP_AND			= 0b00100;
const int OP_IMPL			= 0b00110;

const int OP_FT_NOT		    = 0b10100;
const int OP_FT_AND		    = 0b10101;
const int OP_FT_IMPL		= 0b11011;

const int OP_OR			    = 0b00101;
const int OP_EQUIVALENT	    = 0b00111;

// past time operations
const int OP_PT_Y			= 0b01000;
const int OP_PT_O			= 0b01001;
const int OP_PT_H			= 0b01010;
const int OP_PT_S			= 0b01110;

// metric past and future time operations
// intervals
const int OP_PT_HJ		    = 0b10010;
const int OP_PT_OJ		    = 0b10000;
const int OP_PT_SJ		    = 0b10011;

const int OP_FT_GJ		    = 0b10111;
const int OP_FT_FJ		    = 0b11001;
const int OP_FT_UJ		    = 0b11010;
const int OP_FT_LOD		    = 0b11100;

// metric past and future time operations
// end time points
const int OP_PT_HT		    = 0b10001;
const int OP_PT_OT		    = 0b01111;

const int OP_FT_GT		    = 0b10110;
const int OP_FT_FT		    = 0b11000;


const int DIRECT 		    = 0b01;
const int ATOMIC 		    = 0b00;
const int SUBFORMULA 	    = 0b10;
const int NOT_SET 	        = 0b11;

void BinParser::parseOperator(string filename)
{
    string line;

    ifstream file;
    file.open(filename);

    if(file.is_open())
    {
        while(getline(file, line))
        {
            // Get opcode to determine what object to construct
            int opcode = stoi(line.substr(0,5), nullptr, 2);

            // get type and value for input 1
            int op1type = stoi(line.substr(5,2), nullptr, 2);
            int op1value = stoi(line.substr(7,8), nullptr, 2);

            // get type and value for input 2
            int op2type = stoi(line.substr(15,2), nullptr, 2);
            int op2value = stoi(line.substr(17,8), nullptr, 2);

            // get code referring to line from interval file (if applicable)
            int interval = stoi(line.substr(25,8), nullptr, 2);

            shared_ptr<vector<TimeStep>> value1, value2;
            int lowerbound, upperbound;

            switch(opcode)
            {
                // Atomic Value
                case OP_FT_LOD: 
                    // Gets applicable atomic list vector and creates and ATOM object
                    opQueue->add(make_shared<ATOM>(ATOM(atomic_list->at(op1value))));
                    break;

                // AND Operator
                case OP_AND:
                    value1 = opQueue->get(op1value)->getOutput();
                    value2 = opQueue->get(op2value)->getOutput();
                    opQueue->add(make_shared<AND>(AND(value1, value2)));
                    break;

                // NOT Operator
                case OP_NOT:
                    value1 = opQueue->get(op1value)->getOutput();
                    opQueue->add(make_shared<NOT>(NOT(value1)));
                    break;

                // UNTIL Operator (Future Time)
                case OP_FT_UJ:
                    value1 = opQueue->get(op1value)->getOutput();
                    value2 = opQueue->get(op2value)->getOutput();
                    lowerbound = intervalList.at(0).at(interval);
                    upperbound = intervalList.at(1).at(interval);
                    opQueue->add(make_shared<UNTIL>(UNTIL(value1, value2, lowerbound, upperbound)));
                    break;

                // GLOBAL Operator (Future Time)
                case OP_FT_GJ:
                    value1 = opQueue->get(op1value)->getOutput();
                    lowerbound = intervalList.at(0).at(interval);
                    upperbound = intervalList.at(1).at(interval);
                    opQueue->add(make_shared<GLOBAL>(GLOBAL(value1, lowerbound, upperbound)));
                    break;

                // START Operator (No usage in C++ version)
                case OP_START:
                    break;

                // END Operator (No usage in C++ version)
                case OP_END:
                    break;
            }

        }

        file.close();
    }

}

shared_ptr<OperatorQueue> BinParser::getOperators()
{
    return opQueue;
}

BinParser::BinParser(shared_ptr<vector<shared_ptr<vector<TimeStep>>>> _atomic_list, shared_ptr<OperatorQueue> _opQueue, vector<vector<int>> _intervalList):atomic_list(_atomic_list),opQueue(_opQueue),intervalList(_intervalList)
{};