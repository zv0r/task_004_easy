#include "string_sort.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "misc.h"

int main(void) {
    char* input = NULL;
    int menu_choice = 0;

    input_string(&input);
    menu(&menu_choice);
    process_input(input, menu_choice);
    print_sorted_string(input);

    free(input);
    return 0;
}

void sort(char* string, int direction) {
    int size = strlen(string);
    for (int step = 0; step < size - 1; step++) {
        for (int i = 0; i < size - step - 1; i++) {
            if (direction ? string[i] > string[i + 1] : string[i] < string[i + 1]) {
                int temp = string[i];
                string[i] = string[i + 1];
                string[i + 1] = temp;
            }
        }
    }
}

void process_input(char* input, int menu_choice) {
    switch (menu_choice) {
        case 1:
            sort(input, 1);
            break;
        case 2:
            sort(input, 0);
            break;
        default:
            free(input);
            achtung();
    }
}

void print_sorted_string(char* input) { printf("%s", input); }

void input_string(char** input) {
    scanf("%ms", input);
    for (int i = 0; (*input)[i]; i++) {
        if ((*input)[i] < 97 || (*input)[i] > 122) {
            free(*input);
            achtung();
        }
    }
}

void menu(int* menu_choice) {
    if (scanf("%d", menu_choice) != 1) {
        *menu_choice = 0;
    }
}