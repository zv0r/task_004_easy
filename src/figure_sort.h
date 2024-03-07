#ifndef FIGURE_SORT_H
#define FIGURE_SORT_H

typedef struct rect_t {
    int id;
    int area;
} Rect;

void input(Rect** rectangles, int* size);

void build_rect(Rect* rect, int id, int width, int height);

void sort(Rect* rectangles, int size);

void print_rectangles(Rect* rectangles, int size);

#endif