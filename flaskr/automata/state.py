'''

    Class to represent a single state of a deterministic finite automata.

'''

from termcolor import colored


class State():

    def __init__(self):
        self.__is_start_state: bool = False
        self.__is_accept_state: bool = False
        self.transition_table: dict = {}
        self.__alphabet: list = []
        self.__id: int = None

    def __repr__(self) -> str:

        string = "This is "

        if (self.get_id() == None):
            string += "an unidenified state."
        else:
            string += "state q" + str(self.get_id()) + "." 

        # prints alphabet
        if (len(self.get_alphabet()) == 0):
            string += " It has no alphabet. It is "
        else:
            string += " It has alphabet contains characters "
            for i in range(len(self.__alphabet)):
                    if (i == len(self.__alphabet) - 1):
                        string += self.__alphabet[i] + "."
                    else:
                        string += self.__alphabet[i] + ", "
            string += " It is "
                

        # determines states type
        if (self.__is_start_state and self.__is_accept_state):
            string += "a start & accept state"
        elif (self.__is_accept_state):
            string += "an accept state"
        elif (self.__is_start_state):
            string += "a start state"
        else:
            string += "a normal state"

        # adds transition function
        if (len(self.transition_table) == 0):
            string += " with no transition table."
        else:
            for char in self.transition_table:
                string += " that transitions to " + self.transition_table[char] + " on character " + char + ","
            string += "."

        return string

    def __eq__(self, second_state) -> bool:

        if (second_state == None):
            return False
        elif (self.get_id() == None or second_state.get_id() == None):
            return False
        elif (self.get_id() == second_state.get_id()):
            return True
        else:
            return False

    def get_alphabet(self) -> list:
        return self.__alphabet
    
    def add_to_alphabet(self, char:chr):
        if (char in self.get_alphabet()):
            raise DuplicateCharacterError
        else:
            self.__alphabet.append(char)

    def set_id(self, new_id:int):
        self.__id = new_id

    def get_id(self) -> int:
        return self.__id

    def is_start_state(self) -> bool:
        return self.__is_start_state

    def is_accept_state(self) -> bool:
        return self.__is_accept_state

    def toggle_start_state(self) -> bool:
        if (self.__is_start_state):
            self.__is_start_state = False
        else:
            self.__is_start_state = True

        return self.is_start_state()

    def toggle_accept_state(self) -> bool:
        if (self.__is_accept_state):
            self.__is_accept_state = False
        else:
            self.__is_accept_state = True

        return self.is_accept_state()

class DuplicateCharacterError(Exception):

    colored_message = colored("ERROR: Cannot add duplicate character to alphabet.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

