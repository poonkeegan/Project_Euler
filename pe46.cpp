#include <limits.h>
#include <stdio.h>
const int ARR_SIZE = 1<<14;
bool isPrime[ARR_SIZE] = {};
int primes[ARR_SIZE] = {};
int size = 0;
void initPrime(){
    isPrime[0] = false;
    isPrime[1] = false;
    int i = 0;
    for(i = 2; i < ARR_SIZE; i++){
        isPrime[i] = true;
    }
    for(i = 0; i < ARR_SIZE; i++){
        int j = i + i;
        if(isPrime[i]){
            primes[size] = i;
            size += 1;
            while(j < ARR_SIZE){
                isPrime[j] = false;
                j += i;
            }
        }
    }
}


bool squares[ARR_SIZE] {};
int smallestRoot = 0;
int squaresSize = 0;
bool isSquare(int n){
    while(n > squaresSize){
        smallestRoot++;
        squares[smallestRoot * smallestRoot] = true;
        squaresSize = smallestRoot * smallestRoot;
    }
    return squares[n];
}
void initSquares(){
    squares[0] = true;
    for(int i = 1; i < ARR_SIZE; i++){
        squares[i] = false;
    }
}
void init(){
    initPrime();
    initSquares();
}

bool primeAndSquare(int n){
    for(int i = 0; 2*i*i <n; i++){
        int val = 2*i*i;
        if(isPrime[n-val]){
            printf("%d = %d + 2x%d^2\n",n, n - val, i);
            return true;
        }
    }
    return false;
}

int main(){
    init();
    for(int i = 3; isPrime[i] || primeAndSquare(i); i+=2){
    }
    return 0;
}

