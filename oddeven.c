#include <stdio.h>
#include<string.h>
int main(void) {
	char s[25];
	int i;
	scanf("%s",s);

	for(i=0;i<strlen(s);i=i+2){
	    char temp=s[i];
	    s[i]=s[i+1];
	    s[i+1]=temp;
	}
	printf("%s",s);
}

