#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>
#include <utility>

using namespace std;


MultiMap::MultiMap() {
	this->capacity = 100;
	this->nodes = new DLLANode[this->capacity]{NULL_PAIR};
	this->dlla_size = 0;
	this->head = -1;
	this->tail = -1;
	this->first_empty = 0;

}


void MultiMap::add(TKey c, TValue v) {
	DLLANode new_node;
	new_node.info.first = c;
	new_node.info.second = v;
	if (this->dlla_size + 1 == capacity || (this->dlla_size + 2 >= this->capacity && this->nodes[this->first_empty].next == -1)) {
		this->capacity *= 2;

		DLLANode* elements = new DLLANode[this->capacity];
		for (int index = 0; index < this->dlla_size; index++){
			elements[index] = this->nodes[index];

		delete[] this->nodes;
		this->nodes = elements;
	}
	if (this->isEmpty()) {
		this->dlla_size++;
		this->head = 0;
		this->tail = 0;
		this->first_empty = 1;
		this->nodes[this->first_empty] = DLLANode(make_pair(NULL_TVALUE, NULL_TVALUE), -1, -1);
		new_node.next = -1;
		new_node.prev = -1;
		this->nodes[this->head] = new_node;
		return;
	}
	else if (this->nodes[this->first_empty].next == -1) {
		this->dlla_size++;
		this->nodes[this->tail].next = first_empty;
		new_node.prev = this->tail;
		new_node.next = -1;
		this->tail = this->first_empty;
		this->first_empty = this->dlla_size;
		this->nodes[this->first_empty] = DLLANode(make_pair(NULL_TVALUE, NULL_TVALUE), -1, -1);
		this->nodes[this->tail] = new_node;
		return;
	}
	else if (this->nodes[first_empty].next != -1) {
		this->dlla_size++;
		this->nodes[this->tail].next = first_empty;
		new_node.prev = this->tail;
		new_node.next = -1;
		this->tail = this->first_empty;
		this->first_empty = this->nodes[this->first_empty].next;
		this->nodes[this->tail] = new_node;
		return;
	}
	
	

}// bc = 1, ac = n,wc = n, total case : O(n) (n <- dlla_size) 


bool MultiMap::remove(TKey c, TValue v) {
	if (this->isEmpty())
		return false;
	DLLANode element = this->nodes[head];
	for (int i = 0; i < this->dlla_size; ++i) {
		if (element.info.first == c && element.info.second == v) {
			if (this->dlla_size == 1) {
				this->dlla_size = 0;
				this->head = -1;
				this->tail = -1;
				this->first_empty = 0;
				return true;
			}
			else if (element.prev == -1) {
				int aux;
				aux = this->first_empty;
				this->first_empty = this->head;
				this->nodes[this->first_empty].next = aux;
				this->head = element.next;
				this->nodes[element.next].prev = -1;
				this->dlla_size--;
				return true;
			}
			else if (element.next == -1) {
				if (this->nodes[element.prev].next < this->first_empty) {
					int aux;
					aux = this->first_empty;
					this->first_empty = this->tail;
					this->nodes[this->first_empty].next = aux;
				}
				this->tail = element.prev;
				this->nodes[element.prev].next = -1;
				this->dlla_size--;
				return true;
			}
			else {
				if (this->nodes[element.prev].next < this->first_empty) {
					int aux;
					aux = this->first_empty;
					this->first_empty = this->nodes[element.prev].next;
					this->nodes[this->first_empty].next = aux;
				}
				this->nodes[element.prev].next = element.next;
				this->nodes[element.next].prev = element.prev;
				this->dlla_size--;
				return true;
			}

		}
		if (element.next != -1)
			element = this->nodes[element.next];
	}
	return  false;
}// bc = 1, ac = n, wc = n, total: O(n) (n <- dlla_size)


vector<TValue> MultiMap::search(TKey c) const {
	vector<TValue> return_vector;

	if (this->isEmpty())
		return return_vector;

	DLLANode element = this->nodes[head];
	for (int i = 0; i < this->dlla_size; ++i) {
		if (element.info.first == c)
			return_vector.push_back(element.info.second);
		if(element.next != -1)
			element = this->nodes[element.next];
	}
	return return_vector;
	
}// bc = 1, ac = n, wc = n, total: O(n) (n <- dlla_size)


int MultiMap::size() const {
	return this->dlla_size;
}//theta(1)


bool MultiMap::isEmpty() const {
	if (this->dlla_size == 0)
		return true;
	return false;
}//theta(1)

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}//theta(1)


MultiMap::~MultiMap() {
	delete[] this->nodes;
}
void MultiMap::print()
{
	for (int i = 0; i < this->dlla_size; ++i) {
		std::cout << this->nodes[i].info.first << " ";
		std::cout << this->nodes[i].info.second << " ";
		std::cout << this->nodes[i].prev << " ";
		std::cout << this->nodes[i].next<< " \n";
	}
}
// theta(1)

DLLANode::DLLANode() : info{NULL_TELEM}, prev{-1}, next{-1}
{
}

DLLANode::DLLANode(TElem pair, int prev, int next) : info {std::move(pair)}, prev {prev}, next {next}
{
}
