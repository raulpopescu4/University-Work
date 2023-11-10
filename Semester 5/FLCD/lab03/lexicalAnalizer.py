from symbolTable import SymbolTable
import re

class LexicalAnalyzer:
    def __init__(self, symbol_table):
        self.__symbol_table = symbol_table
        self.__pif = list()
        self.__reserved_keywords = {"def", "int", "char", "string", "boolean", "if", "else", "while", "for", "from",
                                    "to", "return", "print", "input"}
        self.__special_symbols = {"(", ")", "{", "}", ";", "[", "]", "<", "<=", "=", "!=", ">=", "+", "*", ":=", "space", "mod", "-", "div", ","}

    # def is_reserved_word(self, token):
    #     if token in self.__reserved_keywords:
    #         return True;
    #
    #
    # def lexical_analysis(self, input_text):
    #     tokens = input_text.split()
    #     for token in tokens:
    #         if token in self.__reserved_keywords
    #

    def lexical_analysis(self, input_text):
        tokens = input_text.split()
        error_flag = False

        for token in tokens:

            if token in self.__reserved_keywords:
                self.__pif.append((token, "-1"))

            elif token in self.__special_symbols:
                self.__pif.append((token, "-1"))

            elif token.isdigit():
                position = self.__symbol_table.add(token)
                self.__pif.append(("Const", f"({position[0]}, {position[1]})"))

            elif re.match(r'"([^"]*)"', token):
                position = self.__symbol_table.add(token)
                self.__pif.append(("Const", f"({position[0]}, {position[1]})"))

            elif re.match(r"'([^']+)'", token):
                position = self.__symbol_table.add(token)
                self.__pif.append(("Const", f"({position[0]}, {position[1]})"))

            elif token == "false" or token == "true":
                position = self.__symbol_table.add(token)
                self.__pif.append(("Const", f"({position[0]}, {position[1]})"))

            elif re.match(r"([a-zA-Z_][a-zA-Z0-9_]*)", token):
                if self.__symbol_table.search(token) == (-1, -1):
                    position = self.__symbol_table.add(token)
                    self.__pif.append(("Identifier", f"({position[0]}, {position[1]})"))
                else:
                    position = self.__symbol_table.search(token)
                    self.__pif.append(("Identifier", f"({position[0]}, {position[1]})"))

            else:

                print(f"Lexical error: Unrecognized token {token}")
                error_flag = True

        with open("ST.out", "w") as st_out:
            st_out.write(str(self.__symbol_table))
            st_out.write("This is a hash table with coalesced chaining")

        if error_flag:
            print("Lexical error(s) found")
        else:
            print("Lexically correct")

        with open("PIF.out", "w") as pif_out:
            for token in self.__pif:
                pif_out.write(str(token) + "\n")


