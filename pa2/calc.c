#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

/*
 * Reverses a given string.
 */

char * reverse(char * str){
	char* string = malloc(sizeof(str) * strlen(str));
	strcpy(string, str);
	int length = strlen(string);
	if (length%2==0){
		int i=0, k=length-1;
		char temp;
		while (i<k){
			temp = string[i];
			string[i]=string[k];
			string[k]=temp;
			i++;
			k--;
		}
	}
	else{
		int i=0, k = length-1;
		char temp;
		while (i!=k){
			temp = string[i];
			string[i]=string[k];
			string[k]=temp;
			i++;
			k--;
		}
	}

	return string;
}

/*
 * Appends a character to a char pointer string. Takes original char pointer
 * and character to be appended as parameters, and returns resulting string.
 */

char * append(char *str, char c){
	char * result = malloc(strlen(str)*sizeof(str) +2); // Adds one byte for new character, another for '\0'.
	strcpy(result, str);

	result[strlen(result)] = c;
	result[strlen(result) + 1] = '\0';

	return result;
}

/*
 * Takes two doubles as parameters; one represents the base number and the
 * other an exponent. The function then computes that base to that exponent.
 */

 double pow(double number, double exponent){
 	int i, originalNum = number;
 	if (exponent==0){
 		return 1;
 	}
 	for (i=1; i<exponent; i++){
 		number = number * originalNum;
 	}

 	return number;
 }

/*
 * Converts a binary number in a char pointer into a decimal integer. Takes a
 * char pointer as an argument which will then be converted and returned.
 */

int charBinaryToIntDecimal(char * number){
	int result=0, i;
	for (i=0; i<strlen(number); i++){
		if (number[i]=='0'){
			result = result<<1;
		}
		else if(number[i]=='1'){
			result = (result<<1) + 1;
		}
		else {
			fprintf(stderr, "ERROR: Not a binary number.");
		}
	}

	return result;
}

/*
 * Converts a hexadecimal number in a char pointer into a decimal integer. Takes a
 * char pointer as an argument which will then be converted and returned.
 */

int charHexToIntDecimal(char * number){
	int result=0, exponent = strlen(number)-1, i;

	for (i=0; i<strlen(number); i++){
		switch(number[i]){
			case '0': {
				result = result + (0 * pow(16, exponent));
				exponent--;} break;
			case '1': {
				result = result + (1 * pow(16, exponent));
				exponent--;} break;
			case '2': {
				result = result + (2 * pow(16, exponent));
				exponent--;} break;
			case '3': {
				result = result + (3 * pow(16, exponent));
				exponent--;} break;
			case '4': {
				result = result + (4 * pow(16, exponent));
				exponent--;} break;
			case '5': {
				result = result + (5 * pow(16, exponent));
				exponent--;} break;
			case '6': {
				result = result + (6 * pow(16, exponent));
				exponent--;} break;
			case '7': {
				result = result + (7 * pow(16, exponent));
				exponent--;} break;
			case '8': {
				result = result + (8 * pow(16, exponent));
				exponent--;} break;
			case '9': {
				result = result + (9 * pow(16, exponent));
				exponent--;} break;
			case 'A': {
				result = result + (10 * pow(16, exponent));
				exponent--;} break;
			case 'B': {
				result = result + (11 * pow(16, exponent));
				exponent--;} break;
			case 'C': {
				result = result + (12 * pow(16, exponent));
				exponent--;} break;
			case 'D': {
				result = result + (13 * pow(16, exponent));
				exponent--;} break;
			case 'E': {
				result = result + (14 * pow(16, exponent));
				exponent--;} break;
			case 'F': {
				result = result + (15 * pow(16, exponent));
				exponent--;} break;
			case 'a': {
				result = result + (10 * pow(16, exponent));
				exponent--;} break;
			case 'b': {
				result = result + (11 * pow(16, exponent));
				exponent--;} break;
			case 'c': {
				result = result + (12 * pow(16, exponent));
				exponent--;} break;
			case 'd': {
				result = result + (13 * pow(16, exponent));
				exponent--;} break;
			case 'e': {
				result = result + (14 * pow(16, exponent));
				exponent--;} break;
			case 'f': {
				result = result + (15 * pow(16, exponent));
				exponent--;} break;
			default: fprintf(stderr, "ERROR: Invalid hex character."); break;
		}
	}
	return result;
}

/*
 * Converts an octal number in a char pointer into a decimal integer. Takes a
 * char pointer as an argument which will then be converted and returned.
 */

