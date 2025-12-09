from typing import List
from core.token import Token, TokenType

class Lexer:

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.colunm = 1
        self.indent_level = [0]
        self.current_char = self.source[0]

    def advance(self):
        """Avanza la posicion al siguiente caracter"""
        self.pos += 1
        if self.pos >= len(self.source):
            return
        self.current_char = self.source[self.pos]
        if self.current_char == "\n":
            self.line += 1
            self.colunm = 0
        self.colunm += 1

    def peel(self) -> str:
        """Avanza al sigiente caracter sin mover al posicion actual"""
        peek_pos = self.pos + 1
        return self.source[peek_pos] if peek_pos < len(self.source) else ""

    def number(self) -> Token:
        """Consume un numero y lo retorna"""
        line, colunm = self.line, self.colunm
        number_str = ""

        while self.current_char and self.current_char.isdigit():
            number_str += self.current_char
            self.advance()

        if self.current_char == ".":
            number_str += "."
            self.advance()
            while self.current_char and self.current_char.isdigit():
                number_str += self.current_char
                self.advance()

        return Token(TokenType.NUMBER, float(number_str), line, colunm)

    def string(self) -> Token:
        """Consume la cadena y la retorna"""


    def get_next_token(self) -> Token:
        """Retorna el siguiente token y lo consume"""

        while self.current_char in " \t":
            self.advance()

        if self.current_char.isdigit():
            return self.number()
        if self.current_char == '"':
            return self.string()

        return Token(TokenType.EOF, None, self.line, self.colunm)


    def tokenize(self) -> List[Token]:
        """Retorna en una lista todos los tokens"""
        tokens: List[Token] = []
        current_token = self.get_next_token()

        while current_token.type != TokenType.EOF:
            tokens.append(current_token)
            current_token = self.get_next_token()

        tokens.append(current_token)
        return tokens
