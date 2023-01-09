grammar MLTLM;
// Grammar Rules
program
  : statement* EOF
  ;
 
// The part (Identifier ':')? is an optional argument to name a formula
statement
  : (Identifier ':')? expr ';' 
  | contract ';'
  | binding ';'
  | mapping ';'
  ;

// What is this doing? a0:G[0,1]a1 => a4;
contract
  : (Identifier ':')? expr '=>' expr
  ;

expr
  : UnaryOperators '[' Number  ',' Identifier  ']' expr                 # unary_expr
	| UnaryOperators '[' Number ',' Number ',' Identifier  ']' expr       # unary_expr
	| expr BinaryOperators '[' Number ',' Identifier ']' expr             # binary_expr
	| expr BinaryOperators '[' Number ',' Number ',' Identifier ']' expr  # binary_expr
	| op = '!' expr # unary_expr
  | expr op='&' expr    # binary_expr
	| expr op = '|' expr # binary_expr
	| expr op = '<->' expr # binary_expr
	| expr op = '->' expr # binary_expr
  | '(' expr ')' # parens_expr
  | Identifier   # atom_expr
  | 'TRUE'       # bool_expr
  | 'FALSE'      # bool_expr
  ;

binding
  : Identifier ':=' Filter '(' Identifier ')' Conditional Number
  | Identifier ':=' Filter '(' Identifier ',' Number ')' Conditional Number
  ;

mapping
  : Identifier ':=' Number
  ;

// Lexical Spec

Filter
  : 'bool'
  | 'int'
  | 'float'
  | 'rate'
  | 'movavg'
  | 'abs_diff_angle'
  ;

Conditional : [!=><] '='? ;


UnaryOperators : 'G'
          | 'F'
	        | 'O'
	        | 'H';


BinaryOperators:'U'
          | 'R'
          | 'Y'
          | 'S';
          
// GLOBALLY     : 'G' ;
// FINALLY      : 'F' ;
// UNTIL        : 'U' ;
// RELEASE      : 'R' ;
// YESTERDAY    : 'Y' ;
// SINCE        : 'S' ;
// ONCE         : 'O' ;
// HISTORICALLY : 'H' ;

Identifier
  : Letter (Letter | Digit)*
  ;

Number
  : Integer
  | Float
  ;

fragment
Integer
  : Sign? NonzeroDigit Digit*
  | '0'
  ;

fragment
Float
  : Sign? Digit+ '.' Digit+
  ;

fragment
Sign
  : [+-]
  ;

fragment
Digit
  :  [0-9]
  ;

fragment
NonzeroDigit
  : [1-9]
  ;

fragment
Letter
  : [a-zA-Z_]
  ;

Comment : '#' ~[\r\n]* -> skip;
WS  :  [ \t\r\n]+ -> skip;
