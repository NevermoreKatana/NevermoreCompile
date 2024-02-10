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





expr
    : expr op=(DIV | MUL | ADD | SUB) expr
    |INT
    |ID
    |DOUBLE
    |STROKE
    ;

printState
    :'print' LPAREN (expr | DIGIT | STROKE) RPAREN END_STATE
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
    | 'string'
    | 'bool'
    ;


ID: LETTER DIGIT*;
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Zа-яА-Я]+;
INT: DIGIT+ ;
DOUBLE: INT '.' INT;
STROKE: '"'LETTER +'"';
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

