#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arr[11] = {0,};
int maxArr[11];
int max = 0;

void track(int arrow, int* info) {
    if(!arrow) {
        int apeach = 0, line = 0;
        for(int i = 0; i < 10; i++) {
            if(arr[i] || info[i]) {
                arr[i] > info[i] ? (line += 10 - i) : (apeach += 10 - i);
            }
        }

        if(line - apeach >= max) {
            memcpy(maxArr, arr, sizeof(int) * 11);
            max = line - apeach;
        }
        return;
    }

    for(int i = 0; i <= 10 && arr[i] <= info[i]; i++) {
        arr[i]++;
        track(arrow - 1, info);
        arr[i]--;
    }
}

int* solution(int n, int info[], size_t len) {
    int* loss = (int*)malloc(sizeof(int));
    loss[0] = -1;
    track(n, info);
    return max ? maxArr : loss;
}
