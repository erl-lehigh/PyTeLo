grammar wmtl;

@header {
'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''
}


wmtlProperty:
         '(' child=wmtlProperty ')' #parprop
    |    booleanExpr #booleanPred
    |    op=NOT child=wmtlProperty #formula
    |    op=EVENT '[' low=RATIONAL ',' high=RATIONAL ']' ('^' weight=VARIABLE)?
         child=wmtlProperty #formula
    |    op=ALWAYS '[' low=RATIONAL ',' high=RATIONAL ']' ('^' weight=VARIABLE)?
         child=wmtlProperty #formula
    |    left=wmtlProperty op=IMPLIES right=wmtlProperty #formula
    |    left=wmtlProperty op=AND ('^' weight=VARIABLE)?
         right=wmtlProperty #formula
    |    op=AND ('^' weight=VARIABLE)?
         '(' wmtlProperty (',' wmtlProperty)+ ')' #longFormula
    |    left=wmtlProperty op=OR ('^' weight=VARIABLE)?
         right=wmtlProperty #formula
    |    op=OR ('^' weight=VARIABLE)?
         '(' wmtlProperty (',' wmtlProperty)+ ')' #longFormula
    |    left=wmtlProperty op=UNTIL '[' low=RATIONAL ',' high=RATIONAL ']'
         ('^' weight=VARIABLE)? right=wmtlProperty #formula
    ;
booleanExpr:
         op=VARIABLE
    |    op=BOOLEAN
    ;
AND : '&&' | '/\\' ;
OR : '||' | '\\/' ;
IMPLIES : '=>' ;
NOT : '!' | '~' ;
EVENT : 'F' | '<>' ;
ALWAYS : 'G' | '[]' ;
UNTIL : 'U' ;
BOOLEAN : 'true' | 'True' | 'false' | 'False' ;
VARIABLE : ( [a-z] | [A-Z] )( [a-z] | [A-Z] | [0-9] | '_' )* ;
RATIONAL : ('-')? [0-9]* ('.')? [0-9]+ ( 'E' | 'E-' )? [0-9]* ;
WS : ( ' ' | '\t' | '\r' | '\n' )+ -> skip ;