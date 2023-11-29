// pdp_lab03.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <algorithm>

std::mutex mtx; 

std::vector<std::vector<int>> multiplyMatrices(const std::vector<std::vector<int>>& matrixA, const std::vector<std::vector<int>>& matrixB, int type) {
    int numRowsA = matrixA.size();
    int numColsA = matrixA[0].size();
    int numRowsB = matrixB.size();
    int numColsB = matrixB[0].size();

    std::vector<std::vector<int>> result(numRowsA, std::vector<int>(numColsB, 0));

    if (type == 0) { 
        for (int i = 0; i < numRowsA; ++i) {
            for (int j = 0; j < numColsB; ++j) {
                result[i][j] = 0;
                for (int k = 0; k < numColsA; ++k) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }
    }
    else if (type == 1) { 
        for (int i = 0; i < numRowsA; ++i) {
            for (int j = 0; j < numColsB; ++j) {
                result[i][j] = 0;
                for (int k = 0; k < numRowsB; ++k) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }
    }
    else { 
        int k = 4;
        for (int i = 0; i < numRowsA; ++i) {
            for (int j = 0; j < numColsB; ++j) {
                if (i % k == 0) {
                    result[i][j] = 0;
                    for (int x = 0; x < numColsA; ++x) {
                        result[i][j] += matrixA[i][x] * matrixB[x][j];
                    }
                }
            }
        }
    }

    return result;
}

void calculateAndPrintResult(const std::vector<std::vector<int>>& matrixA, const std::vector<std::vector<int>>& matrixB, int type) {
    auto result = multiplyMatrices(matrixA, matrixB, type);

    std::cout << "Product calculated type " << type << ":" << std::endl;
    for (const auto& row : result) {
        for (int value : row) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

void calculateAndPrintThreadPoolResult(const std::vector<std::vector<int>>& matrixA, const std::vector<std::vector<int>>& matrixB, int type) {
    int tasks = 4;
    int elementsPerTask = 20;
    int remainingElements = 21;

    std::vector<std::thread> threadPool;

    for (int i = 0; i < tasks; ++i) {
        if (i == tasks - 1) {
            elementsPerTask = remainingElements;
        }
        threadPool.emplace_back([i, &matrixA, &matrixB, &type]() {
            auto result = multiplyMatrices(matrixA, matrixB, type);
            std::lock_guard<std::mutex> lock(mtx);
            calculateAndPrintResult(matrixA, matrixB, type);
            });
    }

    for (auto& thread : threadPool) {
        thread.join();
    }
}

int main() {
    std::vector<std::vector<int>> matrixA = {
        {1, 2, 3, 4, 5, 6, 7, 8, 9},
        {2, 3, 4, 5, 6, 7, 8, 9, 1},
        {3, 4, 5, 6, 7, 8, 9, 1, 2},
        {4, 5, 6, 7, 8, 9, 1, 2, 3},
        {5, 6, 7, 8, 9, 1, 2, 3, 4},
        {6, 7, 8, 9, 1, 2, 3, 4, 5},
        {7, 8, 9, 1, 2, 3, 4, 5, 6},
        {8, 9, 1, 2, 3, 4, 5, 6, 7},
        {9, 1, 2, 3, 4, 5, 6, 7, 8}
    };

    std::vector<std::vector<int>> matrixB = {
        {9, 8, 7, 6, 5, 4, 3, 2, 1},
        {8, 7, 6, 5, 4, 3, 2, 1, 9},
        {7, 6, 5, 4, 3, 2, 1, 9, 8},
        {6, 5, 4, 3, 2, 1, 9, 8, 7},
        {5, 4, 3, 2, 1, 9, 8, 7, 6},
        {4, 3, 2, 1, 9, 8, 7, 6, 5},
        {3, 2, 1, 9, 8, 7, 6, 5, 4},
        {2, 1, 9, 8, 7, 6, 5, 4, 3},
        {1, 9, 8, 7, 6, 5, 4, 3, 2}
    };

    int userInput;

    std::cout << "Please enter how you want the solution to be solved: \n";
    std::cout << "1 - normal \n";
    std::cout << "2 - thread pool\n";
    std::cin >> userInput;

    if (userInput == 1) {
        calculateAndPrintResult(matrixA, matrixB, 0);
        calculateAndPrintResult(matrixA, matrixB, 1);
        calculateAndPrintResult(matrixA, matrixB, 2);
    }
    else if (userInput == 2) {
        calculateAndPrintThreadPoolResult(matrixA, matrixB, 0);
        calculateAndPrintThreadPoolResult(matrixA, matrixB, 1);
        calculateAndPrintThreadPoolResult(matrixA, matrixB, 2);
    }
    else {
        std::cout << "Not a valid option!" << std::endl;
    }

    return 0;
}
