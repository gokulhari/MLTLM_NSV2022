//Authored by: Meaghan McCleary (mlmccle3@gmail.com), Zach Lewis (zlewis@iastate.edu)

//Included Libraries

#ifndef CLASS_LIB
#define CLASS_LIB

#include <vector>
#include <iostream>
#include <stdio.h>
#include <list>
#include <fstream>
#include <sstream>
#include <string>
#include <string.h>
#include <cstring>
#include <optional>
#include "ClassUtil.hpp" //imports dummy utilities
#include "TimestepReader.hpp"

using namespace std;

class ClassLib{ //template class for operators
public:
	virtual void run(FILE *pFile){};

	void dprint(FILE* pFile, string op, bool isbin, int pc, TimeStep result){ //prints stuff to results file
		char verdictString[6];
		if(result.verdict == true){
			strcpy(verdictString, "true ");
		}
		else
		{
			strcpy(verdictString, "false");
		}
		if (!isbin) { //tests condition to determine which version to use
			fprintf(pFile, "PC: %d %s = [%d %s] \n", pc, op.c_str(), result.time_stamp, verdictString); //Args: program counter, operator
			//text, time stamp of result, verdict of result
		}
		else{
			fprintf(pFile, "PC: %d %s[tau1, tau2] = [%d %s] \n", pc, op.c_str(), result.time_stamp, verdictString);
		}
	};

	shared_ptr<vector<TimeStep>> getOutput()
	{
		return outputTimestep;
	};

	ClassLib(){};
	ClassLib(shared_ptr<vector<TimeStep>> input1, string operation, bool bin) : op(operation), isbin(bin), desiredTimestamp(0)
	{
		inputReader1 = TimestepReader(input1);
	};
	ClassLib(shared_ptr<vector<TimeStep>> input1, shared_ptr<vector<TimeStep>> input2, string operation, bool bin) : op(operation), isbin(bin), desiredTimestamp(0)
	{
		inputReader1 = TimestepReader(input1);
		inputReader2 = TimestepReader(input2);
	};
	~ClassLib(){}; //constructor


	int time = 1;
	int desiredTimestamp;
	string op; //keyword to print in dprint function, eg AND, NOT, etc
	bool isbin; //designation for print function selection
	optional<TimeStep> result; //results variable (time step and verdict)
	int pc;
	TimestepReader inputReader1;
	TimestepReader inputReader2;
	shared_ptr<vector<TimeStep>> outputTimestep = make_shared<vector<TimeStep>>();
};

class ATOM: public ClassLib{
	public:
		~ATOM(){};
		ATOM(shared_ptr<vector<TimeStep>> inputTimestep) : ClassLib(inputTimestep, "ATOM", false) {};

		void run(FILE *pFile){
			
			if(!inputReader1.isEmpty())
			{
				TimeStep A = inputReader1.getCurrent().value();
				if(time == A.time_stamp)
				{
					result = {A.verdict, A.time_stamp};
					outputTimestep->push_back(result.value());
					dprint(pFile, op, isbin, pc, result.value());
				}
				inputReader1.inc(time+1);
			}
		};
};

class AND: public ClassLib{
public: 
	~AND(){};
	AND(shared_ptr<vector<TimeStep>> input1, shared_ptr<vector<TimeStep>> input2) : ClassLib(input1, input2, "AND", false) {}

	int tmin = -1;

	void run(FILE *pFile){

		TimeStep A, B;

		while(!inputReader1.isEmpty() || !inputReader2.isEmpty())
		{
			result = nullopt;

			if (!inputReader1.isEmpty() && !inputReader2.isEmpty())
			{
				A = inputReader1.getCurrent().value();
				B = inputReader2.getCurrent().value();

				if (A.verdict && B.verdict)
				{
					tmin = min(A.time_stamp, B.time_stamp);
					result = {true, tmin};
				}
				else if (!A.verdict && !B.verdict)
				{
					tmin = max(A.time_stamp, B.time_stamp);
					result = {false, tmin};
				}
				else if (!A.verdict)
				{
					tmin = A.time_stamp;
					result = {false, tmin};
				}
				else if (!B.verdict)
				{
					tmin = B.time_stamp;
					result = {false, tmin};
				}
			}
			else if (inputReader1.isEmpty())
			{
				B = inputReader2.getCurrent().value();

				if (!B.verdict)
				{
					result = {false, B.time_stamp};
				}
			}
			else 
			{
				A = inputReader1.getCurrent().value();

				if(!A.verdict)
				{
					result = {false, A.time_stamp};
				}
			}

			if(result.has_value())
			{
				outputTimestep->push_back(result.value());
				dprint(pFile,op,isbin,pc,result.value());
				desiredTimestamp = result.value().time_stamp + 1;
			} else break;

			inputReader1.inc(desiredTimestamp);
			inputReader2.inc(desiredTimestamp);
		}
	};
};

