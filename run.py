'''

    This file runs the same dfa in both c++ and python and compares the run times. The
    DFA accepts all strings with exactly 2 a's on the alphabet Σ = {a, b}. 

'''

import time, subprocess, process, os, random
from subprocess import Popen, PIPE, check_output

RUN_PY = True
RUN_CPP = False
DEBUG = True

def main():

    global RUN_PY, RUN_CPP, DEBUG

    cls()

    time.sleep(1)

    print("...")

    time.sleep(2)

    print_options()

    # input validation
    good_input: bool = False
    user_input: str = ""
    while (not good_input):
        user_input = input("Your choice: ")
        if (user_input != "1" and user_input != "2" and user_input != "3"):
            print("ERROR: Please enter 1, 2, or 3")
            time.sleep(1.5)
            print_options()
        else:
            good_input = True
            if (user_input == "3"):
                print("See you soon!")
                time.sleep(2)
                cls()
                exit()

    cls()

    string: str = ""
    bad_string: bool = False
    num: int = 0
    bad_num: bool = False
    good_input = False
    while (good_input == False):
        if (user_input == "1"):
            print("Alright, what string would you like to enter?")
            string = input("Your string (only a's and b's): ").rstrip()
            for char in string:
                if (char != "a" and char != "b"):
                    bad_string = True
            if (len(string) < 3):
                bad_string = True
            if (bad_string):
                print("ERROR: Please enter a valid string of only a's and b's greater than length 3")
                bad_string = False
                time.sleep(2)
                cls()
            else:
                good_input = True
            
        elif (user_input == "2"):
            print("Alright, what length string would you like to enter?")
            try:
                num = int(input("Your int (must be postive and >= 3): "))
                if (num < 3):
                    bad_num = True
                if (bad_num):
                    print("ERROR: Please enter a valid number")
                    bad_num = False
                    time.sleep(2)
                    cls()
                else:
                    good_input = True
            except:
                print("ERROR: Please enter a valid number")
                bad_num = False
                time.sleep(2)
                cls()

    cls()

    time.sleep(1)

    print("...")

    time.sleep(2)

    cls()

    '''
    
        Generates input string for DFA
    
    '''
    input_string: str = ""
    alphabet: list = ["a", "b"]

    if (user_input == "1"):
        input_string = string
    else:
        for i in range(num):
            index = random.randint(0, 1)
            input_string += alphabet[index]

    python_time: float = 0
    cpp_time: float = 0

    # python
    if (RUN_PY):

        python_start_time = time.time()

        # processes string
        status: bool = process.main(input_string)

        python_end_time = time.time()

        # calculates total time took
        python_time = python_end_time - python_start_time

        # prints results
        if (status):
            print("PythonDFA Accepted the string in {runtime:.21f}\n seconds.".format(input_string, runtime = python_time))
        else:
            print("PythonDFA Rejected the string in {runtime:.21f}\n seconds.".format(input_string, runtime = python_time))

    # cpp
    if (RUN_CPP):

        pass





def cls():

    '''

        Clears console.

    '''

    os.system("cls" if os.name=="nt" else "clear")

def print_options():

    '''

        Prints options for user.

    '''

    cls()

    print("Welcome to the DFA run time comparison simulator.")
    print("---------------------------")
    print("To enter a specific string, press 1 and hit enter.")
    print("To use a random string of specified length, press 2 and hit enter.")
    print("To exit, press 3 and hit enter.")
    print()
    print()



if __name__ == "__main__":
    main()