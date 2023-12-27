#include "lista.h"
#include <iostream>

using namespace std;


PNod creare_rec() {
	TElem x;
	cout << "x=";
	cin >> x;
	if (x == 0)
		return NULL;
	else {
		PNod p = new Nod();
		p->e = x;
		p->urm = creare_rec();
		return p;
	}
}

Lista creare() {
	Lista l;
	l._prim = creare_rec();
	return l;
}

void tipar_rec(PNod p) {
	if (p != NULL) {
		cout << p->e << " ";
		tipar_rec(p->urm);
	}
}

void tipar(Lista l) {
	tipar_rec(l._prim);
}

void distrug_rec(PNod p) {
	if (p != NULL) {
		distrug_rec(p->urm);
		delete p;
	}
}

void distrug(Lista l) {
	//se elibereaza memoria alocata nodurilor listei
	distrug_rec(l._prim);
}

TElem first_elem(Lista l)
{
	return l._prim->e;
}

bool check_empty(Lista l)
{
	return l._prim==NULL;
}

Lista list_from_second(Lista l)
{
	Lista newList;
	newList._prim = l._prim->urm;
	return newList;
}

Lista void_list()
{
	Lista l;
	l._prim = NULL;
	return l;
}

Lista add_first(Lista l, TElem el)
{
	PNod nod = new Nod();
	nod->e = el;
	nod->urm = l._prim;
	l._prim = nod;
	return l;
}

PNod getLast(Lista l)
{
	if (l._prim->urm == NULL)
		return l._prim;
	return getLast(list_from_second(l));
}

void concatenate(Lista l1, Lista l2)
{
	PNod last = getLast(l1);
	last->urm = l2._prim;
}

