from typing import Any, Dict
from enum import Enum


class TokenType(Enum):
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    NULL = 'NULL'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'
    RELATIONAL = 'RELATIONAL'
    ASSIGNMENT = 'ASSIGNMENT'
    DELIMITER = 'DELIMITER'
    COMMENT = 'COMMENT'
    EOF = 'EOF'
    KEYWORD = 'KEYWORD'
    INDENT = 'INDENT'
    DEDENT = 'DEDENT'
    NEWLINE = 'NEWLINE'


class Token:
    def __init__(self, type: TokenType, value: Any, line: int = 0,column: int = 0):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return "{" + f"TokenType: {self.type.value}, Value: {self.value.__str__()}, Line: {self.line}, Column: {self.column}" + "}"


SINGLE_OPERATORS: Dict[str, TokenType] = {
    '+': TokenType.OPERATOR,
    '-': TokenType.OPERATOR,
    '*': TokenType.OPERATOR,
    '/': TokenType.OPERATOR,
    '%': TokenType.OPERATOR,
    '&': TokenType.OPERATOR,
    '|': TokenType.OPERATOR,
    '^': TokenType.OPERATOR,
    '~': TokenType.OPERATOR,

    '<': TokenType.RELATIONAL,
    '>': TokenType.RELATIONAL,

    '=': TokenType.ASSIGNMENT,

    # delimitadores
    '(': TokenType.DELIMITER,
    ')': TokenType.DELIMITER,
    '[': TokenType.DELIMITER,
    ']': TokenType.DELIMITER,
    '{': TokenType.DELIMITER,
    '}': TokenType.DELIMITER,
    ',': TokenType.DELIMITER,
    ':': TokenType.DELIMITER,
    '.': TokenType.DELIMITER,
    ';': TokenType.DELIMITER,
}

MULTI_OPERATORS: Dict[str, TokenType] = {
    '//': TokenType.OPERATOR,
    '**': TokenType.OPERATOR,
    '<<': TokenType.OPERATOR,
    '>>': TokenType.OPERATOR,

    '==': TokenType.RELATIONAL,
    '!=': TokenType.RELATIONAL,
    '<=': TokenType.RELATIONAL,
    '>=': TokenType.RELATIONAL,

    '+=': TokenType.ASSIGNMENT,
    '-=': TokenType.ASSIGNMENT,
    '*=': TokenType.ASSIGNMENT,
    '/=': TokenType.ASSIGNMENT,
    '//=': TokenType.ASSIGNMENT,
    '**=': TokenType.ASSIGNMENT,
    '&=': TokenType.ASSIGNMENT,
    '|=': TokenType.ASSIGNMENT,
    '^=': TokenType.ASSIGNMENT,
}

KEYWORDS = {
    "if", "else", "elif",
    "while", "for",
    "def", "return",
    "class",
    "and", "or", "not",
    "in", "is",
    "True", "False", "None",
}

DELIMITERS = {'(', ')', '[', ']', '{', '}', ',', ':', '.'}

ESCAPES = {
    'n': '\n',
    't': '\t',
    '\\': '\\',
    '"': '"',
    "'": "'"
}
