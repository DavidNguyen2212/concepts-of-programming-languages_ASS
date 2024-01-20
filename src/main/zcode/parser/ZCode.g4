grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

/*------------------------------------------------------------------
 * LEXER RULES 
 ------------------------------------------------------------------*/

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
SEMI	: ';';

// KEYWORDS
TRUE	: 'true' ;
FALSE	: 'false' ;
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

// Literal
NUM_LIT	: INT_PART DEC_PART? EXP_PART?;
fragment INT_PART : [0-9]+;
fragment DEC_PART : [.] [0-9]*;
fragment EXP_PART : [eE] [+-]? [0-9]+;
BOO_LIT	: TRUE | FALSE;
STR_LIT	: 
	DOU_Q (~[\r\n\f\\"'] | ESCAPE | DOU_Q_INTEXT)* DOU_Q {
	self.text = self.text[1:-1]
};

// STR_LIT: ["] (~[\r\n\f\\"'] | '\\' [bfrnt'\\] | [']["])* ["] {self.text = self.text[1:-1]};
NEWLINE: '\n';
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
fragment ILL_ESC_CHAR: '\\'~[bfrnt'\\] | [']~["];
// IDENTIFIER 
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

// SKIP THESE INGREDIENTS
COMMENT: '##' ~[\r\n\f]*; // -> skip skip comments
WS: [ \t\r]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: DOU_Q (~[\r\n\f\\"] | ESCAPE | DOU_Q_INTEXT)* ('\r'? '\n' | EOF) 
{
	err_string = self.text[1:]
	if (err_string[-1] == '\n'):
		raise UncloseString(self.text[1:-2])
	else:
		raise UncloseString(err_string)
};

ILLEGAL_ESCAPE: DOU_Q (~[\r\n\f\\"] | ESCAPE | DOU_Q_INTEXT)* ILL_ESC_CHAR {
	esc_list = ['\'', 'b', 'f', 'r', 'n', 't', '\\']
	for i in range(1, len(self.text) - 1):
		if (self.text[i] == esc_list[0]) or (self.text[i] == '\\' and self.text[i+1] not in esc_list): 
			raise IllegalEscape(self.text[1:i+2])
			break
};

ERROR_CHAR: . {raise ErrorToken(self.text)};
