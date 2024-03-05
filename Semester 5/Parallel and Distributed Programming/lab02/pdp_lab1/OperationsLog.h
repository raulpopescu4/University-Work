#pragma once

#include "Operation.h"
#include <vector>

class OperationsLog
{
private:
	std::vector<Operation> log;
public:
	const std::vector<Operation> getOperationsLog();
	OperationsLog();
	~OperationsLog();
	void addOperation(const Operation& operation);
	void deleteOperation(const Operation& operation);

};

