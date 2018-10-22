grammar stl;

@header {
'''
 Copyright (C) 2015-2018 Cristian Ioan Vasile <cvasile@mit.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''
}


stlProperty:
         '(' child=stlProperty ')' #parprop
    |    booleanExpr #booleanPred
    |    op=NOT child=stlProperty #formula
    |    op=EVENT '[' low=RATIONAL ',' high=RATIONAL ']' child=stlProperty #formula
    |    op=ALWAYS '[' low=RATIONAL ',' high=RATIONAL ']' child=stlProperty #formula
    |    left=stlProperty op=IMPLIES right=stlProperty #formula
    |    left=stlProperty op=AND right=stlProperty #formula
    |    left=stlProperty op=OR right=stlProperty #formula
    |    left=stlProperty op=UNTIL '[' low=RATIONAL ',' high=RATIONAL ']' right=stlProperty #formula
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
BOOLEAN : 'true' | 'True' | 'false' | 'False' ;
VARIABLE : ( [a-z] | [A-Z] )( [a-z] | [A-Z] | [0-9] | '_' )* ;
RATIONAL : ('-')? [0-9]* ('.')? [0-9]+ ( 'E' | 'E-' )? [0-9]* ;
WS : ( ' ' | '\t' | '\r' | '\n' )+ -> skip ;
