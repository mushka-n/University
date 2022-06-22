#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h> 
#include <string.h> 
#include <time.h>
#include <stdlib.h>
#include <malloc.h>

//константы -размер колоды и стола
#define cards_num 52
#define table_players_max 9

//структура руки
struct hand {
	char num;
	int card1;
	int card2;
};

//я реально не знаю где это еще может пригодяиться
enum just_not_to_get_my_ass_wooped {
	ANOTHER_TABLE_IS_NOT_NEEDED,
	ANOTHER_TABLE_IS_NEEDED
};


//----------------------------------------------------------------------------


int* Tables_Num_And_Table_Players_Num(int players_num)
{
	//определяем какое кол-во столов нам необоходимо
	int tables_num = players_num / table_players_max;
	if (players_num % table_players_max != 0) {
		tables_num+=ANOTHER_TABLE_IS_NEEDED;
	}
	else {
		tables_num += ANOTHER_TABLE_IS_NOT_NEEDED;
	}

	//динамический массив, первый элемент которого - кол-во столов, а последующие - кол-во игроков на каждом
	int* tables = (int*)malloc((tables_num + 1) * sizeof(int));
	tables[0] = tables_num;

	//распределение игроков по столам
	if (players_num % table_players_max != 0 && players_num > table_players_max) 
	{
		for (int i = 1; i < tables_num - 1; i++) {
			tables[i] = 9;
		}
		tables[tables_num - 1] = ((table_players_max + (players_num % table_players_max)) / 2) + ((table_players_max + (players_num % table_players_max)) % 2);
		tables[tables_num] = (table_players_max + (players_num % table_players_max)) / 2;
	}
	else if (players_num % table_players_max != 0 && players_num < table_players_max) {
		tables[1] = players_num;
	}
	else {
		for (int i = 1; i < tables_num + 1; i++) {
			tables[i] = table_players_max;
		}
	}

	//возвращаем значение
	return tables;
}


int* Create_And_Shuffle_Deck()
{
	//создаем динамический массив из чисел 0-51 
	int* deck = (int*)malloc(cards_num * sizeof(int));
	for (int i = 0; i < cards_num; i++) {
		//printf("%d", i);
		deck[i] = i;
	}

	//перемешиваем числа в массиве
	for (int i = 0; i < cards_num; i++) {
		int random = rand() % 51;
		int temp = i;
		deck[i] = deck[random];
		deck[random] = temp;
	}

	//возвращаем массив
	return deck;
}


struct hand * Distribute_Cards_To_Hands(int players_num, int* deck) {
	//массив из структур типа рука
	struct hand* players = (struct hand*)malloc(players_num * sizeof(struct hand));

	//заполняем руки игроков и id использованных карт равным -1
	for (int i = 0; i < players_num * 2; i+=2) {
		players[i/2].card1 = deck[i];
		players[i/2].card2 = deck[i + 1];
		players[i / 2].num = (char)(i / 2);
		deck[i] = -1;
		deck[i + 1] = -1;
	}
	for (int i = players_num; i < table_players_max; i++) {
		players[i].card1 = -1;
		players[i].card2 = -1;
		players[i].num = (char)"-";
	}


	//возвращаем массив структур
	return players;
}


void Read_Card(int card) {

	char rank_alph[13][3] = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
	char suit_alph[4][2] = { "S", "C", "H", "D" };

	char* suit = suit_alph[card / 13];
	char* rank = rank_alph[card % 13];

	char* t;
	
	if (card == -1 or card>51) {
		t = (char*)"--";
	}
	else {
		t = strncat(rank, suit, 2);
	}

	printf("%s", t);

	t = (char*)"";
}


int* Dealers_Cards(int* deck){

	//printf("%d", deck[51]);

	int* dealers_cards = (int*)malloc(5 * sizeof(int));

	int k = 0;
	for (int i = 51; i > 46; i-=1) {
		dealers_cards[k] = 0;
		dealers_cards[k] = deck[i];
		
		//printf("%d %d\n", k, i);
		//printf("%d %d\n", dealers_cards[k], deck[i]);
		k++;
		//printf(" --- %d --- \n", dealers_cards[k]);
	}

	return dealers_cards;
}


void Result(struct hand * players) {

	printf("            player 1    [dealer]    player 9\n");

	printf("            ");
	Read_Card(players[0].card1);
	printf(" / ");
	Read_Card(players[0].card2);
	printf("                 ");
	Read_Card(players[8].card1);
	printf(" / ");
	Read_Card(players[8].card2);
	printf("\n\n");

	 
	printf("  player 2                                      player 8\n");

	printf("  ");
	Read_Card(players[1].card1);
	printf(" / ");
	Read_Card(players[1].card2);
	printf("                                       ");
	Read_Card(players[7].card1);
	printf(" / ");
	Read_Card(players[7].card2);
	printf("\n");


	printf("\n");
	printf("  player 3                                      player 7\n");

	printf("  ");
	Read_Card(players[2].card1);
	printf(" / ");
	Read_Card(players[2].card2);
	printf("                                       ");
	Read_Card(players[6].card1);
	printf(" / ");
	Read_Card(players[6].card2);
	printf("\n\n");


	printf("            player 4    player 5    player 6\n");

	printf("            ");
	Read_Card(players[3].card1);
	printf(" / ");
	Read_Card(players[3].card2);
	printf("     ");
	Read_Card(players[4].card1);
	printf(" / ");
	Read_Card(players[4].card2);
	printf("     ");
	Read_Card(players[5].card1);
	printf(" / ");
	Read_Card(players[5].card2);
	printf("\n\n");



	printf("\n\n");
}









