
#hardware-related causes of computer issues and find a solution for those
def solution_a():
        print("i)If your entire keyboard stops working all of a sudden: can be a motherboard issue instead\n\
        ii) Some keys are not responding or outputting random characters, while other keys work normally: keyboard become faulty\n\
        Please Replace the Keyboard\n")

def solution_b():
  
    print("Reason: The touchpad gets damaged over the years of accumulating dust, rust, moisture.\n\
    Using excessive force when you press the touchpad button can also cause damage to it over the years.\n\n\
    Solution: Better to replace the touchpad\n")


def solution_c():
     print("1. Deleting bad registry files\n\
    2.Updating drivers\n\
    3. In some cases, a computer may keep on restarting because of faulty hardware.\n\
    The three main hardware to check on are:RAM,CPU, External Devices \n")

def solution_d():
    print("Restart Windows Explorer.\n\
    To do this, press and hold (Ctrl+Alt+Delete) on your keyboard to open the Task Manager.\n\
    Next, locate and select Windows Explorer from the Processes tab and click Restart.\n\
    You may need to click More Details at the bottom of the window to see the Processes tab.\n")


def solution_e():
    print("i) Check the power supply\n\
    ii) Make sure the monitor or display is functionaln\n\
    iii) If none of the steps work, restart the system\n")


def solution_f():
    
    print("a) Make sure the sound comes from the hard drive\n\
    b) Run a diagnostic software\n")

def solution_g():
    print("1. Check that there is enough space for updates\n\
    2. Scan your system for viruses\n\
    3. Return BIOS settings to their default levels.")

def function_for_problem(arguments):
    match arguments:
        case "a": 
            solution_a()
        case "b":
            solution_b()

        case "c":
            solution_c()
        
        case "d":
            solution_d()

        case "e":
            solution_e()

        case "f":
            solution_f()

        case "g":
            solution_g()



"""--------------------------------------------------------------------------
                                Taking input
---------------------------------------------------------------------------"""

if __name__ == "__main__":
    problem_number= int(input("Please Enter the number of problems you are facing: "))

    print("(a) keys not working on keyboard \n\
    (b) Laptop touchpad causing cursor to jump randomly\n\
    (c) System Automatically Restart\n\
    (d) The computer is frozen\n\
    (e) Computer won’t turn on\n\
    (f) Noisy Hard Drive\n\
    (g)  Blue Screen Of Death (BSOD)\n")
    problems=["a","b","c","d","e","f","g"]


    for _ in range (problem_number):
        problem_select = str(input("Choose your problems types: "))[:1]
        if problem_select not in problems:
            problem_select = str(input("Please select from the given option: "))[:1]
            problem_types.append(problem_select)
        else:
            problem_types.append(problem_select)
    print(problem_types)
    for _ in problem_types:
        print("solution of problem: {}".format(_))
        function_for_problem(_)
    