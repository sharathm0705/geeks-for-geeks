class Solution {
  public:
    int missingNum(int n, vector<int>& arr) {
        long long total = (long long)n * (n + 1) / 2;
        long long sum = 0;
        for(int x : arr) sum += x;
        return total - sum;
    }
};