#include "Set.h"
#include "SetIterator.h"
#include "iostream"

Set::Set() {
    this->last_element = 0;
	this->elements = new bool[1];
    this->first_element = 0;
    this->elements[0] = false;
    this->set_size = 0;
}


bool Set::add(TElem elem) {

    if ((elem >= this->first_element) && (elem <= this->last_element)){
        if (this->elements[abs(this->first_element - elem)] == true) {
            return false;
        }
        this->elements[abs(this->first_element - elem)] = true;
        this->set_size++;
        return true;
    }

    if (elem < this->first_element){
        TElem new_first_element = elem;
        bool* new_elements = new bool[abs(this->last_element - new_first_element) + 2];
        for(int index = 0; index < abs(this->first_element - new_first_element) + 1; ++index){
            if (index == 0){
                new_elements[index] = true;
            }
            else{
                new_elements[index] = false;
            }
        }
        for(int index = 0; index < abs(this->last_element - this->first_element) + 1; ++index){
            new_elements[index + abs(this->first_element - new_first_element)] = this->elements[index];
        }
        new_elements[abs(this->last_element - new_first_element) + 1] = false;
        delete[] this->elements;
        this->elements = new_elements;
        this->first_element = new_first_element;
        /*std::cout<<"for <"<<std::endl;
        for(int index = 0; index < abs(this->last_element - this->first_element) + 1; ++index)
            std::cout<<this->elements[index]<<" "<<this->first_element+index<<std::endl;*/
        this->set_size++;
        return true;

    }
    if (elem > this->last_element){
        TElem new_last_element = elem;
        bool* new_elements = new bool[abs(new_last_element - this->first_element) + 2];
        for(int index = abs(this->last_element - this->first_element) + 1; index < (abs(new_last_element - this->first_element) + 1); ++index){
            if(index == abs(new_last_element - this->first_element)){
                new_elements[index] = true;
            }
            else{
                new_elements[index] = false;
            }
        }
        for(int index = 0; index < abs(this->last_element - this->first_element) + 1; ++index){
            new_elements[index] = this->elements[index];
        }
        new_elements[abs(new_last_element - this->first_element) + 1] = false;
        delete [] this->elements;
        this->elements = new_elements;
        this->last_element = new_last_element;
        /*std::cout<<"for >"<<std::endl;
        for(int index = 0; index < abs(this->last_element - this->first_element) + 1; ++index)
            std::cout<<this->elements[index]<<" "<<index + this->first_element<<std::endl;*/
        this->set_size++;
        return true;
    }

}


bool Set::remove(TElem elem) {
    /*for(int index = 0; index <= abs(this->last_element - this->first_element) + 1; ++index){
        if(this->first_element + index == elem){
            if(this->elements[index] == true){
                this->elements[index] = false;
                return true;
            }
            else
                return false;
        }
    }
	return false;*/
    if (elem < this->first_element)
        return false;
    if (elem > this->last_element)
        return false;
    if (this->elements[abs(this->first_element - elem)] == true) {
        this->elements[abs(this->first_element - elem)] = false;
        this->set_size--;
        return true;
    }
    else
        return false;
    return false;
}

bool Set::search(TElem elem) const {
	/*for(int index = 0; index <= abs(this->last_element - this->first_element) + 1; ++index){
        if(this->first_element + index == elem){
            if(this->elements[index] == true)
                return true;
            else
                return false;
        }

    }
	return false;*/
    if (elem < this->first_element)
        return false;
    if (elem > this->last_element)
        return false;
    if (this->elements[abs(this->first_element - elem)] == true)
        return true;
    else
        return false;
    
}



int Set::size() const {
   /* int set_size = 0;
    for(int index = 0; index <= abs(this->last_element - this->first_element) + 1; ++index){
        if(this->elements[index] == true) {
            set_size++;
        }
    }*/
    return this->set_size;
}


bool Set::isEmpty() const {
	for(int index = 0; index <= abs(this->last_element - this->first_element) + 1; ++index){
        if(this->elements[index] == true)
            return false;
    }
	return true;
}


Set::~Set() {
	delete[] this->elements;
}


SetIterator Set::iterator() const {
	return SetIterator(*this);
}


