// MSSV: 2112737
// TEN: NGUYEN DUC AN
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

/*------------------------------------------------------------------
 * PARSER RULES 
 ------------------------------------------------------------------*/

program			: NEWLINE* decl_list EOF;
decl_list 		: decl decl_list | decl;
decl			: vars_decl | funs_decl;

// Ignore rule
ignore			: NEWLINE+;

// Variables declaration
vars_decl		: (norm_decl | var_decl | dynamic_decl) ignore; 
norm_decl 		: (scalar_type ID | scalar_type array_type) (ASSIGN exp)?;
var_decl		: VAR ID ASSIGN exp;
dynamic_decl	: DYNAMIC ID (ASSIGN exp)?;

// Function declaration
funs_decl		: FUNC ID LP formal_params RP (ignore? block_stmt | ignore? return_stmt | ignore); 
formal_params 	: formal_pms_prm | ;
formal_pms_prm	: formal_pm COMMA formal_pms_prm | formal_pm;
formal_pm		: scalar_type ID | scalar_type array_type;

// Array
array_type 		: ID LS dim_list RS;
dim_list 		: NUM_LIT COMMA dim_list | NUM_LIT;
array_ele		: (ID | fun_call) LS index_ops RS;

// Statements
stmt			: block_stmt | if_stmt | for_stmt 
				| assign_stmt | continue_stmt | break_stmt
				| return_stmt | (fun_call ignore) | vars_decl;
block_stmt 		: BEGIN ignore stmtlist END ignore;
stmtlist 		: stmtprime | ;
stmtprime		: stmt stmtprime | stmt;
if_stmt			: IF LP exp RP ignore? stmt
				(ELIF LP exp RP ignore? stmt)* (ELSE ignore? stmt)?;  
for_stmt		: FOR ID UNTIL exp BY exp ignore? stmt;
assign_stmt 	: (ID | ID LS index_ops RS) ASSIGN exp ignore;
index_ops		: exp | exp COMMA index_ops;
continue_stmt 	: CONTINUE ignore;
break_stmt 		: BREAK ignore;
return_stmt		: RETURN exp? ignore;

// Function call
fun_call		: ID LP index_ops? RP; //| builtins_call;

// Expressions
exp 		: exp1 CONCAT exp1 | exp1;
exp1		: exp2 (EQ_NUM | EQ_STR | DIFFER | LT | GT | LE | GE) exp2 | exp2;
exp2		: exp2 (AND | OR) exp3 | exp3;
exp3		: exp3 (PLUS | MINUS) exp4 | exp4;
exp4		: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5		: NOT exp5 | exp6;
exp6		: MINUS exp6 | exp7;
exp7		: (ID | ID LP index_ops? RP) LS index_ops RS | exp8;
exp8		: array_val | LP exp RP | ID | fun_call;

array_val 	: array_list | NUM_LIT | BOO_LIT | STR_LIT;
scalar_type	: NUMBER | BOOL | STRING;
array_list	: LS index_ops RS;

// IO
// builtins_call	: readNumber | writeNumber | readBool | writeBool | readString | writeString;
// readNumber		: 'readNumber' LP RP;
// writeNumber 	: 'writeNumber' LP (ID | array_ele | NUM_LIT) RP;
// readBool		: 'readBool' LP RP;
// writeBool 		: 'writeNumber' LP (ID | array_ele | BOO_LIT) RP;
// readString		: 'readString' LP RP;
// writeString		: 'writeString' LP (ID | array_ele | STR_LIT) RP;

/*------------------------------------------------------------------
 * LEXER RULES 
 ------------------------------------------------------------------*/

// KEYWORDS

NUMBER	: 'number';
BOOL	: 'bool' ;
STRING	: 'string';
RETURN	: 'return';
VAR     : 'var' ;
DYNAMIC	: 'dynamic';
FUNC	: 'func' ; 
FOR		: 'for';
UNTIL	: 'until';
BY		: 'by';
BREAK	: 'break';
CONTINUE: 'continue';
IF	    : 'if' ;
ELSE	: 'else' ;
ELIF	: 'elif';
BEGIN	: 'begin';
END		: 'end';
NOT		: 'not';
AND		: 'and';
OR		: 'or';

// OPERATORS
PLUS	: '+';
MINUS	: '-';
MUL		: '*';
DIV		: '/';
MOD		: '%';
EQ_STR  : '=' ;
ASSIGN 	: '<-' ; 
DIFFER	: '!=';
LT		: '<';
LE	    : '<=' ;
GT		: '>';
GE	    : '>=' ;
CONCAT	: '...';
EQ_NUM  : '==' ;	

// SEPARATORS
LP		: '(';
RP		: ')';
LS		: '[';
RS		: ']';
COMMA	: ',';
NEWLINE	: '\n' | '\r\n' {self.text = '\n'};

// IDENTIFIER 
ID		: [a-zA-Z_] [a-zA-Z_0-9]*;

// LITERAL: bat buoc phai de the nay moi chay
BOO_LIT	: TRUE | FALSE;
TRUE	: 'true' ;
FALSE	: 'false' ;
NUM_LIT	: INT_PART DEC_PART? EXP_PART?;
fragment INT_PART : [0-9]+;
fragment DEC_PART : [.] [0-9]*;
fragment EXP_PART : [eE] [+-]? [0-9]+;

STR_LIT: ["] (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"' )* ["] {self.text = self.text[1:-1]};
fragment ILL_ESC_CHAR: [\r\f] |'\\'~[bfrnt'\\];

// SKIP THESE INGREDIENTS
COMMENT: '##' ~[\r\n\f]* -> skip; 
WS: [ \t\b\f]+ -> skip; 

UNCLOSE_STRING: ["] (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"' )* ('\r\n' | '\n' | EOF) {
	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: ["] (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"' )* ILL_ESC_CHAR {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
