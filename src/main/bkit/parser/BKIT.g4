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

func_declare: FUNCTION COLON ID PARAMETER COLON paramList BODY COLON statement* ENDBODY DOT ;

paramList: ID (COMMA ID)* ;

statement: var_declare
         | assign_stmt 
		 | if_stmt
		 | for_stmt 
		 | while_stmt 
		 | doWhile_stmt 
		 | break_stmt
		 | continue_stmt
		 | call_stmt
		 | return_stmt;

//------Expression------

assign_stmt: (ID | ID (LS INTLIT RS)+) ASSIGNMENT exp0 SEMI;

exp0: exp1 rela_op exp1 | exp1 ;
exp1: exp1 logic_op exp2 | exp2 ;
exp2: exp2 add_op exp3 | exp3 ;
exp3: exp3 mul_op exp4 | exp4 ;
exp4: not_op exp4 | exp5 ;
exp5: dec_op exp5 | exp6 ;
exp6: exp6 index_op | exp7 ;
exp7: exp8 func_call exp8 | exp8 ;
exp8: LP exp0 RP | ID | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT ;

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
funcexpr: openrands func_call openrands | openrands ;
openrands: LP expression RP | ID | INTLIT ; 

//------Statements------

func_call: ID LP argumentList RP ;

if_stmt: IF exp0 THEN statementList (elseIf_stmt)* (ELSE statementList)? ENDIF DOT ;

elseIf_stmt: ELSEIF exp0 THEN statementList ;

statementList: statement* ;

for_stmt: FOR LP exp0 COMMA exp0 COMMA exp0 RP DO statementList ENDFOR DOT ;

while_stmt: WHILE exp0 DO statementList ENDWHILE DOT ;

doWhile_stmt: DO statementList WHILE exp0 ENDDO DOT ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI ;

call_stmt: ID LP argumentList RP SEMI ;

argumentList: (argument (COMMA argument)*)* ;

argument: ID | exp0 ;

return_stmt: RETURN exp0 SEMI ;

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

TRUE: 'True' ;

FALSE: 'False' ;

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

INTLIT: DECINT | HEXINT | OCTINT;

fragment DECINT: [1-9][0-9]* | [0] ;

fragment HEXINT: [0]([xX][1-9][0-9A-F]*)* ;

fragment OCTINT: [0]([oO][1-7][0-7]*)* ;

fragment Exponent: [eE] SUBINT? [0-9]+ ;

fragment Digit: [0-9] ;

FLOATLIT: Digit+ DOT Digit* Exponent
        | Digit+ (DOT Digit* | Exponent)
		| Digit DOT ;

BOOLLIT: TRUE | FALSE ;

fragment Characters: ~[\b\f\r\n\t"'\\] | Esc_Seq ;

fragment Esc_Seq: '\\' [bfrnt'\\] | ['] '"' ;

fragment Illegal_esc: '\\' ~[bfrnt'\\] ;

STRINGLIT: '"' Characters* '"' 
	{
		text = str(self.text)
		self.text = text[1:-1]
	};

ARRAYLIT: LB ARRAY COMMA ARRAYLIT RB | ARRAY ;

ARRAY: LB (INTLIT | FLOATLIT | STRINGLIT) (COMMA INTLIT | FLOATLIT | STRINGLIT)* RB;

//------Comment------

BLOCK_COMMENT: '**' .*? '**' -> skip ;
	
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: '"' Characters* ~["] ;
ILLEGAL_ESCAPE: '"' Characters* Illegal_esc;
UNTERMINATED_COMMENT: .;