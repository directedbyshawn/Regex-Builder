'''

    Class to represent a deterministic finite automata.

'''

import state
from state import State
from termcolor import colored


class DFA():

    current_id = 0

    def __init__(self):
        self.__states: list = []
        self.__alphabet: list = []
        self.__start_state: State = None
        self.__accept_states: list = []
        self.__current_state: State = None
        self.__num_states: int = 0

    def __repr__(self) -> str:

        # prints how many states
        string = "This is a " + str(self.__num_states) + " state DFA "

        # prints info about alphabet
        if (len(self.__alphabet) == 0):
            string += "current working on no alphabet"
        else:
            string += "currently working on the alphabet containing characters "
            try:
                for i in range(len(self.__alphabet)):
                    if (i == len(self.__alphabet) - 1):
                        string += self.__alphabet[i] + ". "
                    else:
                        string += self.__alphabet[i] + ", "
            except:
                raise BadAlphabetError

        # lists states
        if (len(self.get_states()) == 0):
            string += " It has no states."
        else:
            string += "It has states "
            for i in range(len(self.get_states())):
                if (i == len(self.get_states()) - 1):
                    string += "and state q" + str(self.get_states()[i].get_id()) + ". "
                else:
                    string += "q" + str(self.get_states()[i].get_id()) + ", "

        # prints start state if there is one
        if (self.has_start_state()):
            string += "It has start state q" + str(self.get_start_state().get_id()) + ". "
        else:
            string += "It currently has no start state. "

        # prints accept state info
        if (len(self.get_accept_states()) == 0):
            string += "It currently has no accept states."
        elif (len(self.get_accept_states()) == 1):
            string += "It has accept state q" + str(self.get_accept_states()[0].get_id()) + "."
        else:
            string += "It has accept states "
            for i in range(len(self.get_accept_states())):
                if (i == len(self.get_accept_states()) - 1):
                    string += " and q" + self.get_accept_states()[i] + "."
                else:
                    string += "q" + self.get_accept_states()[i] + ", "
            

        return string

    def get_states(self) -> list:
        return self.__states

    def add_state(self, new_state:State) -> bool:

        # ensures that state is not already in dfa
        if (new_state in self.get_states()):
            raise DuplicateStateError
        
        # ensure that dfa and new state have same alphabet
        if (new_state.get_alphabet() != self.get_alphabet()):
            raise MismatchingAlphabetError

        if (new_state.is_start_state() and self.has_start_state()):
            raise MultipleStartStateError

        # ensure state isnt a start state if there is already one, if there isnt make it the start state
        if (new_state.is_start_state() and self.has_start_state()):
            raise MultipleStartStateError
        elif (new_state.is_start_state()):
            self.set_start_state(new_state)

        # see if its an accept state and if so add it to accept state list
        if (new_state.is_accept_state()):
            self.add_accept_state(new_state)

        # set states id
        new_state.set_id(DFA.current_id)
        DFA.current_id += 1

        # add it to states list
        self.__states.append(new_state)

        # increment num_states
        self.__num_states += 1

    def get_alphabet(self) -> list:
        return self.__alphabet
    
    def add_to_alphabet(self, char:chr):
        if (char in self.get_alphabet()):
            raise state.DuplicateCharacterError
        else:
            self.__alphabet.append(char)

    def has_start_state(self) -> bool:
        if (self.__start_state == None):
            return False
        else:
            return True

    def get_start_state(self) -> State:
        return self.__start_state
        
    def set_start_state(self, new_start_state:State) -> bool:
        if (self.has_start_state()):
            return False
        else:
            self.__start_state = new_start_state
            return True

    def has_accept_states(self) -> bool:
        if (len(self.__accept_states) == 0):
            return False
        else:
            return True

    def get_accept_states(self) -> list:
        return self.__accept_states

    def add_accept_state(self, new_accept_state:State):
        self.__accept_states.append(new_accept_state)

    def get_current_state(self) -> State:
        return self.__current_state

    def set_current_state(self, new_state:State):
        self.__current_state = new_state

    def add_transition(self, character:chr, current_state:State, new_state:State):
        if (current_state not in self.get_states() or new_state not in self.get_states()):
            raise StatesDNE
        if (character in current_state.transition_table.keys()):
            raise DuplicateTransitionError
        elif (character not in self.get_alphabet()):
            raise UnrecognizedCharacterError

        current_state.transition_table[character] = new_state

    def parse_string(self, string:str) -> bool:

        # makes sure dfa has start state
        if (not self.has_start_state()):
            raise NoStartStateError
        
        # makes sure dfa has at least one accept state
        if (not self.has_accept_states):
            raise NoAcceptStatesError

        # makes sure the input string is valid
        for char in string:
            if char not in self.get_alphabet():
                raise BadCharacterParseError

        # makes sure each states has the correct amount of transitions
        for state in self.get_states():
            list_of_keys = []
            for key in state.transition_table:
                list_of_keys.append(key)
            if list_of_keys != self.get_alphabet():
                raise MissingTransitionsError

        # runs string through dfa
        if (string == ""):
            if (self.get_start_state().is_accept_state()):
                return True
            else:
                return False
        else:
            self.set_current_state(self.get_start_state())
            new_state:State = State()
            for char in string:
                new_state = self.get_current_state().transition_table[char]
                self.set_current_state(new_state)

            if (self.get_current_state().is_accept_state()):
                return True
            else:
                return False



class MissingTransitionsError(Exception):

    colored_message = colored("ERROR: DFA's transition table is missing some values", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class BadCharacterParseError(Exception):

    colored_message = colored("ERROR: Cannot parse a string with characters outside the DFA's alphabet", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)
    
class NoAcceptStatesError(Exception):

    colored_message = colored("ERROR: Cannot parse a string until there is a start state", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class NoStartStateError(Exception):

    colored_message = colored("ERROR: Cannot parse a string until there is a start state", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class StatesDNE(Exception):

    colored_message = colored("ERROR: Couldnt find current or new states when adding transition", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class MultipleStartStateError(Exception):

    colored_message = colored("ERROR: Cannot have multiple start states", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class MismatchingAlphabetError(Exception):

    colored_message = colored("ERROR: Alphabet of state and DFA do not match", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class BadAlphabetError(Exception):

    colored_message = colored("ERROR: Bad alphabet characters", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class DuplicateStateError(Exception):

    colored_message = colored("ERROR: Cannnot add duplicate state", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class DuplicateTransitionError(Exception):

    colored_message = colored("ERROR: Cannot add a transition on a character that already exists.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class UnrecognizedCharacterError(Exception):

    colored_message = colored("ERROR: Cannot add a transition for a character that is not in the alphabet.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)