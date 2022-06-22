#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <stdio.h>
#include <string.h>
#include <cctype>
#include <cstdlib>

#include "Source.h"

/*todo:
- массив из ключей
- массив из значений 
- переменная отвечающая за размер словаря
*/

enum {
	INT,
	DOUBLE,
	CHAR,
	ERROR,
};

enum {
	EXIT,
	PUT,
	GET,
	PRINT

};

typedef union Value_Type {
	int i;
	double d;
	char* s;
	char bytes[8];
}v_type;

typedef struct Value {
	int type;
	union Value_Type act_value;
}value;

typedef struct Dict {
	int len;
	char** Keys;
	value* Values;
}dict;


int main() {
	int n = 256;

	char** keys = (char**)malloc(n * sizeof(char*));
	value* values = (value*)malloc(n * sizeof(value));

	dict dictionary;
	dictionary.Values = values;
	dictionary.Keys = keys;
	dictionary.len = 0;

	printf(" 1 - Put new (change) value with a given key\n");
	printf(" 2 - Get value of a given key\n");
	printf(" 3 - Print value of a given key with its bytes\n");
	printf(" 0 - Exit programm\n\n");
	
	int step;
	while (1)
	{
		printf("-----------------------------\n");
		printf("\nChoose your step\n");
		scanf("%d", &step);
		printf("\n");

		if (step != 0 && step != 1 && step != 2 && step != 3) {
			printf("\nERROR: step number was incorrect\n");
		}

		if (step == EXIT) {
			return 0;
		}

		if (step == PUT) {
			dictionary = Put(dictionary);
		}

		else if (step == GET) {
			value get_value = Get(dictionary);
			if (get_value.type == DOUBLE) {
				printf("%f\n", get_value.act_value.d);
			}
			else if (get_value.type == INT) {
				printf("%d\n", get_value.act_value.i);
			}
			else if (get_value.type == CHAR) {
				printf("%s\n", get_value.act_value.s);
			}
			else {
				printf("ERROR: no value for the given key\n");
			}
		}

		else if (step == PRINT) {
			Print(dictionary);
		}
		printf("\n-----------------------------");
	}

	

	return 0;
}