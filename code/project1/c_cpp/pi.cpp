#include <stdio.h>
int cauculatepi(int n){
    double pi = 0.0;
    for (int i = 0; i < n; i++){
        pi += 1.0 / (2 * i + 1);
    }
    return pi;
}