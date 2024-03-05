#pragma once

#include "Operation.h"
#include <vector>

class OperationsRecord
{
private:
	std::vector<Operation> record;
public:
	const std::vector<Operation> getOperationsRecord();
	OperationsRecord();
	~OperationsRecord();

};

