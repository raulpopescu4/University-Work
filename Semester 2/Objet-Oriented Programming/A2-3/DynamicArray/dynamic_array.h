

#ifndef A23OOP_DYNAMIC_ARRAY_H
#define A23OOP_DYNAMIC_ARRAY_H
#include "../domain/domain.h"

typedef struct {
    Country * data;
    int capacity;
    int length;
}DynamicArray;

DynamicArray createDynamicArray(int capacity);
void destroyDynamicArray(DynamicArray * array);
void addElement(DynamicArray * array, Country element);
void deleteElement(DynamicArray * array, int delete_index);
void updateElement(DynamicArray * array, int update_index, Country update_element);
//void resizeDynamicArray(DynamicArray * array);
int arrayCapacity(DynamicArray * array);
int arrayLength(DynamicArray * array);
#endif //A23OOP_DYNAMIC_ARRAY_H
