#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <stdio.h>
#include <string.h>
#include <cctype>
#include <cstdlib>

enum {
	INT,
	DOUBLE,
	CHAR,
	ERROR
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



int What_Type(char* value){

	char str[256];
	for (int i = 0; i < strlen(value); i++) {
		str[i] = *(value + i);
	}
	for (int i = 0; i < strlen(value); i++) {
	}

	if (isdigit(str[0]))
	{
		for (int i = 0; i < strlen(str); i++)
		{

			if ( str[i] == '.' ) {
				return 1;
			}

			if (i == strlen(str) - 1) {
				return 0;
			}
		}

	}

	else {
		return 2;
	}

	//printf("%s", dictionary.values[len].s);

	return 3;
}


////////////////////////////////////////////////////////////////////////////////////


struct Dict Put(struct Dict dictionary) {

	char* key = new char[256];
	printf("Insert the key:  ");
	scanf("%s", key);

	char* value = new char[256];
	printf("Insert its value:  ");
	scanf("%s", value);

	int type = What_Type(value);

	for (int i = 0; i < dictionary.len+1; i++) {
		if ( i == dictionary.len || strncat(key, (const char*)dictionary.Keys[i], strlen(key)) == 0) {
			if (type == DOUBLE) {
				double x = atof(value);
				dictionary.Values[i].act_value.d = x;
				dictionary.Values[i].type = 1;
			}
			else if (type == INT) {
				int x = atoi(value);
				dictionary.Values[i].act_value.i = x;
				dictionary.Values[i].type = 0;
			}
			else {
				char* x = value;
				dictionary.Values[i].act_value.s = x;
				dictionary.Values[i].type = 2;
			}
			dictionary.Keys[i] = key;
		}
		if (i == dictionary.len) {
			dictionary.len+=1;
			i++;
		}
	}


	return dictionary;

}


////////////////////////////////////////////////////////////////////////////////////


struct Value Get(struct Dict dictionary) {

	value get_value;
	get_value.type = 3;

	char* key = new char[256];
	printf("Insert the key:   ");
	scanf("%s", key);

	if (dictionary.len == 0) {
		printf("ERROR: dictionary is empty\n");
		return get_value;
	}

	for (int i = 0; i < dictionary.len; i++) {
		if (strncmp(key, (const char*)dictionary.Keys[i], strlen(key)) == 0) {
			if (dictionary.Values[i].type == DOUBLE) {
				get_value.act_value.d = dictionary.Values[i].act_value.d;
				get_value.type = 1;
			}
			else if (dictionary.Values[i].type == INT) {
				get_value.act_value.i = dictionary.Values[i].act_value.i;
				get_value.type = 0;
			}
			else {
				get_value.act_value.s = dictionary.Values[i].act_value.s;
				get_value.type = 2;
			}
		}
	}

	return get_value;
}


////////////////////////////////////////////////////////////////////////////////////


void Print(struct Dict dictionary)
{
	int n = 1234;

	value get_value = Get(dictionary);

	int type= get_value.type;

	if (type == DOUBLE) {
		double x = get_value.act_value.d;
		for (int i = 0; i < 8; i++) {
			for (int j = 1 << 7; j; j >>= 1) {
				printf("%d", j & get_value.act_value.bytes[i]);
			}
		}
	}


	else if (type == INT) {
		int x = get_value.act_value.i;
		for (int i = 0; i < 4; i++) {
			for (int j = 1 << 7; j; j >>= 1) {
				printf("%d", j & get_value.act_value.bytes[i]);
			}
		}
	}


	else {
		char* x = get_value.act_value.s;
		for (int i = 0; i < 1; i++) {
			for (int j = 1 << 7; j; j >>= 1) {
				printf("%d", j & get_value.act_value.bytes[i]);
			}
		}
	}

	
}