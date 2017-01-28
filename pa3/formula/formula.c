#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "formula.h"
#include "nCr.h"
#include <time.h>
#include <ctype.h>
#include <sys/time.h>

/*
 * Prints the formula (1+x)^n, with the following interface: formula <power>,
 * where power represents n.
 */

int main(int argc, char **argv){

	struct timeval start, end;
	gettimeofday(&start, NULL);
	char * number = malloc(sizeof(argv[1]) * sizeof(argv[1]));
	strcpy(number, argv[1]);

	// Checks for help flag.
	if (strcmp(number, "-h")==0){
		usage();
		gettimeofday(&end, NULL);
		printf("Time required = %ld microseconds.\n", ((end.tv_sec*1000000 + end.tv_usec)-(start.tv_sec*1000000 + start.tv_usec)));
		return 0;
	}

	// Loop ensures that power is a positive integer.
	int i;
	for (i=0; i<strlen(number); i++){
		if(isdigit(number[i])==0){
			printf("ERROR: Invalid character in input: %c\n", number[i]);
			return 0;
		}
	}

	// Power is the int form of the exponent that was stored in argv[1]
	int power;
	power = charDecimalToIntDecimal(number);

	// Error checking for negative exponents
	if (power<0){
		printf("ERROR: Power must be non-negative.\n");
		return 0;
	}

	// Count is originally set to 1, and increases each loop until it's greater than power
	int count = 1, nChooser;
	printf("(1 + x)^%d = 1 + ", power);
	while (count<=power){
		nChooser = nCr(power, count);
		if (count<power){
			printf("%d*x^%d + ", nChooser, count);
		}
		// The last statement, when count==power, is printed without a " + " at the end for neatness.
		else {
			printf("%d*x^%d\n", nChooser, count);
		}
		count++;
	}

	gettimeofday(&end, NULL);
	printf("Time required = %ld microseconds.\n", ((end.tv_sec*1000000 + end.tv_usec)-(start.tv_sec*1000000 + start.tv_usec)));
	return 0;
}
