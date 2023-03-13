#include "Matrix.h"
#include <exception>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
	
	SLLElement* first_element = new SLLElement;
	this->nr_lines = nrLines;
	this->nr_columns = nrCols;
	this->first_element = first_element;
	this->first_element->element.column = -1;
	this->first_element->element.line = -1;
	this->first_element->element.value = NULL_TELEM;
	this->first_element->next = nullptr;
	
}


int Matrix::nrLines() const {
	return this->nr_lines;
}//theta(1)


int Matrix::nrColumns() const {
	return this->nr_columns;
}//theta(1)


TElem Matrix::element(int i, int j) const {
	
	if ((i < 0) || (i > this->nr_lines))
		throw std::exception();
	if ((j < 0) || (j > this->nr_columns))
		throw std::exception();
	if (first_element->next == nullptr)
		return NULL_TELEM;
	SLLElement* next_element = this->first_element->next;
	while (next_element != nullptr) {
		if ((next_element->element.line == i) && (next_element->element.column == j))
			return next_element->element.value;
		next_element = next_element->next;
	}
	return NULL_TELEM;
}// bc = theta(1) wc = theta(nr elements) O(nr elements)

TElem Matrix::modify(int i, int j, TElem e) {
	if ((i < 0) || (i > this->nr_lines))
		throw std::exception();
	if ((j < 0) || (j > this->nr_columns))
		throw std::exception();
	if ((Matrix::element(i, j) == NULL_TELEM)) {
		SLLElement* new_element = new SLLElement;
		new_element->element.line = i;
		new_element->element.column = j;
		new_element->element.value = e;
		new_element->next = nullptr;
		if ((first_element->next == nullptr))
			first_element->next = new_element;
		else {
			SLLElement* next_element = this->first_element->next;
			while (next_element != nullptr) /*{
				if (((i >= next_element->element.line) && (j > next_element->element.column)) && next_element->next == nullptr) {
					next_element->next = new_element;
					return NULL_TELEM;
				}

				if ((i <= next_element->next->element.line) && (j < next_element->next->element.column)) {
					SLLElement* aux = next_element->next;
					next_element->next = new_element;
					new_element->next = aux;
					return NULL_TELEM;
				}
				if ((i > next_element->element.line) || (j >= next_element->element.column))
					next_element = next_element->next;

			}*/
			{
				if ((i >= next_element->element.line) && (j > next_element->element.column)) {
					if (next_element->next == nullptr) {
						next_element->next = new_element;
						return NULL_TELEM;
					}
					else {
						if ((i < next_element->next->element.line) || (j <= next_element->next->element.column)) {
							SLLElement* aux = next_element->next;
							next_element->next = new_element;
							new_element->next = aux;
							return NULL_TELEM;
						}
						else {
							next_element = next_element->next;
						}
					}
				}
				else {
					first_element->next = new_element;
					new_element->next = next_element;
					return NULL_TELEM;
				}

			}
		}

	}
	else {
		if ((first_element->element.line == i) && (first_element->element.column == j)) {
			TElem last_value = NULL_TELEM;
			last_value = first_element->element.value;
			first_element->element.value = e;
			return last_value;
		}
		SLLElement* next_element = this->first_element->next;
		while (next_element != nullptr) {
			if ((next_element->element.line == i) && (next_element->element.column == j)) {
				TElem last_value = NULL_TELEM;
				last_value = next_element->element.value;
				next_element->element.value = e;
				return last_value;
			}
			next_element = next_element->next;
		}
	}
}

void Matrix::print_matrix() {
	for (int i = 0; i < this->nrLines(); ++i){
		for (int j = 0; j < this->nrColumns(); ++j) 
			cout << this->element(i, j) << " ";
		cout << endl;
		}
	cout << endl;
}


