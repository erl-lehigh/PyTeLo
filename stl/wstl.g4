grammar wstl;

@header {
'''
 Copyright (C) 2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''
}


wstlProperty:
         '(' child=wstlProperty ')' #parprop
    |    booleanExpr #booleanPred
    |    op=NOT child=wstlProperty #formula
    |    op=EVENT '[' low=RATIONAL ',' high=RATIONAL ']' ('^' weight=VARIABLE)?
         child=wstlProperty #formula
    |    op=ALWAYS '[' low=RATIONAL ',' high=RATIONAL ']' ('^' weight=VARIABLE)?
         child=wstlProperty #formula
    |    left=wstlProperty op=IMPLIES right=wstlProperty #formula
    |    left=wstlProperty op=AND ('^' weight=VARIABLE)?
         right=wstlProperty #formula
    |    op=AND ('^' weight=VARIABLE)?
         '(' wstlProperty (',' wstlProperty)+ ')' #longFormula
    |    left=wstlProperty op=OR ('^' weight=VARIABLE)?
         right=wstlProperty #formula
    |    op=OR ('^' weight=VARIABLE)?
         '(' wstlProperty (',' wstlProperty)+ ')' #longFormula
    |    left=wstlProperty op=UNTIL '[' low=RATIONAL ',' high=RATIONAL ']'
         ('^' weight=VARIABLE)? right=wstlProperty #formula
    |    left=wstlProperty op=RELEASE '[' low=RATIONAL ',' high=RATIONAL ']'
         ('^' weight=VARIABLE)? right=wstlProperty #formula
    ;
expr:
        ( '-(' | '(' ) expr ')'
    |   <assoc=right>   expr '^' expr
    |   VARIABLE '(' expr ')'
    |   expr ( '*' | '/' ) expr
    |   expr ( '+' | '-' ) expr
    |   RATIONAL
    |   VARIABLE
    ;
booleanExpr:
         left=expr op=( '<' | '<=' | '=' | '>=' | '>' ) right=expr
    |    op=BOOLEAN
    ;
AND : '&' | '&&' | '/\\' ;
OR : '|' | '||' | '\\/' ;
IMPLIES : '=>' ;
NOT : '!' | '~' ;
EVENT : 'F' | '<>' ;
ALWAYS : 'G' | '[]' ;
UNTIL : 'U' ;
RELEASE : 'R' ;
BOOLEAN : 'true' | 'True' | 'false' | 'False' ;
VARIABLE : ( [a-z] | [A-Z] )( [a-z] | [A-Z] | [0-9] | '_' )* ;
RATIONAL : ('-')? [0-9]* ('.')? [0-9]+ ( 'E' | 'E-' )? [0-9]* ;
WS : ( ' ' | '\t' | '\r' | '\n' )+ -> skip ;
