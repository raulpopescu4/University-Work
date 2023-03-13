#pragma once
//DO NOT INCLUDE BAGITERATOR


//DO NOT CHANGE THIS PART
#include <utility>
#include <cstdio>
#include <cmath>

#define NULL_TELEM -111111;
typedef int TElem;
typedef std::pair<TElem, int> Pair;
#define NULL_PAIR pair<int,int> (-111111, -111111)
#define tombstone pair<int,int> (-111111, -11111)

class BagIterator; 
class Bag {

private:
    long int capacity;
    float load_factor;
    Pair* table;
    int table_size;
    int bag_size;

    //DO NOT CHANGE THIS PART
	friend class BagIterator;
public:
	//constructor
	Bag();

	//adds an element to the bag
	void add(TElem e);

	//removes one occurrence of an element from a bag
	//returns true if an element was removed, false otherwise (if e was not part of the bag)
	bool remove(TElem e);

	//checks if an element appears is the bag
	bool search(TElem e) const;

	//returns the number of occurrences for an element in the bag
	int nrOccurrences(TElem e) const;

	//returns the number of elements from the bag
	int size() const;

	//returns an iterator for this bag
	BagIterator iterator() const;

	//checks if the bag is empty
	bool isEmpty() const;

	//destructor
	~Bag();

    int quadratic_function(int elem, int tries) const{
        return int(((abs(elem) % this->capacity) + 0.5*tries + 0.5*tries*tries)) % this->capacity;
    }

};