grammar stl;

@header {
'''
 Copyright (c) 2015-2020 
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab (ERL), Lehigh University
 @author: Cristian Ioan Vasile <cvasile@lehigh.edu>

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
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
