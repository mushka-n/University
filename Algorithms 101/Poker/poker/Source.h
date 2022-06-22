#pragma warning (disable: 4430 4)
int * Tables_Num_And_Table_Players_Num(int players_num);
int * Create_And_Shuffle_Deck();
struct hand * Distribute_Cards_To_Hands(int players_num, int * deck);
void Read_Card(int card);
int* Dealers_Cards(int* deck);
void Result(struct hand* players);
