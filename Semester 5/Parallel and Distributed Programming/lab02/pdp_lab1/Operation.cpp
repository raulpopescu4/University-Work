#include "Operation.h"

Operation::Operation()
{
	serial_number = global_operation_serial_number;
	global_operation_serial_number++;
}

Operation::~Operation()
{
	{}
}

const int& Operation::getSerialNumber()
{
	return this->serial_number;
}




