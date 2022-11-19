#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>
#include <sys/time.h> 
#include <ncurses.h> 
#include <stdio.h>

#define BABY_SNAKE 2
#define INIT_SPEED 220

/*Linked List for the Snake pieces, last piece will have nextPiece = NULL*/
typedef struct snakePiece{
    int x;
    int y;
    struct snakePiece* nextPiece;
}snakePiece;

/*Global Variables*/
int xDir; 
int yDir;
snakePiece *head, *self, *tail; //snake pointers
int trophyX, trophyY = 0; //trophy values for the x, y coordinates
bool collectedTrophy = true;
time_t elapsed;
int growNum = 0;
bool runGame = true; //game stops if there is collision with: borders, snake, or if its reversed
int perimeter;
int snakeCount = 0;
int speed = INIT_SPEED;

/*Declare Function Prototypes*/
void menu();
void drawBorders();
void moveSnake();
void snakeCollision();
void makeTrophies();
void collectTrophies();
void grow();
void timeChecker();
int set_ticker(int);
void deleteList();
void win();


int main(){ 

    menu(); //print the menu for the user

    int input; //initialize user input
    elapsed = time(NULL) + 1;
    srand(time(0));
    int randomDir = rand() % 3 + 1; //initialize random direction for the snake

    //switch statement that decides the direction the snake will start on
    //left isn't handled to avoid a bug collision
    switch(randomDir){
        case 1: //right
            xDir = 1;
            yDir = 0;
            break;
        case 2: //up
            xDir = 0;
            yDir = -1;
            break;
        case 3: //down
            xDir = 0;
            yDir = 1;
            break;
    }

    head = (snakePiece*)malloc(sizeof(snakePiece)); //allocating snake into memory
    
    head->x = 15; //snake's head coordinate on the x-axis
    head->y = 15; //snake's head coordinate on the y-axis
    
    snakePiece *tempPiece = head; //initialize snake 

    //for loop to create the snake, the length will be 3 
    for(int i = 0; i < BABY_SNAKE; i++){ 
        curs_set(0); //making cursor invisible              
        snakePiece *p = (snakePiece*)malloc(sizeof(snakePiece)); //allocating snake into memory
        tempPiece->nextPiece = p;
        p->x = (tempPiece->x) - 1;
        p->y = tempPiece->y;
        snakeCount++;
        tempPiece = p;
    }

    tempPiece->nextPiece = NULL; //tail->next is NULL
    tail = tempPiece;
    
    void moveSnake(int); 
    signal(SIGALRM, moveSnake); //handling signal for snake to move
    signal(SIGINT, SIG_IGN);
    set_ticker(speed);
    initscr(); //initializing screen
    crmode();
    noecho();
    curs_set(0); //making cursor invisible  
    cbreak(); //in this mode, characters typed by the user are immediately available to the program, and erase/kill character-processing is not performed
    nodelay(stdscr, true); //causes getch() to be a non-blocking call, if no input is ready, getch() returns ERR
    keypad(stdscr, true);
    perimeter = (LINES-1) + (COLS-1);
   
   //while the snake game is running, get the user's keyboard input
    while(1){ 

        input = getch(); //getting user input from the keyboard

        //switch statement to check whether the user is pressing left, right, up, or down on the keyboard
        switch(input){
            case KEY_LEFT:
                xDir = -1;
                yDir = 0;
                set_ticker(speed);                
                break;
            case KEY_RIGHT:
                xDir = 1;
                yDir = 0;
                set_ticker(speed);
                break;
            case KEY_UP:
                xDir = 0;
                yDir = -1;
                set_ticker(speed);
                break;
            case KEY_DOWN:
                xDir = 0;
                yDir = 1;
                set_ticker(speed);
                break;   
        }
    }
    
//end of main function
}

