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

program		: decl_list EOF;
decl_list 	: decl decl_list | decl;
decl		: vars_decl | funs_decl | ignore;

// kí tự bỏ qua
ignore		: NEWLINE (COMMENT NEWLINE | NEWLINE)*;

// Variables declaration
vars_decl	: (var_decl | imp_var_decl | dynamic_decl) ignore; 
var_decl 	: (value_type ID | value_type array_type) (ASSIGN exp)?;
imp_var_decl: VAR ID ASSIGN exp;
dynamic_decl: DYNAMIC ID (ASSIGN exp)?;

// Function declaration
funs_decl	: FUNC ID LP formal_params RP (ignore? block_stmt | ignore? return_stmt | ignore); 
formal_params : formal_pms_prm | ;
formal_pms_prm: formal_pm COMMA formal_pms_prm | formal_pm;
formal_pm	: value_type ID | DYNAMIC ID | value_type array_type;

// Array
array_type 	: ID LS dim_list RS;
dim_list 	: NUM_LIT COMMA dim_list | NUM_LIT;
array_ele	: ID LS exp_list RS;
//list_index_ops: exp list_index_ops | exp; 


// Statements
stmt		: block_stmt | if_stmt | for_stmt 
			| assign_stmt | continue_stmt | break_stmt
			| return_stmt | (fun_call ignore) | vars_decl | funs_decl;
block_stmt 	: BEGIN ignore stmtlist END ignore;
stmtlist 	: stmtprime | ;
stmtprime	: stmt stmtprime | stmt;
if_stmt		: IF exp ignore? stmt
			(ELIF exp ignore? stmt)* (ELSE ignore? stmt)?;  
for_stmt	: FOR ID UNTIL exp BY exp ignore? stmt;
assign_stmt : (ID | ID index_ops ) ASSIGN exp ignore;
index_ops : LS exp RS index_ops | LS exp RS; 
continue_stmt : CONTINUE ignore;
break_stmt : BREAK ignore;
return_stmt: RETURN exp? ignore;

// Function call
fun_call	: ID LP exp_list? RP | builtins_call;

// Expressions
exp 		: exp1 CONCAT exp1 | exp1;
exp1		: exp2 (EQ_NUM | EQ_STR | DIFFER | LT | GT | LE | GE) exp2 | exp2;
exp2		: exp2 (AND | OR) exp3 | exp3;
exp3		: exp3 (PLUS | MINUS) exp4 | exp4;
exp4		: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5		: NOT exp5 | exp6;
exp6		: MINUS exp6 | exp7;
exp7		: exp7 LS exp_list RS | exp8;
exp8		: array_val | LP exp RP | ID | fun_call;

array_val 	: array_list | NUM_LIT | BOO_LIT | STR_LIT;
value_type	: NUMBER | BOOL | STRING;
array_list: LS list_arr_literal? RS;
list_arr_literal: array_val COMMA list_arr_literal | array_val;
exp_list	: exp COMMA exp_list | exp;

// IO
builtins_call : readNumber | writeNumber | readBool | write | readString | writeString;
readNumber	: 'readNumber' LP RP;
writeNumber : 'writeNumber' LP (ID | array_ele | NUM_LIT) RP;
readBool	: 'readBool' LP RP;
write 		: 'writeNumber' LP (ID | array_ele | BOO_LIT) RP;
readString	: 'readString' LP RP;
writeString	: 'writeString' LP (ID | array_ele | STR_LIT) RP;

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


// IDENTIFIER 
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

BOO_LIT	: TRUE | FALSE;
TRUE	: 'true' ;
FALSE	: 'false' ;
NUM_LIT	: INT_PART DEC_PART? EXP_PART?;
fragment INT_PART : [0-9]+;
fragment DEC_PART : [.] [0-9]*;
fragment EXP_PART : [eE] [+-]? [0-9]+;

STR_LIT	: 
	DOU_Q (~[\r\n\f\\"'] | ESCAPE | DOU_Q_INTEXT)* DOU_Q {
	self.text = self.text[1:-1]
};
// STR_LIT: ["] (~[\r\n\f\\"'] | '\\' [bfrnt'\\] | [']["])* ["] {self.text = self.text[1:-1]};

// OTHERS
fragment DOU_Q	: '"';
fragment DOU_Q_INTEXT : '\'"';
fragment ESCAPE: '\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\\\'
	| '\\\''; 
fragment ILL_ESC_CHAR: [\r\f\\] |'\\'~[bfrnt\\] | [']~["];


// SKIP THESE INGREDIENTS
NEWLINE: '\n';
COMMENT: '##' ~[\r\n\f]*; //  skip comments
WS: [ \t\r]+ -> skip; // skip spaces, tabs, newlines

// UNCLOSE_STRING: DOU_Q (~[\r\n\f\\'"] | ESCAPE | DOU_Q_INTEXT)* ('\r\n'| '\n' | EOF) 
// {
// 	err_string = self.text[1:]
// 	if (err_string[-1] == '\n'):
// 		raise UncloseString(self.text[1:-2])
// 	else:
// 		raise UncloseString(err_string)
// };

// ILLEGAL_ESCAPE: DOU_Q (~[\r\n\f\\'"] | ESCAPE | DOU_Q_INTEXT)* ILL_ESC_CHAR {
// 	esc_list = ['\'', 'b', 'f', 'r', 'n', 't', '\\']
// 	for i in range(1, len(self.text) - 1):
// 		if (self.text[i] == esc_list[0]) or (self.text[i] == '\\' and self.text[i+1] not in esc_list): 
// 			raise IllegalEscape(self.text[1:i+2])
// 			break
// };
// ["] (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"' )* ('\r\n'| '\n' | EOF)
UNCLOSE_STRING: DOU_Q (~[\r\n\f\\'"] | ESCAPE | DOU_Q_INTEXT)* ('\r\n'| '\n' | EOF) {
	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: DOU_Q (~[\r\n\f\\'"] | ESCAPE | DOU_Q_INTEXT)* ILL_ESC_CHAR {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
