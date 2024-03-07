#include "figure_sort.h"

#include <stdio.h>
#include <stdlib.h>

#include "misc.h"

int main(void) {
    int size = 0;
    Rect* rectangles = NULL;

    input(&rectangles, &size);
    sort(rectangles, size);
    print_rectangles(rectangles, size);

    free(rectangles);
    return 0;
}

void print_rectangles(Rect* rectangles, int size) {
    for (int i = 0; i < size; i++) {
        printf(i > 0 ? "\n" : "");
        printf("%d %d", rectangles[i].id, rectangles[i].area);
    }
}

void sort(Rect* rectangles, int size) {
    for (int step = 0; step < size - 1; step++) {
        for (int i = 0; i < size - step - 1; i++) {
            if (rectangles[i].area > rectangles[i + 1].area) {
                Rect temp = rectangles[i];
                rectangles[i] = rectangles[i + 1];
                rectangles[i + 1] = temp;
            }
        }
    }
}

void build_rect(Rect* rect, int id, int width, int height) {
    rect->id = id;
    rect->area = width * height;
}

void input(Rect** rectangles, int* size) {
    if (scanf("%d", size) == 1 && *size > 0) {
        *rectangles = malloc(*size * sizeof(Rect));
        int tmp_width, tmp_height, tmp_id;
        for (int i = 0; i < *size; i++) {
            if (scanf("%d%d%d", &tmp_id, &tmp_width, &tmp_height) == 3 && tmp_id > 0 && tmp_width > 0 &&
                tmp_height > 0) {
                build_rect(*rectangles + i, tmp_id, tmp_width, tmp_height);
            } else {
                free(*rectangles);
                achtung();
            }
        }
    } else {
        achtung();
    }
}
