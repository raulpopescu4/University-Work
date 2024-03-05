#include "Account.h"

Account::Account(const OperationsLog& log)
{
	this->log = log;
}

Account::Account()
{
	{}
}

Account::~Account()
{
	{}
}

const int Account::getBalance()
{
	return this->balance;
}

void Account::setBalance(const int& balance)
{
	this->balance = balance;
}
