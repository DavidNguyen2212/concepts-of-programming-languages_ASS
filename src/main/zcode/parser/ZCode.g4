grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: charList EOF;

/*------------------------------------------------------------------
 * LEXER RULES ------------------------------------------------------------------
 */

// OPERATORS
PLUS	: '+';
MINUS	: '-';
MUL		: '*';
DIV		: '/';
MOD		: '%';
ASS	    : '=' ;
ARROW   : '<-' ; 
DIFFER	: '!=';
LT		: '<';
LE	    : '<=' ;
GT		: '>';
GE	    : '>=' ;
SPREAD	: '...';
EQ	    : '==' ;	

// SEPARATORS
LP		: '(';
RP		: ')';
LS		: '[';
RS		: ']';
COMMA	: ',';

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

// ID
IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

// SKIP THESE INGREDIENTS
WS: [ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, newlines
COMMENT: '##' (.)*? -> skip; // skip comments
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;