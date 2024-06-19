#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

class Graph {
public:
    Graph(int vertices) : V(vertices), graph(vertices, std::vector<int>(vertices, 0)) {}

    void addEdge(int u, int v) {
        graph[u][v] = 1;
    }

    void displayCycle(const std::vector<int>& path) const {
        for (int vertex : path) {
            std::cout << vertex << " ";
        }
        std::cout << path[0] << std::endl;
    }

    bool isSafe(int v, const std::vector<int>& path, int pos) const {
        if (graph[path[pos - 1]][v] == 0)
            return false;

        for (int i = 0; i < pos; ++i) {
            if (path[i] == v)
                return false;
        }

        return true;
    }

    void hamiltonianCycleUtil(int start, std::vector<int>& path, int pos, int numThreads) {
        if (pos == V) {
            if (graph[path[pos - 1]][start] == 1) {
                displayCycle(path);
                foundCycle = true;
            }
            return;
        }

        for (int v = 0; v < V; ++v) {
            if (isSafe(v, path, pos)) {
                path[pos] = v;

                if (pos % numThreads == 0) {
                    std::vector<std::thread> threads;
                    std::mutex mtx;

                    for (int neighbor : getNeighbors(v)) {
                        threads.emplace_back([&](int currentNeighbor) {
                            if (isSafe(currentNeighbor, path, pos + 1)) {
                                std::lock_guard<std::mutex> lock(mtx);
                                path[pos + 1] = currentNeighbor;
                                hamiltonianCycleUtil(start, path, pos + 1, numThreads);
                            }
                            }, neighbor);
                    }

                    for (auto& thread : threads) {
                        thread.join();
                    }
                }
                else {
                    hamiltonianCycleUtil(start, path, pos + 1, numThreads);
                }

                path[pos] = -1;
            }
        }
    }

    void hamiltonianCycle(int start, int numThreads) {
        std::vector<int> path(V, -1);
        path[0] = start;

        hamiltonianCycleUtil(start, path, 1, numThreads);

        if (!foundCycle) {
            std::cout << "No Hamiltonian cycle exists." << std::endl;
        }
    }

private:
    int V;
    std::vector<std::vector<int>> graph;
    bool foundCycle = false;

    std::vector<int> getNeighbors(int v) const {
        std::vector<int> neighbors;
        for (int i = 0; i < V; ++i) {
            if (graph[v][i] == 1) {
                neighbors.push_back(i);
            }
        }
        return neighbors;
    }
};

int main() {
    Graph graph(5);
    Graph cycleGraph(6);

    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);
    graph.addEdge(4, 0);

    cycleGraph.addEdge(0, 1);
    cycleGraph.addEdge(1, 2);
    cycleGraph.addEdge(2, 3);
    cycleGraph.addEdge(3, 4);
    cycleGraph.addEdge(4, 5);
    cycleGraph.addEdge(5, 0);
    cycleGraph.addEdge(5, 4);

    int startVertex = 0; 
    int numThreads = 5;

    graph.hamiltonianCycle(startVertex, numThreads);

    return 0;
}
