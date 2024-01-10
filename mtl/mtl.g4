grammar mtl;

@header {
'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
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