int charOctalToIntDecimal(char * number){
	int result=0, exponent = strlen(number)-1, i;

	for (i=0; i<strlen(number); i++){
		switch(number[i]){
			case '0': {
				result = result + (0 * pow(8, exponent));
				exponent--;} break;
			case '1': {
				result = result + (1 * pow(8, exponent));
				exponent--;} break;
			case '2': {
				result = result + (2 * pow(8, exponent));
				exponent--;} break;
			case '3': {
				result = result + (3 * pow(8, exponent));
				exponent--;} break;
			case '4': {
				result = result + (4 * pow(8, exponent));
				exponent--;} break;
			case '5': {
				result = result + (5 * pow(8, exponent));
				exponent--;} break;
			case '6': {
				result = result + (6 * pow(8, exponent));
				exponent--;} break;
			case '7': {
				result = result + (7 * pow(8, exponent));
				exponent--;} break;
			default: fprintf(stderr, "ERROR: Invalid octal character."); break;
		}
	}
	return result;
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

/*
 * Converts a decimal integer into a binary string. Takes an int
 * as an argument which will then be converted and returned.
 */
char *decimalIntToBinaryChar(int number){
	char *output="";
	int temp = number, k;
	while (temp!=0){
		k = temp%2;
		temp = temp/2;
		if (k!=0 && k!=1){
			fprintf(stderr, "ERROR: Impossible value.");
			return NULL;
		}
		else {
			output = append(output, k + '0');
		}
	}
	output = reverse(output);

	return output;
}

/*
 * Converts a decimal integer into a hexadecimal string. Takes an int
 * as an argument which will then be converted and returned.
 */
char *decimalIntToHexChar(int number){
	char *output="";
	int temp = number, k;
	while (temp!=0){
		k = temp%16;
		temp = temp/16;
		if (k>9){
			if (k==10){
				output = append(output, 'A');
			}
			else if (k==11){
				output = append(output, 'B');
			}
			else if(k==12){
				output = append(output, 'C');
			}
			else if(k==13){
				output = append(output, 'D');
			}
			else if(k==14){
				output = append(output, 'E');
			}
			else if(k==15){
				output = append(output, 'F');
			}
			else{
				fprintf(stderr, "ERROR: Impossible value.");
				return NULL;
			}
		}
		else {
			output = append(output, k + '0');
		}
	}

	output = reverse(output);
	return output;
}

/*
 * Converts a decimal integer into an octal string. Takes an int
 * as an argument which will then be converted and returned.
 */
char *decimalIntToOctalChar(int number){
	char *output="";
	int temp = number, k;
	while (temp!=0){
		k = temp%8;
		temp = temp/8;
		if (k>7 && k<0){
			fprintf(stderr, "ERROR: Impossible value.");
			return NULL;
		}
		else {
			output = append(output, k + '0');
		}
	}
	output = reverse(output);
	return output;
}

int main(int argc, char **argv){
	char * num1, *num2, *num1Sign, *num2Sign,
	*operator, *num1Base, *num2Base, *outputBase;

	//Initialization of all variables first.
	operator = malloc(sizeof(argv[1]) * strlen(argv[1]));
	strcpy(operator, argv[1]);

	// Initialzes first number variables.
	num1Sign = malloc(sizeof(argv[2]) * strlen(argv[2]));
	if(argv[2][0]=='-'){
		num1Sign = append(num1Sign, argv[2][0]);
	}
	else{
		num1Sign = append(num1Sign, argv[2][0]);
	}

	num1Base = malloc(sizeof(argv[2]) * strlen(argv[2]));
	if (argv[2][0]=='-'){
		num1Base = append(num1Base, argv[2][1]);
	}
	else{
		num1Base = append(num1Base, argv[2][0]);
	}

	num1 = malloc(sizeof(argv[2]) * strlen(argv[2]));
	num1="";
	int i;
	if (argv[2][0] =='-'){
		for (i=2; i<strlen(argv[2]); i++){
			num1 = append(num1, argv[2][i]);
		}
	}
	else {
		for (i=1; i<strlen(argv[2]); i++){
			num1 = append(num1, argv[2][i]);
		}
	}

	num2Sign = malloc(sizeof(argv[3]) * strlen(argv[3]));
	if(argv[3][0]=='-'){
		num2Sign = append(num2Sign, argv[3][0]);
	}
	else{
		strcpy(num2Sign, "");
	}

	num2Base = malloc(sizeof(argv[3]) * strlen(argv[3]));
	if (argv[3][0]=='-'){
		num2Base = append(num2Base, argv[3][1]);
	}
	else{
		num2Base = append(num2Base, argv[3][0]);
	}

	num2 = malloc(sizeof(argv[3]) * strlen(argv[3]));
	num2="";

	if (argv[3][0] =='-'){
		for (i=2; i<strlen(argv[3]); i++){
			num2 = append(num2, argv[3][i]);
		}
	}
	else {
		for (i=1; i<strlen(argv[3]); i++){
			num2 = append(num2, argv[3][i]);
		}
	}

	outputBase= malloc(sizeof(argv[4]) * strlen(argv[4]));
	strcpy(outputBase, argv[4]);

	int number1, number2;

	// Converts nubers to an integer decimal format for later computing.
	if (num1Base[0]=='b'){
		number1 = charBinaryToIntDecimal(num1);
		if (num1Sign[0]=='-'){
			number1 = (-1*number1); // Changes number to negative.
		}
	}
	else if(num1Base[0]=='d'){
		number1 = charDecimalToIntDecimal(num1);
		if (num1Sign[0]=='-'){
			number1 = (-1*number1); // Changes number to negative.
		}
	}

	else if(num1Base[0]=='o'){
		number1 = charOctalToIntDecimal(num1);
		if (num1Sign[0]=='-'){
			number1 = (-1*number1); // Changes number to negative.
		}
	}

	else if(num1Base[0]=='x'){
		number1 = charHexToIntDecimal(num1);
		if (num1Sign[0]=='-'){
			number1 =(-1*number1); // Changes number to negative.
		}
	}

	else{
		fprintf(stderr, "ERROR: Invalid base type for first number.\n");
		return 0;
	}

	// Conversions for second number.
	if (num2Base[0]=='b'){
		number2 = charBinaryToIntDecimal(num2);
		if (num2Sign[0]=='-'){
			number2 = (-1*number2); // Changes number to negative.
		}
	}
	else if(num2Base[0]=='d'){
		number2 = charDecimalToIntDecimal(num2);
		if (num2Sign[0]=='-'){
			number2 = (-1*number2); // Changes number to negative.
		}
	}

	else if(num2Base[0]=='o'){
		number2 = charOctalToIntDecimal(num2);
		if (num2Sign[0]=='-'){
			number2 = (-1*number2); // Changes number to negative.
		}
	}

	else if(num2Base[0]=='x'){
		number2 = charHexToIntDecimal(num2);
		if (num2Sign[0]=='-'){
			number2 = (-1*number2); // Changes number to negative.
		}
	}

	else{
		fprintf(stderr, "ERROR: Invalid base type for second number.\n");
		return 0;
	}

	// Calculates output in decimal.

	int output;

	if (operator[0]=='+'){
		output = number1 + number2;
	}

	else if (operator[0]=='-'){
		output = number1 - number2;
	}

	else if (operator[0]=='x'){
		output = number1 * number2;
	}
	else{
		fprintf(stderr, "ERROR: Invalid operator.\n");
	}

	// Converts output to correct base.

	if (outputBase[0]=='d'){
		if (output<0){
			output = abs(output);
			printf("-%s%d\n", outputBase, output);
			return 0;
		}
		printf("%s%d\n", outputBase, output);
		return 0;
	}

	else if(outputBase[0]=='b'){
		char *stringOutput = malloc(33);
		if (output<0){
			output = abs(output);
			stringOutput = decimalIntToBinaryChar(output);
			printf("-%s%s\n", outputBase, stringOutput);
			return 0;
		}
		stringOutput = decimalIntToBinaryChar(output);
		printf("%s%s\n", outputBase, stringOutput);
		return 0;
	}

	else if(outputBase[0]=='x'){
		char *stringOutput = malloc(33);
		if (output<0){
			output = abs(output);
			stringOutput = decimalIntToHexChar(output);
			printf("-%s%s\n", outputBase, stringOutput);
			return 0;
		}
		stringOutput = decimalIntToHexChar(output);
		printf("%s%s\n", outputBase, stringOutput);
		return 0;
	}

	else if(outputBase[0]=='o'){
		char *stringOutput = malloc(33);
		if (output<0){
			output = abs(output);
			stringOutput = decimalIntToOctalChar(output);
			printf("-%s%s\n", outputBase, stringOutput);
			return 0;
		}
		stringOutput = decimalIntToOctalChar(output);
		printf("%s%s\n", outputBase, stringOutput);
		return 0;
	}

	else {
		fprintf(stderr, "ERROR: Invalid output base.");
		return 0;
	}
	return 0;
}
