#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	this->position = col.head;
}

TElem MultiMapIterator::getCurrent() const{
	if (!this->valid())
		throw std::exception();
	return col.nodes[this->position].info;
}

bool MultiMapIterator::valid() const {
	return position != -1;
}

void MultiMapIterator::next() {
	if (!this->valid())
		throw exception();
	this->position = col.nodes[this->position].next;
}

void MultiMapIterator::first() {
	this->position = col.head;
}

