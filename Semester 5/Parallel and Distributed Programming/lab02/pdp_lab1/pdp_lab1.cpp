#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <random>

std::vector<int> vector1;
std::vector<int> vector2; 
std::vector<int> products;
std::mutex mtx;
std::condition_variable cv;
bool ready = false;
const int vector_size = 10;

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> dis(1, 10);


void producer() {


    
    for (int i = 0; i < vector_size; ++i) {
        int product = vector1[i] * vector2[i];
        std::unique_lock<std::mutex> lock(mtx);
        products.push_back(product);
        ready = true;
        cv.notify_one();
        while (ready) {
            cv.wait(lock);
        }
    }
}

void consumer() {

    std::unique_lock<std::mutex> lock(mtx);
    long long sum = 0;
    for (int i = 0; i < vector_size; ++i) {
        cv.wait(lock, [] { return ready; });
        sum += products[i];
        ready = false;
        cv.notify_one();
    }
    std::cout << "Scalar product: " << sum << std::endl;
}

int main() {

    for (int i = 0; i < vector_size; ++i) {
        int randomInt = dis(gen);
        vector1.push_back(randomInt);
    }

    for (int i = 0; i < vector_size; ++i) {
        int randomInt = dis(gen);
        vector2.push_back(randomInt);
    }

    for (int i = 0; i < vector_size; ++i) {
        std::cout << vector1[i] << " ";
        
    }
    std::cout << '\n';
    
    for (int i = 0; i < vector_size; ++i) {
        std::cout << vector2[i] << " ";

    }
    std::cout << '\n';


    std::thread producerThread(producer);
    std::thread consumerThread(consumer);

    producerThread.join();
    consumerThread.join();

    return 0;
}
