def ok():
    print("""
    
a) LEX___

%{
#include<stdio.h>
int v=0,op=0,id=0,flag=0;
%}
%%
[a-zA-Z]+[0-9A-Za-z]* {id++;printf("\n Identifier:");ECHO;}
[\+\-\*\/\=] {op++;printf("\n Operartor:");ECHO;}
"(" {v++;}
")" {v--;}
";" {flag=1;}
.|\n {;}
%%
int main(){
printf("\n Enter the expression \n");
yylex();
if((op+1)==id&&v==0&&flag==0)
printf("\n Expression is Valid\n");
else printf("\n Expression is Invalid\n");
printf("\n The number of identifiers are: %d \nThe number of operators are: %d \n",id,op);
int yywrap(){
return 1;
}
}


b) YACC___

%{
#include"y.tab.h"
extern yylval;
%}
%%
[0-9]+ {yylval=atoi(yytext);return num;}
[\+\-\*\/] {return yytext[0];}
[)] {return yytext [0];}
[(] {return yytext[0];}
. {;}
\n {return 0;}
%%

%{
#include<stdio.h>
#include<stdlib.h>
%}
%token num
%left '+' '-'
%left '*' '/'
%%
input:exp {printf("%d\n",$$);exit(0);}
exp:exp'+'exp {$$=$1+$3;}
| exp'-'exp {$$=$1-$3;}
| exp'*'exp {$$=$1*$3;}
| exp'/'exp {if($3==0) {printf("divide by zero\n");exit(0);}
		  else
		  $$=$1/$3;}
| '('exp')' {$$=$2;}
| num {$$=$1;}
%%
int main()
{
printf("\n Enter an expression:\n");
yyparse();
}
int yyerror()
{
printf("\n error");
exit(0);
}

    """)