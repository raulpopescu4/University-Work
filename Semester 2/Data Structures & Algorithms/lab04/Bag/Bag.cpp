#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;


Bag::Bag() {
	this->capacity = 128;
    this->table_size = 0;
    this->load_factor = 0.7;
    this->table = new Pair[this->capacity];
    for(int i = 0; i < this->capacity; ++i)
        this->table[i] = NULL_PAIR;
    this->bag_size = 0;

}// theta(n)


void Bag::add(TElem elem) {
    int tries = 0;
    int index = this->quadratic_function(elem, tries);
    if(this->table_size + 1 > int(this->load_factor * this->capacity)){
        long int old_capacity = this->capacity;
        this->capacity *= 2;
        Pair* new_table = new Pair[this->capacity];
        for(int i = 0; i < this->capacity; ++i)
            new_table[i] = NULL_PAIR;
        for(int i = 0; i < old_capacity; ++i){
            if(this->table[i] != NULL_PAIR  && this->table[i] != tombstone){
                tries = 0;
                index = this->quadratic_function(table[i].first, tries);
                while (true){
                    if(new_table[index] == NULL_PAIR){
                        new_table[index] = this->table[i];
                        break;
                    }
                    else{
                        tries++;
                        index = this->quadratic_function(table[i].first, tries);
                    }
                }
            }
        }
        delete[] this->table;
        this->table = new_table;
        tries = 0;
        index = this->quadratic_function(elem, tries);

    }
    while (true){
        if(this->table[index] == NULL_PAIR || this->table[index] == tombstone){
            Pair new_element;
            new_element.first = elem;
            new_element.second = 1;
            this->table[index] = new_element;
            this->table_size++;
            this->bag_size++;
            return;
        }
        else{
            if(this->table[index].first == elem){
                this->table[index].second++;
                this->bag_size++;
                return;
            }

        }
        tries++;
        index = this->quadratic_function(elem, tries);

    }
}//bc: theta(1) ac: theta(n) wc: theta(n) total case: 0(n), n = capacity


bool Bag::remove(TElem elem) {
    int tries = 0;
    int index = this->quadratic_function(elem, tries);
    if(this->isEmpty())
        return false;
    while(this->table[index] != NULL_PAIR){
        if(this->table[index].first == elem && this->table[index].second == 1) {
            this->table[index] = tombstone;
            this->bag_size--;
            return true;
        }
        if(this->table[index].first == elem && this->table[index].second != 1){
            this->table[index].second --;
            this->bag_size--;
            return true;
        }
            tries++;
            index = this->quadratic_function(elem, tries);


    }
	return false; 
}//bc: theta(1) ac: theta(n) wc: theta(n) total case: 0(n), n = capacity


bool Bag::search(TElem elem) const {
    int tries = 0;
    int index = this->quadratic_function(elem, tries);
    if(this->isEmpty())
        return false;
    while(this->table[index] != NULL_PAIR){
        if(this->table[index].first == elem)
            return true;
        tries++;
        index = this->quadratic_function(elem, tries);


    }
	return false; 
}//bc: theta(1) ac: theta(n) wc: theta(n) total case: 0(n), n = capacity

int Bag::nrOccurrences(TElem elem) const {
    int tries = 0;
    int index = this->quadratic_function(elem, tries);
    if(this->isEmpty())
        return false;
    while(this->table[index] != NULL_PAIR){
        if(this->table[index].first == elem)
            return this->table[index].second;
        tries++;
        index = this->quadratic_function(elem, tries);

    }
    return 0;
}//bc: theta(1) ac: theta(n) wc: theta(n) total case: 0(n), n = capacity


int Bag::size() const {
	return this->bag_size;
}//theta(1)


bool Bag::isEmpty() const {
	return (this->table_size == 0);
}//theta(1)

BagIterator Bag::iterator() const {
	return BagIterator(*this);
}//theta(1)


Bag::~Bag() {
	delete[] this->table;
}// theta(1)

