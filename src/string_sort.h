#ifndef STRING_SORT_H
#define STRING_SORT_H

void input_string(char** input);

void menu(int* menu_choice);

void process_input(char* input, int menu_choice);

void print_sorted_string(char* input);

void sort(char* input, int direction);

#endif