/*Author: Sully Lugo
Method for interacting main menu screen at the beginning of the game.
-User can select to begin the game
-User can select to view the rules on a different screen and return to main menu
-User can quit the game using CTRL + C*/
void menu()
{
    int choice, choice2; //initializing variables that store the user's choice

    //printing the name of the game
    printf("\n\n\t\t\t\tWELCOME TO THE\n\n");
    
    puts(
        "\t\t(  ____ \\( (    /|(  ___  )| \\    /\\(  ____ \\ \n"
        "\t\t| (    \\/|  \\  ( || (   ) ||  \\  / /| (    \\/ \n"
        "\t\t| (_____ |   \\ | || (___) ||  (_/ / | (_      \n"
        "\t\t(_____  )| (\\ \\) ||  ___  ||   _ (  |  __)    \n"
        "\t\t      ) || | \\   || (   ) ||  ( \\ \\ | (      \n"
        "\t\t/\\____) || )  \\  || )   ( ||  /  \\ \\| (____/\\ \n"
        "\t\t\\_______)|/    )_)|/     \\||_/    \\/(_______/ \n"
        "\n"
        "\t\t       (  ____ \\(  ___  )(       )(  ____ \\ \n"
        "\t\t       | (    \\/| (   ) || () () || (    \\/ \n"
        "\t\t       | |      | (___) || || || || (_ \n"
        "\t\t       | | ____ |  ___  || |(_)| ||  __)  \n"
        "\t\t       | | \\_  )| (   ) || |   | || ( \n"
        "\t\t       | (___) || )   ( || )   ( || (____/\\ \n"
        "\t\t       (_______)|/     \\||/     \\|(_______/\n\n\n"

    );

    //printing choices user can pick from
    printf("Please select a number.\n");
    printf("1) Play Game\n");
    printf("2) Rules\n");
    printf("Quit (Press Ctrl + C)\n\n");
    printf("Game created by Pedro, Nehway, Kiara, Kimberly, and Sully\n");
    scanf("%d", &choice);

    //if the user presses 1, break and go into snake game
    if(choice == 1){
        return;

    //if the user presses 2, show rules of the game
    }else if(choice == 2){

        curs_set(0); //making cursor invisible 
    
    puts(
        "\t\t(  ____ \\( (    /|(  ___  )| \\    /\\(  ____ \\ \n"
        "\t\t| (    \\/|  \\  ( || (   ) ||  \\  / /| (    \\/ \n"
        "\t\t| (_____ |   \\ | || (___) ||  (_/ / | (_      \n"
        "\t\t(_____  )| (\\ \\) ||  ___  ||   _ (  |  __)    \n"
        "\t\t      ) || | \\   || (   ) ||  ( \\ \\ | (      \n"
        "\t\t/\\____) || )  \\  || )   ( ||  /  \\ \\| (____/\\ \n"
        "\t\t\\_______)|/    )_)|/     \\||_/    \\/(_______/ \n"
        "\n"
        "\t\t       (  ____ \\(  ___  )(       )(  ____ \\ \n"
        "\t\t       | (    \\/| (   ) || () () || (    \\/ \n"
        "\t\t       | |      | (___) || || || || (_ \n"
        "\t\t       | | ____ |  ___  || |(_)| ||  __)  \n"
        "\t\t       | | \\_  )| (   ) || |   | || ( \n"
        "\t\t       | (___) || )   ( || )   ( || (____/\\ \n"
        "\t\t       (_______)|/     \\||/     \\|(_______/"

    );

    //printing rules of the game for the user
    printf("RULES OF THE GAME:\n\n\n");
    printf("\tThe snake is hungry! Use the arrow keys to guide the snake to it's next meal.\n");
    printf("\tEat all of the trophies without crashing into the borders or reversing.\n");
    printf("\tThe size of your snake is in the top left corner.\n\n\n");
    printf("Press 1 to return to the MAIN MENU.\n");
    printf("Press CTRL+C to return to QUIT THE GAME.\n");
    printf("Press any other number to BEGIN THE GAME.\n");
    scanf("%d", &choice2);

    //if the user presses 1, it will go back to the main menu 
    if(choice2 == 1){
        menu();
    }

    //if the user presses anything but 1, it will print out an error
    else{
        return;
    }
   } 

//end of menu function
}


