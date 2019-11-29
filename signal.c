#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int tmps = 20;

void gest(int sig){
	if(tmps == 0) {
		printf("temps écoulé ! \n");
		fflush(stdout);
		exit(1);
	}
	else {
		printf("Il reste %d secondes \n", tmps);
		fflush(stdout);
		tmps--;
		alarm(1);
	}
}


int main() {
	signal(SIGALRM, gest);
	alarm(1);


	getchar();
}
