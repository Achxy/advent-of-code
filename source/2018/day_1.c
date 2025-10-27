#include <stdio.h>
#include <stdlib.h>


long part_1(FILE *fp) {
    long sigma = 0;
    char line[1 << 4];
    while (fgets(line, sizeof(line), fp) != NULL) {
        sigma += strtol(line, NULL, 10);
    }
    return sigma;
}

int main(void) {
    FILE *fp;
    fp = fopen("../../data/2018_1.txt", "r");
    if (fp == NULL) {
        printf("bruh\n");
        return 1;
    }
    printf("Part 1: %ld", part_1(fp));
    printf("\n");
    fclose(fp);
    return 0;
}