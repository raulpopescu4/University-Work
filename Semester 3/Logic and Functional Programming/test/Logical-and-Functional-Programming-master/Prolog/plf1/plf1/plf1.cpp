// plf1.cpp : This file contains the 'main' function. Program execution begins and ends there.
#pragma once

#include <iostream>
#include "lista.h"

bool search(Lista list, TElem elem)
{
	if (check_empty(list))
		return false;
	if (first_elem(list) == elem)
		return true;
	return search(list_from_second(list), elem);
}

Lista list_to_set(Lista list)
{
	if (check_empty(list))
		return void_list();
	TElem elem = first_elem(list);
	if (!search(list_from_second(list), elem))
	{
		return add_first(list_to_set(list_from_second(list)),elem);
	}
	return list_to_set(list_from_second(list));
}

Lista copy(Lista list)
{
	if (check_empty(list))
		return void_list();
	return add_first(copy(list_from_second(list)),first_elem(list));
}

Lista union_with_second_set(Lista b, Lista res)
{
	if (check_empty(b))
		return void_list();
	TElem elem = first_elem(b);
	if (!search(list_from_second(res), elem))
	{
		return add_first(union_with_second_set(list_from_second(b),res), elem);
	}
	return union_with_second_set(list_from_second(b), res);
}

Lista union_two_sets(Lista a, Lista b)
{
	Lista res = void_list();
	res = copy(a);
	Lista res2 = void_list();
	res2 = union_with_second_set(b, res);
	concatenate(res, res2);
	return res;
}
int main()
{
	/*Lista testList;
	testList = creare();
	Lista set = void_list();
	set = list_to_set(testList);
	tipar(set);*/
	Lista a, b, res;
	a = creare();
	b = creare();
	res = void_list();
	res = union_two_sets(a,b);
	tipar(res);
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
