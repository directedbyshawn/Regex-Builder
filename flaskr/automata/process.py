'''

    This file runs the python implementation of the DFA and returns whether the string was accepted or not

'''

import dfa, state, sys
from termcolor import colored



def main(string) -> bool:

    # empty list of states
    states = []
    
    # q0 (start state)
    state1 = state.State()
    state1.toggle_start_state()
    states.append(state1)

    # q1
    state2 = state.State()
    states.append(state2)

    # q2 (accept state)
    state3 = state.State()
    state3.toggle_accept_state()
    states.append(state3)

    # q3 (reject state)
    state4 = state.State()
    states.append(state4)

    # adds alphabet to all states
    for this_state in states:
        this_state.add_to_alphabet("a")
        this_state.add_to_alphabet("b")
    
    # initialize dfa
    this_dfa = dfa.DFA()

    # add alphabet
    this_dfa.add_to_alphabet("a")
    this_dfa.add_to_alphabet("b")

    # add states
    this_dfa.add_state(state1)
    this_dfa.add_state(state2)
    this_dfa.add_state(state3)
    this_dfa.add_state(state4)

    '''

        Transition table for each state
    
    '''
    this_dfa.add_transition("a", state1, state2)
    this_dfa.add_transition("b", state1, state1)
    
    this_dfa.add_transition("a", state2, state3)
    this_dfa.add_transition("b", state2, state2)

    this_dfa.add_transition("a", state3, state4)
    this_dfa.add_transition("b", state3, state3)
    
    this_dfa.add_transition("a", state4, state4)
    this_dfa.add_transition("b", state4, state4)

    # passes string into dfa
    return (this_dfa.parse_string(string))


if __name__ == "__main__":
    print(colored("ERROR: Please use run.py instead.", "red"))