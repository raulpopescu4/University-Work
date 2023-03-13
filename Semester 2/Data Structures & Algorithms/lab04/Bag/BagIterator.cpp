#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c)
{
	this->iteration_array = new Pair[bag.bag_size];
    Pair new_element;
    int j = 0, count;
    for(int i = 0; i < c.capacity; ++i){
        if(bag.table[i] != NULL_PAIR){
            count = 0;
            while(count < bag.table[i].second){
                new_element.first = bag.table[i].first;
                new_element.second = count + 1;
                this->iteration_array[j] = new_element;
                j++;
                count++;
            }
        }

    }
    this->position = 0;
}


void BagIterator::first() {
	this->position = 0;
}


void BagIterator::next() {
	if(!this->valid())
        throw std::exception();
    this->position++;
}


bool BagIterator::valid() const {
	if(this->position == bag.bag_size)
	    return false;
    return true;
}



TElem BagIterator::getCurrent() const
{
    if(!this->valid())
        throw std::exception();
	return this->iteration_array[this->position].first;

}
