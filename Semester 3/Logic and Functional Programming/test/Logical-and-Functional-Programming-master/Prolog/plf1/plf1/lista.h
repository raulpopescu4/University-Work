#pragma once
#include "pch.h"

//tip de data generic (pentru moment este intreg)
typedef int TElem;

//referire a structurii Nod;
struct Nod;

//se defineste tipul PNod ca fiind adresa unui Nod
typedef Nod *PNod;

typedef struct Nod {
	TElem e;
	PNod urm;
};

typedef struct {
	//prim este adresa primului Nod din lista
	PNod _prim;
} Lista;

//operatii pe lista - INTERFATA

//crearea unei liste din valori citite pana la 0
Lista creare();
//tiparirea elementelor unei liste
void tipar(Lista l);
// destructorul listei
void distrug(Lista l);

TElem first_elem(Lista l);
bool check_empty(Lista l);
Lista list_from_second(Lista l);
Lista void_list();
Lista add_first(Lista l, TElem el);
PNod getLast(Lista l);
void concatenate(Lista l1, Lista l2);
