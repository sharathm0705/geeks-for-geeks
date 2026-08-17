class Solution {
  public:
    int reverseDigits(int n) {
        // Code here
        int temp = n;
        int answer = 0;
        while(n>0)
        {
           answer = (answer *10) + n % 10;
           n = n/10;
        }
        return answer;
    } 
};