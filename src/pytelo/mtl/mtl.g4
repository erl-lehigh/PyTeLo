grammar mtl;

@header {
'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''
}


mtlProperty:
         '(' child=mtlProperty ')' #parprop
    |    booleanExpr #booleanPred
    |    op=NOT child=mtlProperty #formula
    |    op=EVENT '[' low=RATIONAL ',' high=RATIONAL ']' child=mtlProperty #formula
    |    op=ALWAYS '[' low=RATIONAL ',' high=RATIONAL ']' child=mtlProperty #formula
    |    left=mtlProperty op=IMPLIES right=mtlProperty #formula
    |    left=mtlProperty op=AND right=mtlProperty #formula
    |    left=mtlProperty op=OR right=mtlProperty #formula
    |    left=mtlProperty op=UNTIL '[' low=RATIONAL ',' high=RATIONAL ']' right=mtlProperty #formula
    ;
booleanExpr:
         op=BOOLEAN
    |    op=VARIABLE
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
