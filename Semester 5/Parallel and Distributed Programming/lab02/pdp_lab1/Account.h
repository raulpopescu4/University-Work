#pragma once

#include "OperationsLog.h"

class Account
{
private:
	OperationsLog log;
	int balance;

public:
	Account(const OperationsLog& log);
	Account();
	~Account();
	const int getBalance();
	void setBalance(const int& balance);
};

