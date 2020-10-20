//Student ID: 1814220
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
	    str = result.text
	    escSeq = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
	    if str in escSeq:        
            raise UncloseString(str[1:-1])
	    else:
	        raise UncloseString(str[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape((result.text)[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : (var_declare | func_declare)* EOF ;

//------Variable Declaration------

var_declare: VAR COLON varList SEMI ;

varList: variable (COMMA variable)* ;

variable: ID ASSIGNMENT (INTLIT | FLOATLIT | STRINGLIT | BOOLLIT)
	    | ID (LS INTLIT RS)+ ASSIGNMENT ARRAYLIT 
		| ID ;

//------Function Declaration

func_declare: FUNCTION COLON ID (PARAMETER COLON paramList)? BODY COLON var_declare* statement* ENDBODY DOT ;

paramList: ID (COMMA ID)* ;

statement: assign_stmt 
		 | if_stmt
		 | for_stmt | while_stmt | doWhile_stmt 
		 | break_stmt
		 | continue_stmt
		 | call_stmt
		 | return_stmt;

//------Expression------

assign_stmt: (ID | ID (LS INTLIT RS)+ | exp0) ASSIGNMENT exp0 SEMI;

exp0: exp1 rela_op exp1 | exp1 ;
exp1: exp1 logic_op exp2 | exp2 ;
exp2: exp2 add_op exp3 | exp3 ;
exp3: exp3 mul_op exp4 | exp4 ;
exp4: not_op exp4 | exp5 ;
exp5: dec_op exp5 | exp6 ;
exp6: exp6 index_op | exp7 ;
exp7: func_call | exp8 ;
exp8: LP exp0 RP | ID | INTLIT | FLOATLIT | BOOLLIT ;

rela_op: EQ | NEQ | GT | LT | GTE | LTE | NEQFLOAT | GTFLOAT | LTFLOAT | GTEFLOAT | LTEFLOAT ;

logic_op: AND | OR ;

add_op: ADDINT | ADDFLOAT | SUBINT | SUBFLOAT ;

mul_op: MULINT | MULFLOAT | DIVINT | DIVFLOAT | MOD ;

not_op: EP ;

dec_op: SUBINT | SUBFLOAT ;

index_op: (LS expression RS)+ ; 

//------Expression For Index operator------

expression: addexpr ;
addexpr: addexpr (ADDINT | SUBINT | MULINT | DIVINT | MOD) funcexpr | funcexpr ;
funcexpr: func_call | openrands ;
openrands: LP expression RP | ID | INTLIT | ID (LS INTLIT RS)+ ; 

//------Statements------

func_call: ID LP argumentList RP ;

if_stmt: IF exp0+ THEN statement* (elseIf_stmt)* (ELSE statement*)? ENDIF DOT ;

elseIf_stmt: ELSEIF exp0 THEN statement* ;

// statementList: statement* ;

for_stmt: FOR LP ((ID | ID (LS INTLIT RS)+) ASSIGNMENT exp0) COMMA exp0 COMMA exp0 RP DO statement* ENDFOR DOT ;

while_stmt: WHILE exp0 DO statement* ENDWHILE DOT ;

doWhile_stmt: DO statement* WHILE exp0 ENDDO DOT ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI ;

call_stmt: ID LP argumentList RP SEMI ;

argumentList: (argument (COMMA argument)*)* ;

argument: ID | exp0 ;

return_stmt: RETURN (exp0 | STRINGLIT)? SEMI ;

//------Identifiers------

ID: [a-z][A-Za-z_0-9]* ;

//------Keywords------

VAR: 'Var' ;

BODY: 'Body' ;

BREAK: 'Break' ;

CONTINUE: 'Continue' ;

DO: 'Do' ;

ELSE: 'Else' ;

ELSEIF: 'ElseIf' ;

ENDBODY: 'EndBody' ;

ENDIF: 'EndIf' ;

ENDFOR: 'EndFor' ;

ENDWHILE: 'EndWhile' ;

FOR: 'For' ;

FUNCTION: 'Function' ;

IF: 'If' ;

PARAMETER: 'Parameter' ;

RETURN: 'Return' ;

THEN: 'Then' ;

WHILE: 'While' ;

ENDDO: 'EndDo' ;

//------Separators------

LB: '{' ;

RB: '}' ;

LP: '(' ;

RP: ')' ;

LS: '[' ;

RS: ']' ;

SEMI: ';' ;

COLON: ':' ;

COMMA: ',' ;

DOT: '.' ;

//------Arithmetic Operators------

ADDINT: '+' ;

SUBINT: '-' ;

MULINT: '*' ;

DIVINT: '\\' ;

MOD: '%' ;

ADDFLOAT: '+.' ;

SUBFLOAT: '-.' ;

MULFLOAT: '*.' ;

DIVFLOAT: '\\.' ;

EP: '!' ;

AND: '&&' ;

OR: '||' ;

//------Relational Operator------

ASSIGNMENT: '=' ;

EQ: '==' ;

NEQ: '!=' ;

GT: '>' ;

LT: '<' ;

GTE: '>=' ;

LTE: '<=' ;

NEQFLOAT: '=/=' ;

GTFLOAT: '>.' ;

LTFLOAT: '<.' ;

GTEFLOAT: '>=.' ;

LTEFLOAT: '<=.' ;

//------Literals------

fragment Hex: [xX][1-9A-F][0-9A-F]* ;

fragment Oct: [oO][1-7][0-7]* ;

INTLIT: [1-9][0-9]* 
	  | [0] Hex
	  | [0] Oct
	  | [0];

fragment Exponent: [eE] SUBINT? [0-9]+ ;

fragment Digit: [0-9] ;

FLOATLIT: (([1-9][0-9]*)+ | [0]) DOT Digit* Exponent
        | (([1-9][0-9]*)+ | [0]) DOT Digit* 
		| ([1-9][0-9]*)+ Exponent
		| (([1-9][0-9]*) | [0]) DOT ;

BOOLLIT: 'True' | 'False' ;

fragment Characters: ~[\b\f\r\n\t"'\\] | Esc_Seq ;

fragment Esc_Seq: '\\' [bfrnt'\\] | ['] '"' ;

fragment Illegal_esc: '\\' ~[bfrnt'\\] ;

STRINGLIT: '"' Characters* '"' 
	{
		text = str(self.text)
		self.text = text[1:-1]
	};

ARRAYLIT: LB ARRAY (COMMA ARRAY)* RB | ARRAY ;

ARRAY: LB (INTLIT (COMMA INTLIT)*)* RB
	 | LB (FLOATLIT (COMMA FLOATLIT)*)* RB 
	 | LB (STRINGLIT (COMMA STRINGLIT)*)* RB
	 | LB (BOOLLIT (COMMA BOOLLIT)*)* RB;

//------Comment------

BLOCK_COMMENT: '**' .*? '**' -> skip ;
	
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: '"' Characters* ~["] ;
ILLEGAL_ESCAPE: '"' Characters* Illegal_esc;
UNTERMINATED_COMMENT: '**' .*? ;