class UNTIL: public ClassLib{ //formed based on Until algorithm
public:
	int tmin, tout, tdow, tpre, lb, ub;
	TimeStep last;

	~UNTIL(){};
	UNTIL(shared_ptr<vector<TimeStep>> input1, shared_ptr<vector<TimeStep>> input2, int lowerbound, int upperbound) : ClassLib(input1, input2, "U", true), lb(lowerbound), ub(upperbound) {
		tmin = -1;
		tout = 0;
		tdow = 0;
		tpre = 0;
		last = {false, -1};
	}

	void run(FILE *pFile){

		while(!inputReader1.isEmpty() && !inputReader2.isEmpty())
		{
			TimeStep A = inputReader1.getCurrent().value();
			TimeStep B = inputReader2.getCurrent().value();

			tmin = min(A.time_stamp, B.time_stamp);
			desiredTimestamp = tmin + 1;

			if (B.verdict == false && last.verdict == true){
				tdow = tpre + 1;
			}

			tpre = B.time_stamp;

			if (B.verdict == true){
				result = {true,tmin-lb};
			}
			else if (A.verdict == false) {
				result = {false,tmin-lb};
			}
			else if (tmin >= ((ub-lb) + tdow)){
				result = {false,tmin-ub};
			}
			if(result.has_value())
			{
				if (result.value().time_stamp >= tout){
					tout = result.value().time_stamp + 1;
					dprint(pFile,op,isbin,pc,result.value());
					outputTimestep->push_back(result.value());
				}
			}

			last = B;

			inputReader1.inc(desiredTimestamp);
			inputReader2.inc(desiredTimestamp);
		}

	}

};

class NOT: public ClassLib{
public:
	NOT(shared_ptr<vector<TimeStep>> input1) : ClassLib(input1, "NOT", false) {}

	int tmin = -1;

	void run(FILE *pFile){
		cout << "yes" << endl;
		while(!inputReader1.isEmpty())
		{
			
			TimeStep A = inputReader1.getCurrent().value();
			if (A.time_stamp > tmin)
			{
				tmin = A.time_stamp;
				result = {!A.verdict, A.time_stamp};
				outputTimestep->push_back(result.value());

				dprint(pFile, op, isbin, pc, result.value());
			}

			inputReader1.inc(tmin+1);
		}
		
	};

};

class GLOBAL: public ClassLib{
public:
	int lb, ub, tmin, mup;
	TimeStep last;

	~GLOBAL(){};
	GLOBAL(shared_ptr<vector<TimeStep>> input1, int lowerbound, int upperbound) : ClassLib(input1, "G", true), lb(lowerbound), ub(upperbound)
	{	
		tmin = -1;
		mup = 0;
		last = {false, -1};
	}

	void run(FILE *pFile){

		while(!inputReader1.isEmpty())
		{
			TimeStep A = inputReader1.getCurrent().value();

			if (A.verdict == true && last.verdict == false)
			{
				mup = last.time_stamp + 1;
			}

			//tmin = A.time_stamp;

			if (A.verdict == true && A.time_stamp >= max((ub-lb)+mup,ub))
			{
				result = {true,A.time_stamp-ub};
				outputTimestep->push_back(result.value());
				dprint(pFile,op,isbin,pc,result.value());
			}
			else if (A.time_stamp >= lb){
				result = {false,A.time_stamp-lb};
				outputTimestep->push_back(result.value());
				dprint(pFile,op,isbin,pc,result.value());
			}

			last = A;

			desiredTimestamp = A.time_stamp + 1;

			inputReader1.inc(desiredTimestamp);
		}

	}
};

// class END: public ClassLib{
// public:
// 	~END(){};
// 	END() : ClassLib()
// 	{
// 		isbin = false;
// 		op = "END";
// 	}

// 	void run(FILE *pFile){
// 		// bool empty = empty(i);
// 		// while(!empty){
// 		// 	dprint(pFile,op,isbin,pc,result);
// 		// 	i = i + 1;
// 		// 	//empty = ClassUtil.Empty(i);
// 		// }
// 	}

// };
#endif
