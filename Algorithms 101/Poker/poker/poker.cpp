#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h> 
#include <string.h> 
#include <time.h>
#include <stdlib.h>

#include "Source.h"

#define cards_num 52
#define table_players_max 9


/*
todo:
 - функция которя определяет кол-во столов и рассаживет игроков по ним
 - функция которая создает колоду       ---\ можно 
 - функция которая перемешивает колоду  ---/ объединить
 - функция которая распределяет колоду между игроками
 - функция которая возвращает наименование карты по ее номеру
 - функция которая выводит все на экран
 -
 

тз:
 - енам
битовые поля
 - структуры
 - многофайловость

на вход:
кол-во игроков

на выход:
стол игроки и их руки (красиво)
*/



struct hand {
	char num;
	int card1;
	int card2;
};



int main() {
	//настройка рандома для перемешки карт
	srand(time(NULL));

	//получение входных значений
	int players_num;
	scanf("%d", &players_num);
	printf("\n");

	//динамический массив, первый элемент которого - кол-во нужных нам столов, 
	//а последующие - кол-ва игроков сидящих за каждым их них
	int * tables = Tables_Num_And_Table_Players_Num(players_num);

	for (int i = 1; i < tables[0] + 1; i++) {

		//создание и перемешка колоды
		int* deck = Create_And_Shuffle_Deck();

		//распределение карт по рукам
		struct hand* players = Distribute_Cards_To_Hands(tables[i],deck);
		
		//вывод
		printf("                  ---   Table  %d   ---   \n\n", i);
		Result(players);

		

	} 

	//завершаем программу
	return 0;
}