/*Function to draw the borders of the snake pit.
Author: Kiara Azarigian
*/
void drawBorders(){

  //for loop that draws the top line of the pit
   for(int i = 0; i < COLS-1; i++){ 
        move(0,i);
        addstr("x");
        move(LINES-1, i);
        addstr("x");
    }

    //for loop that draws the left line of the pit
    for(int i = 0; i < LINES; i++){ 
        move(i,0);
        addstr("x");
        move(i,COLS-1);
        addstr("x");
    }

    mvprintw(0,0, "%d", snakeCount+1);

//end of drawBorders function
}


/*Function to handle the movement of the snake.
Author: Pedro
*/
void moveSnake(int signum){

    curs_set(0); //making cursor invisible
    signal(SIGALRM, moveSnake);
    erase(); //clear screen
    drawBorders(); //redraw borders   
     
    snakeCollision(); //check for collision

    timeChecker(&collectedTrophy); //check whether the trophy expired
    makeTrophies(&trophyX, &trophyY, &collectedTrophy); //make trophies
    collectTrophies(trophyX, trophyY, &collectedTrophy); //collect trophies
    
    win(); //check if the user won
    
    int xTemp = head->x;
    int yTemp = head->y;

    head->x = xTemp + xDir;
    head->y = yTemp + yDir;

    //if the game is not running, exit
    if(!runGame){
        deleteList();
        endwin(); //turn off curses and reset
        exit(1);
    }

    mvaddch(head->y, head->x, '@'); //printing the head of the snake
    int xCurr, yCurr;
    snakePiece*currPiece = head->nextPiece;
    
    while(currPiece != NULL){                               //Check that node is not tail
        xCurr = currPiece->x;                               //Save current x
        yCurr = currPiece->y;                               //Save current y
        currPiece->x = xTemp;                               //Set current x to previous x
        currPiece->y = yTemp;                               //Set current y to previous y
        mvaddch(yTemp, xTemp, '#');
        xTemp = xCurr;                                      //Save current x for next iteration
        yTemp = yCurr;                                      //Save current y for next iteration
        currPiece = currPiece->nextPiece;                   //Go to next node
    }

    refresh(); //update screen

 //end of moveSnake function
}


/*Author: Kimberly Aviles
Function to handle the snake's collision against border or itself, if it detects collision, it terminates the game.*/
void snakeCollision(){
 
    start_color(); 
    init_pair(1,COLOR_WHITE, COLOR_RED);

    self = head->nextPiece; //self (refering to the snake pieces) will check if the heads next is hitting itself (snake)

    //while self isn't empty
    while(self != NULL){

        //check if self is colliding against x, y or head, if it is end the game
        if(self->x == head->x && self->y == head->y){
            clear(); //clears screen
            drawBorders(); //draw borders
            move(10,20); //move to row10, col20
            attron(COLOR_PAIR(1));
            addstr("SELF COLLISION! YOU LOST THE GAME."); //print to the user that the snake collided against itself
            attroff(COLOR_PAIR(1));
            refresh(); //update the screen
            sleep(2); //adding delay
            runGame = false; //means end the game
            
        }
        //check if head is at the border's position (touching it at the x, y coordinate), if it is end the game
        else if((head->x >= (COLS-1) || head->x <= 0) || (head->y >= (LINES-1)|| head->y <=0)){
            clear(); //clears screen
            drawBorders(); //draw borders
            move(10,20); //move to row10, col20
            attron(COLOR_PAIR(1));
            addstr("BORDER COLLISION! YOU LOST THE GAME."); //print to the user that the snake collided against the border
            attroff(COLOR_PAIR(1));
            refresh(); //update the screen
            sleep(2); //adding delay
            runGame = false; //means end the game
        }

        self = self->nextPiece; //iterate for every snake piece
    }

//end of snakeCollision function
} 


