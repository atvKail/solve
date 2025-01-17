#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>
#include <map>
#include <queue>
#include <algorithm>
#include<set>

using namespace std;
#define all(a) a.begin(), a.end()
#define forq(val, bg, en, step) for(int val = bg; val < en; val += step)
#define forv(v, m) for(auto v: m)
#define pb push_back
#define ld long
#define lld long long
#define f first
#define s second
using namespace std; 

/*
Interesting structures

decue<t> z(n-oe)
decue<t> z[100 - const]
mb [decue<t>, decue<t>...]
https://metanit.com/cpp/tutorial/7.8.php

bitset<4> =>  0000
https://learn.microsoft.com/ru-ru/cpp/standard-library/bitset-class?view=msvc-170

vector<t> n[100 - const]
mb [vector<t>, vector<t>...]
https://learn.microsoft.com/ru-ru/cpp/standard-library/vector-class?view=msvc-170
*/

class Optimization{
    const int INSERTION_SORT_THRESHOLD = 16;
    int partition(vector<int> &arr, int low, int high) {
        int pivotIndex = low + rand() % (high - low + 1);
        int pivot = arr[pivotIndex];
        swap(arr[pivotIndex], arr[high]);
        int i = low;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                swap(arr[i], arr[j]);
                i++;
            }
        }
        swap(arr[i], arr[high]);
        return i;
    }
    void insertionSort(vector<int> &arr, int low, int high) {
        for (int i = low + 1; i <= high; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= low && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    void QuickSort(vector<int> &arr, int low, int high) {
        if (low < high) {
            if (high - low + 1 <= INSERTION_SORT_THRESHOLD) {
                insertionSort(arr, low, high);
            } else {
                int pivotIndex = partition(arr, low, high);
                QuickSort(arr, low, pivotIndex - 1);
                QuickSort(arr, pivotIndex + 1, high);
            }
        }
    }
};
class Sorting {
    void bubble_sort(vector<int>& a)
    {
        int n = a.size();
        bool unordered = true;
        while (unordered) {
            unordered = false;
            for (int j = 0; j < n - 1; ++j) {
                if (a[j] > a[j + 1]) {
                    swap(a[j], a[j + 1]);
                    unordered = true;
                }
            }
            --n;
        }
    }

    void insertion_sort(vector<int>& a)
    {
        for (int i = 1; i < a.size(); ++i)
        {
            int tmp = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > tmp)
            {
                a[j + 1] = a[j];
                --j;
            }
            a[j + 1] = tmp;
        }
    }

    void CountSort(vector<int>& a) {
        vector<int> cnt(a.size(), 0);
        for (int el : a) {
            ++cnt[el];
        }
        a.resize(0);
        for (int d = 0; d < cnt.size(); ++d) {
            a.insert(a.end(), cnt[d], d);
        }
    }

    vector<int> merge(vector<int> a, vector<int> b) {
        vector<int> res;
        int i = 0;
        int j = 0;
        while (i < a.size() && j < b.size()) {
            if (a[i] <= b[j])
                res.push_back(a[i++]);
            else
                res.push_back(b[j++]);
        }
        while (i < a.size())
            res.push_back(a[i++]);
        while (j < b.size())
            res.push_back(b[j++]);
        return res;
    }
    vector<int> msort(vector<int> a) {
        if (a.size() <= 1)
            return a;
        int k = a.size() / 2;
        return merge(
            msort(vector<int>(a.begin(), a.begin() + k)),
            msort(vector<int>(a.begin() + k, a.end())));
    }

    vector<int> SelectionSort(vector<int> &a){
        int n = a.size(), z = 0;
        vector<int> temparyArr = a;
        for(int i = 0; i < n; i++){
            z = i;
            for(int j = i + 1; j < n; j++){
                if (a[j] < a[z]){
                    z = j;
                }
            }
            swap(a[z], a[i]);
        }
        return a;
    }
    
    vector<int> QuickSort(vector<int> &arr) {
        if (arr.size() <= 1) {
            return arr;
        }
        int m = arr[0];
        vector<int> left, right, equal;
        for (int num : arr) {
            if (num < m) {
                left.pb(num);
            } else if (num > m) {
                right.pb(num);
            } else {
                equal.pb(num);
            }
        }
        vector<int> sorted;
        vector<int> sortedLeft = QuickSort(left);
        vector<int> sortedRight = QuickSort(right);
        sorted.insert(sorted.end(), all(sortedLeft));
        sorted.insert(sorted.end(), all(equal));
        sorted.insert(sorted.end(), all(sortedRight));
        return sorted;
    }
    void QuickSortLowMemory(vector<int> &arr, int low, int high) {
        if (low < high) {
            int pivot = arr[low];
            int left = low + 1;
            int right = high;
            while (true) {
                while (left <= right && arr[left] <= pivot) {
                    left++;
                }
                while (arr[right] >= pivot && right >= left) {
                    right--;
                }

                if (left < right) {
                    swap(arr[left], arr[right]);
                } else {
                    break;
                }
            }
            swap(arr[low], arr[right]);
            QuickSortLowMemory(arr, low, right - 1);
            QuickSortLowMemory(arr, right + 1, high);
        }
    }
};
class MathematicalAlgorithms{
    vector<bool> sieve_eratosthenes(int limit){
        vector<bool> is_prime(limit + 1, true);
        is_prime[0] = is_prime[1] = false;
        for (int number = 2; number <= limit; ++number) {
            if (is_prime[number]) {
                for (int multiple = 2 * number; multiple <= limit; multiple += number) {
                    is_prime[multiple] = false;
                }
            }
        }
        return is_prime;
    }

    int gcd(int a,int b){
        if(b==0)
            return a;
        else
            return (b == 0) ? a : gcd(b,a%b);  
    }
    int lcm(int a,int b){
        return (a*b)/gcd(a,b);
    }
};
class AlgorithmsForGraphs{
    typedef pair<int,unsigned int> PII;
    typedef vector<PII> VPII;
    typedef vector<VPII> VVPII;
    // vector<VPII> graph;
    // VPII x0 = {};
    // graph.push_back(x0);
    // VPII x1 = {{0,5}, {2, 3}};
    // graph.push_back(x1);
    // VPII x2 = {{0,1}, {1,3}};
    // graph.push_back(x2);
    // int node_count  = 3;
    // int source_node = 1;
    // DijkstrasShortestPath(source_node, node_count, graph);
    const int INT_MAX = 1 << 11;
    void DijkstrasShortestPath (int source_node, int node_count, VVPII& graph) {
        const int INF = INT_MAX;
        vector<unsigned int> dist(node_count, INF);
        set<PII> set_length_node;
        dist[source_node] = 0;
        set_length_node.insert(PII(0,source_node));
        while (!set_length_node.empty()) {
            PII top = *set_length_node.begin();
            set_length_node.erase(set_length_node.begin());
            int current_source_node = top.second;
            for (PII it : graph[current_source_node]) {
                int adj_node = it.first;
                int length_to_adjnode = it.second;
                if (dist[adj_node] > length_to_adjnode + dist[current_source_node]) {
                    if (dist[adj_node] != INF) {
                    set_length_node.erase(set_length_node.find(PII(dist[adj_node],adj_node))); 
                    }
                    dist[adj_node] = length_to_adjnode + dist[current_source_node];
                    set_length_node.insert(PII(dist[adj_node], adj_node));
                }
            }
        }   
        for (int i=0; i<node_count; i++)
            cout << "Source Node(" << source_node << ") -> Destination Node(" << i << ") : " << dist[i] << endl;
    }

    
};