grammar nevermorecompiler;

prog: stat* ;

stat
    :assignmentStatement
    |printState
    |ifStatement
    |ifElseStatement
    |forStatement
    |whileStatement
    |doWhileStatement
//    | functionStatement
    |NEWLINE
    ;

ifStatement: 'if' equation RCORNER ifBody LCORNER END_STATE;

ifElseStatement: 'if' equation RCORNER ifBody LCORNER 'else' RCORNER elseBody LCORNER END_STATE;

ifBody:  (stat)* ;

elseBody: (stat)* ;

forStatement: 'for' LPAREN forInit equation END_STATE forModify RPAREN RCORNER forBody LCORNER;

forModify: ID INCREMENT;
forInit: type ID EQ expr END_STATE;
forBody: (stat)*;

whileStatement: 'while' LPAREN equation RPAREN RCORNER  whileBody LCORNER END_STATE;

doWhileStatement: 'do' RCORNER whileBody LCORNER 'while' LPAREN equation RPAREN END_STATE;

whileBody: (stat)*;

//functionStatement
//    : funcType functionName LPAREN RPAREN RCORNER functionBody LCORNER END_STATE
//    ;
//
//functionBody: (stat)*;
//
//functionName: ID;
//
//funcType: type
//    | 'void'
//    ;

expr
    : expr (MUL | DIV) expr
    | expr (ADD | SUB) expr
    |INT
    |ID
    |DOUBLE
    ;

printState
    :'print' LPAREN (expr | DIGIT ) RPAREN END_STATE
    ;


equation
   : expr op=relop expr
   ;

relop
   : EQ_EQ
   | GT
   | LT
   | NOT_EQ
   ;


assignmentStatement: type ID EQ expr END_STATE;

type
    : 'int'
    | 'double'
    ;


ID: LETTER DIGIT*;
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Zа-яА-Я]+;
INT: DIGIT+ ;
DOUBLE: INT '.' INT;
END_STATE:';';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
GT: '>';
LT: '<';
EQ_EQ: '==';
NOT_EQ: '!=';
RCORNER: '{';
LCORNER: '}';


INCREMENT: ADD ADD;

EQ: '=';

WS
    : [ \n\t\r] -> skip
    ;
NEWLINE:'\r'? '\n' ;

