//Имя грамматики
grammar nevermorecompiler;

//Программа состоит из 0 или более операторов (Parser Rule)
prog: (globalStatement?  (functionStatement)*) EOF ;


// Доступные операторы
stat
    :assignmentStatement
    |printState
    |ifStatement
    |ifElseStatement
    |forStatement
    |whileStatement
    |doWhileStatement
    |globalStatement
    |functionStatement
    |functionCall
    |NEWLINE
    ;

//Оператор "если" (Parser Rule)
ifStatement: 'if' equation RCORNER ifBody LCORNER END_STATE;
//Оператор "если-иначе"(Parser Rule)
ifElseStatement: 'if' equation RCORNER ifBody LCORNER 'else' RCORNER elseBody LCORNER END_STATE;
//оператор для отслеживания тела "если" и "если-иначе"(Parser Rule)
ifBody:  (stat)* ;
//Оператор отслеживания тела иначе в "если" и "если-иначе"(Parser Rule)
elseBody: (stat)* ;
//Оператор цикла "for"(Parser Rule)
forStatement: 'for' LPAREN forInit equation END_STATE forModify RPAREN RCORNER forBody LCORNER;
//Оператор отслеживания увелечения цикла(Parser Rule)
forModify: ID INCREMENT;
//Оператор отслеживания инициализации цикла "фор"(Parser Rule)
forInit: type ID EQ expr END_STATE;
//Оператор отслеживания тела цикла "фор"(Parser Rule)
forBody: (stat)*;
//Оператор цикла "пока"(Parser Rule)
whileStatement: 'while' LPAREN equation RPAREN RCORNER  whileBody LCORNER END_STATE;
//Оператор цикла "делать пока"(Parser Rule)
doWhileStatement: 'do' RCORNER whileBody LCORNER 'while' LPAREN equation RPAREN END_STATE;
//Оператор отслеживания тела цикла "пока" и "делать-пока"(Parser Rule)
whileBody: (stat)*;

// Выражение может быть арифметическим выражением, целым числом, или идентификатором.(Parser Rule)
expr
    : expr (MUL | DIV) expr
    | expr (ADD | SUB) expr
    |INT
    |ID
    |DOUBLE
    ;
//Оператор вывода(Parser Rule)
printState
    :'print' LPAREN printBody RPAREN END_STATE
    ;
//Оператор для отслеживания наполнения оператора "вывод"(Parser Rule)
printBody: ID
    | INT
    | DOUBLE
    ;
//Оператор создания глобальных переменных(Parser Rule)
globalStatement
    : 'global:' (globalBody)* END_STATE
    ;
//Оператор отслеживания тела "глобал"(Parser Rule)
globalBody: type ':' ID;
//Уравнение условного оператора(Parser Rule)
equation
   : expr op=relop expr
   ;
//Операторы сравнения(Parser Rule)
relop
   : EQ_EQ
   | GT
   | LT
   | NOT_EQ
   ;
//Оператор присваивания(Parser Rule)
assignmentStatement: type ID EQ expr END_STATE;
//Типы данных переменных(Parser Rule)
type
    : 'int'
    | 'double'
    ;

functionStatement
   : funcType functionName LPAREN RPAREN RCORNER functionBody LCORNER END_STATE
   ;

functionBody: (stat)*;

functionName: ID;

funcType: type
   | 'void'
   ;
functionCall
    :'call' 'void' functionName LPAREN RPAREN END_STATE;

// Идентификатор (начинается с буквы, может содержать буквы и цифры)(Lexer Token)
ID: LETTER DIGIT*;
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Zа-яА-Я]+;

// Целое число(Lexer Token)
INT: DIGIT+;

// Вещественное число(Lexer Token)
DOUBLE: INT '.' INT;

// Завершающая точка с запятой(Lexer Token)
END_STATE: ';';

// Арифметические операторы(Lexer Token)
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

// Скобки(Lexer Token)
LPAREN: '(';
RPAREN: ')';

// Операторы сравнения(Lexer Token)
GT: '>';
LT: '<';
EQ_EQ: '==';
NOT_EQ: '!=';

// Левая и правая фигурные скобки(Lexer Token)
RCORNER: '{';
LCORNER: '}';

// Оператор инкремента(Lexer Token)
INCREMENT: ADD ADD;

// Оператор присваивания(Lexer Token)
EQ: '=';

// Пробельные символы (пробел, табуляция, новая строка)(Lexer Token)
WS: [ \n\t\r] -> skip;


//Новая линия(Lexer Token)
NEWLINE:'\r'? '\n' ;