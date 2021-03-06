#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <stdio.h>

#include "Source.h"


typedef struct GRAPH {
	int** table;
	int v_num;
	int* e_values;
}Graph;

typedef struct Tree {
	int** t;
};

void main() {

	// ???????? ?????
	Graph graph = Data_Input();

	printf("Your input graph:\n");
	for (int i = 0; i < graph.v_num; i++)  {
		for (int j = 0; j < graph.v_num; j++) {
			printf("%d  ", graph.table[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	// ??????? ??????
	int** t = (int**)malloc(graph.v_num * sizeof(int*));
	for (int i = 0; i < graph.v_num; i++) {
		t[i] = (int*)malloc(graph.v_num * sizeof(int));
		for (int j = 0; j < graph.v_num; j++) {
			t[i][j] = 0;
		}
	}

	Graph tree;
	tree.table = t;
	tree.v_num = graph.v_num;
	tree.e_values = graph.e_values;

	/////////////////////////////////////////////////

	
	int* used = (int*)malloc((graph.v_num *2 ) * sizeof(int));
	// ?????? ? ??????? ?????? ?????? ???-?? ??????????? ????? ???, ????? ?? ?????????????? ??????

	int e_counter = 0;
	int k = 0;
	while (e_counter < graph.v_num - 1){
		for (int i = 0; i < graph.v_num; i++) {
			for (int j = 0; j < graph.v_num; j++) {
				if (graph.table[i][j] == graph.e_values[k]) {
					for (int u = 1; u < graph.v_num+2; u++) {
						used[u] = -1;
					}
					used[0] = 0;
					if (If_Cycle(tree, i, j, used) == 0) {
						graph.table[i][j] = 0;
						graph.table[j][i] = 0;
						tree.table[i][j] = graph.e_values[k];
						tree.table[j][i] = graph.e_values[k];
						e_counter++;
					}
				}
			}
		}
		k++;
	}


	
	printf("Output tree:\n");
	for (int i = 0; i < graph.v_num; i++) {
		for (int j = 0; j < graph.v_num; j++) {
			printf(" %d ", tree.table[i][j]);
		}
		printf("\n");
	}


	/////////////////////////////////////////////////

	for (int i = 0; i < graph.v_num; i++) {
		free(graph.table[i]);
		free(tree.table[i]);
	}
	free(graph.table);
	free(tree.table);
	free(used);
	free(t);
}