/*Author: Nehway Sahn
Function to implement the trophies.*/
void makeTrophies(int *trophyX, int *trophyY, bool *collectedTrophy){
    
    srand(time(0)); 
    int upper, lower; //initializing upper and lower bounds
    char *num; //initializing a char pointer

    if(*collectedTrophy == true){ 

        if(head->x + 10 < COLS-2 && head->x - 10 > 2){
            upper = head->x + 10;
            lower = head->x - 10;
            }
        else{
            upper = COLS-2;
            lower = 2;
        }
        *trophyX = (rand() %(upper - lower + 1)) + lower;
              
        if(head->y + 10 < LINES-2 && head->y - 10 > 2){
            upper = head->y + 10;
            lower = head->y - 10;
        }               
        else{
            upper = LINES-2; 
            lower =  2;
        }
        *trophyY = (rand() %(upper - lower + 1)) + lower; 

        growNum = rand() % 9 + 1; //creating a random number from 1 to 9
        *collectedTrophy = false;
    }
            
    mvprintw(*trophyY, *trophyX, "%d", growNum); //printing the trophy on the snake pit

//end of makeTrophies
}


/*Function that handles the collection of the trophies by the snake.
Author: Nehway Sahn
*/
void collectTrophies(int trophyX, int trophyY, bool *collectedTrophy){

        //if the snake's head at the x, y coordinate passes over the trophy at the x, y coordinate
        //the snake collected the trophy, set it to true
        if(trophyY == head->y && trophyX == head->x){
            *collectedTrophy = true;
            grow(); //calling grow function to update the snake's length and speed proportionally to the amount of trophies it has collected

    }

//end of collectTrophies function
}

/*Function to handle the snake's speed and length based on the trophies it has.
Author: Pedro 
*/
void grow(){

    snakePiece *tempPiece = tail;

    for(int i = 0; i < growNum; i++){

        snakePiece *p = (snakePiece*)malloc(sizeof(snakePiece));
        tempPiece->nextPiece = p;
        p->x = (tempPiece->x) + xDir;
        p->y = tempPiece->y + yDir;
        snakeCount++;
        tempPiece = p;
    }

    tempPiece->nextPiece = NULL; //tail->next is NULL
    tail = tempPiece;

    //update the speed
    if(speed > 20){
        speed = INIT_SPEED - 50;
        set_ticker(speed);
    }

}


/*Function that checks time on the trophy. 
It will set collectedTrophy to true when time is up, so
the makeTrophy function will make a new trophy.
Author: Kiara Azarigian
*/
void timeChecker(bool *collectedTrophy){

    time_t currentTime = time(NULL);

    //elapsed is currentTime + 1
    if(currentTime == elapsed){ 
        growNum--;
        elapsed++;
    }

    if(growNum == 0){
        *collectedTrophy = true;
    }

//end of timeChecker function
}


/*Function that handles intervals of time.*/
int set_ticker(int n_msecs){
    
    struct itimerval new_timeset;
    long n_sec, n_usecs;

    n_sec = n_msecs / 1000; //int part
    n_usecs = (n_msecs % 1000)*1000L; //remainder

    new_timeset.it_interval.tv_sec = n_sec; //set reload
    new_timeset.it_interval.tv_usec = n_usecs; //new ticker value
    new_timeset.it_value.tv_sec = n_sec; //store it
    new_timeset.it_value.tv_usec = n_usecs; //store it

    return setitimer(ITIMER_REAL, &new_timeset, NULL);

//end of set_ticker function
}


void deleteList(){

   struct snakePiece* current = head;
   struct snakePiece* next;
 
   while (current != NULL){
       next = current->nextPiece;
       free(current);
       current = next;
   }
 
   head =  NULL;

//end of deleteList function
}


/*Author: Kiara Azarigian
Function that checks length of snake and if it has reached the winning length, 
it will display a message and terminate the game.*/
void win(){

    //if the snake pieces are greater or equal to the half of the pit, user wins
    if(snakeCount >= (perimeter/2)){
        clear(); //clear screen
        drawBorders(); //draw borders
        move(10,20); //move to row10, col20
        start_color(); 
        init_pair(1,COLOR_WHITE, COLOR_YELLOW);
        attron(COLOR_PAIR(1));
        addstr("WINNER WINER WINNER"); //printing to the user they won
        attroff(COLOR_PAIR(1));
        refresh(); //update the screen
        sleep(2); //add delay
        runGame = false; //means end the game
    }

//end of win function
}