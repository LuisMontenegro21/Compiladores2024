grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   IF expr THEN block END NEWLINE # ifStat
    |   WHILE expr DO block END NEWLINE # whileStat
    |   FUNCTION ID '(' ')' block END NEWLINE # funcDef
    |   NEWLINE                      # blank
    ;

block: stat+ ; 

expr:   expr ('*'|'/') expr          # MulDiv
    |   expr ('+'|'-') expr          # AddSub
    |   expr ('==' | '!=') expr      # comparison
    |   INT                          # int
    |   ID                           # id
    |   '(' expr ')'                 # parens
    ;

MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction
EQ : '==' ; // define token for equality
NEQ : '!=' ; // define token for inequality
ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace
COMMENT : '//' ~[\r\n]* -> skip ; // skip comments with //
IF : 'if' ;
THEN : 'then' ;
WHILE : 'while' ;
DO : 'do' ;
END : 'end' ;
FUNCTION : 'function' ;