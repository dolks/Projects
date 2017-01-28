#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * Prints out correct usage interface for executng formula.c.
 */

void usage(){
	printf("Usage: formula <positive integer>\n");
	return;
}

/*
 * Converts a decimal number in a char pointer into a decimal integer. Takes a
 * char pointer as an argument which will then be converted and returned.
 */

int charDecimalToIntDecimal(char * number){

	int result=0, i;

	for (i=0; i<strlen(number); i++){
		result = result * 10 + (number[i]-'0');
	}

	return result;
}
