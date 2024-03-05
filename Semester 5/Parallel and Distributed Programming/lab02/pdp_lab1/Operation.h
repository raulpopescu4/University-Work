#pragma once
#include <string>


class Operation
{
private:
	int serial_number;
	Account sender;
	Account receiver;
	int amount;

public:
	Operation();
	~Operation();
	const int& getSerialNumber();

};

