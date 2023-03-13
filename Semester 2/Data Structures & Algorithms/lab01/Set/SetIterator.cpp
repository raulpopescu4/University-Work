#include "SetIterator.h"
#include "Set.h"
#include <exception>
#include <iostream>

SetIterator::SetIterator(const Set& m) : set(m)
{
    if (set.isEmpty()) {
        this->current = 0;
        this->current_set = 1;
   }
	for(int index = 0; index <= abs(set.last_element - set.first_element) + 1; ++index){
        if(set.elements[index] == true){
            this->current = index;
            this->current_set = 1;
            break;
        }
    }
}


void SetIterator::first() {
    for(int index = 0; index <= abs(set.last_element - set.first_element) + 1; ++index){
        if(set.elements[index] == true){
            this->current = index;
            this->current_set = 1;
            break;
        }
    }
}


void SetIterator::next() {
    if(!this->valid())
        throw std::exception();
    if (this->current_set == set.size()) {
        this->current_set++;
        this->current = abs(set.last_element - set.first_element) + 2;
    }
    else{
        for (int index = this->current + 1; index <= abs(set.last_element - set.first_element) + 1; ++index) {
            if (set.elements[index] == true) {
                this->current = index;
                this->current_set++;
                break;
            }
        }
    }
}


TElem SetIterator::getCurrent(){
    if(!this->valid())
        throw std::exception();
    return (this->current + set.first_element);


}

bool SetIterator::valid() const{
    if (this->current_set <= set.size())
        return true;
    return false;
        
}



