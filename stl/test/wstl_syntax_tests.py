'''
 Copyright (C) 2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

from StringIO import StringIO

from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')

from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

# Parse the WSTL formulae strings

with open('wstl_syntax_tests.txt', 'rt') as fin:
    text = StringIO()
    for line in fin:
        if line.strip():
            text.write(line)
        else:
            input_string = text.getvalue()
            print(input_string.strip())
            lexer = wstlLexer(InputStream(input_string))
            tokens = CommonTokenStream(lexer)
            parser = wstlParser(tokens)
            t = parser.wstlProperty()
            if t.weight is None:
                print(None)
            else:
                print(t.weight.text)

            text.close()
            text = StringIO()
