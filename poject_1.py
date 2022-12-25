
#hardware-related causes of computer issues and find a solution for those
from multipledispatch import dispatch    

#Taking and store information about the Computer and User
user_information_store={}
user_information_ =[]


for _ in range (int(input("Enter the number of time you want's to run the program: "))):

    """=========================================================================================================================
                                User Information Class
    =========================================================================================================================="""
    
    class user_iformation():
        
        def __init__(self, user_name ="", user_address="", user_mobile="", laptop_model = "") -> None:
            self.user_name = user_name
            self.user_address = user_address
            self.user_mobile = user_mobile
            self.laptop_model = laptop_model

        def python_decorator(func):                                   #Apply pythond decorator
            def user_info(self):
                name = self.user_name
                address = self.user_address
                mobile_number = self.user_mobile

                #The ANSI escape sequence to print bold text is: '\033[1m'  , '\033[0m' ends the bold formatting
                print("\n\033[1mUser Information \033[0m\nName:{}\nAddress: {}\nMobile Number:{}".format(name, address, mobile_number))   
                func(self,self.user_name)
            
            return user_info


        @python_decorator
        def computer_info(self, laptop_info):
            print("Laptop Information from parent class, {}".format(laptop_info))

        python_decorator = staticmethod(python_decorator)



    class computer_information(user_iformation):                                #Class Inheritance
        
        def __init__(self, user_name="", user_address="", user_mobile="", 
        laptop_model="",laptop_RAM_info="", laptop_core_i="", laptop_problem="" ) -> None:
            super().__init__(user_name, user_address, user_mobile, laptop_model)
            self.laptop_model=laptop_model
            self.laptop_RAM_info = laptop_RAM_info
            self.laptop_core_i = laptop_core_i
            self.laptop_problem = laptop_problem

        @user_iformation.python_decorator
        def computer_info(self,user):                                 #method overriding 
            print("\n\033[1mLaptop Information of the user \"{}\"\033[0m\nLaptop Model:{}\n"\
                "RAM Info.: {}\nCorei: {}\nProblem: {}".format(user,self.laptop_model,self.laptop_RAM_info ,self.laptop_core_i, self.laptop_problem))
                                                                                
            


    """===========================================================================
                Take the order for fixing problem and provide cost estimation
    ==========================================================================="""
    class Problem_fixing_cost:
        cost_to_fix= 0

        @dispatch(object)
        def day_cost(self,problem):
            cost = (self.cost_to_fix * 5)
            return "To fix Problem {} you need {} Taka".format(problem, cost)


        @dispatch(object, int)
        def day_cost(self, problem, days):                    #Method Overloading
            cost_per_day = int((self.cost_to_fix*2)/100)
            cost = (self.cost_to_fix - cost_per_day) * days
            return "To fix Problem {} within {} days you need {} Taka".format(problem, days, cost)





    """------------------------------------------------------------------------------------
                    Solutions of the user problem
    ------------------------------------------------------------------------------------"""

    class Troubleshooting:
        
        def solution_a():
            solution= "i)If your entire keyboard stops working all of a sudden: can be a motherboard issue instead\n"\
            "ii) Some keys are not responding or outputting random characters, while other keys work normally: keyboard become faulty\n"\
            "Please Replace the Keyboard"
            print (solution)
            cost ="100"
            return cost

        def solution_b():
            solution="Reason: The touchpad gets damaged over the years of accumulating dust, rust, moisture.\n"\
            "Using excessive force when you press the touchpad button can also cause damage to it over the years.\n"\
            "Solution: Better to replace the touchpad"
        
            print (solution)
            cost = "200"
            return cost

        def solution_c():
            solution="1. Deleting bad registry files\n"\
            "2.Updating drivers\n"\
            "3. In some cases, a computer may keep on restarting because of faulty hardware.\n"\
            "The three main hardware to check on are:RAM,CPU, External Devices"
    
            print (solution)
            cost="400"
            return cost

        def solution_d():
            solution="Restart Windows Explorer.\n"\
            "To do this, press and hold (Ctrl+Alt+Delete) on your keyboard to open the Task Manager.\n"\
            "Next, locate and select Windows Explorer from the Processes tab and click Restart.\n"\
            "You may need to click More Details at the bottom of the window to see the Processes tab."
            print (solution)
            cost = "600"
            return cost


        def solution_e():
            solution="i) Check the power supply\n"\
            "ii) Make sure the monitor or display is functionaln\n"\
            "iii) If none of the steps work, restart the system"
            print (solution)
            cost = "700"
            return cost


        def solution_f():
            solution="a) Make sure the sound comes from the hard drive\n"\
            "b) Run a diagnostic software"
            print (solution)
            cost="900"
            return cost

        def solution_g():
            solution="1. Check that there is enough space for updates\n"\
            "2. Scan your system for viruses\n"\
            "3. Return BIOS settings to their default levels."
        
            print (solution)
            cost="600"
            return cost

    
    def function_for_problem(arguments):
        match arguments:
            case "a": 
                print("\nsolution of problem: {}) {}".format("a","keys not working on keyboard" ))
                return Troubleshooting.solution_a()
                

            case "b":
                print("\nsolution of problem: {}) {}".format("b","aptop touchpad causing cursor to jump randomly"))
                return Troubleshooting.solution_b()
                

            case "c":
                print("\nsolution of problem: {}) {}".format("c","System Automatically Restart"))
                return Troubleshooting.solution_c()
                
            
            
            case "d":
                print("\nsolution of problem: {}) {}".format("d","The computer is frozen"))
                return Troubleshooting.solution_d()
                

            case "e":
                print("\nsolution of problem: {}) {}".format("e","Computer won't turn on"))
                return Troubleshooting.solution_e()
                

            case "f":
                print("\nsolution of problem: {}) {}".format("f", "Noisy Hard Drive"))
                return Troubleshooting.solution_f()
                

            case "g":
                print("\nsolution of problem: {}) {}".format("g", "Blue Screen Of Death (BSOD)"))
                return Troubleshooting.solution_g()
                







    """===================================================================================================
                                    Taking input
    ===================================================================================================="""

    if __name__ == "__main__":

        """------------------------------------------------------------------------------------------------
                User Information Provided By User
        -------------------------------------------------------------------------------------------------"""
        print("Provide Your Information")
        user_information_store["User Name"]=input("Enter user Name: ")
        user_information_store["Mobile"] = input("Enter user mobile number: ")
        user_information_store["user_address"]=input("Enter user address: ")
        user_information_store["laptop model"]=input("Enter user laptop model: ")
        user_information_store["laptope_RAM_info"]=input("Enter your laptop RAM size: ")
        user_information_store["latop_core_i"]=input("Core-i of your laptop: ")
        user_information_store["laptop_problem"]= input("Write your laptop problem within 20 words: ")
        user_information_.append(user_information_store.copy())

        user_one = computer_information()
        user_one.user_name = user_information_store["User Name"]
        user_one.user_address = user_information_store["user_address"]
        user_one.user_mobile = user_information_store["Mobile"] 
        user_one.laptop_model = user_information_store["laptop model"]
        user_one.laptop_RAM_info = user_information_store["laptope_RAM_info"]
        user_one.laptop_core_i = user_information_store["latop_core_i"]
        user_one.laptop_problem = user_information_store["laptop_problem"]


        """--------------------------------------------------------------------------------------------
                Problem Selection By User
        --------------------------------------------------------------------------------------------"""
        while True:                                                         #Error Hndling
            try:
                problem_number= int(input("Please Enter the number of problems you are facing : "))
                break
            except ValueError:
                print("Please Enter Intiger Value")

        problem_list = "(a) keys not working on keyboard \n"\
            "(b) Laptop touchpad causing cursor to jump randomly\n"\
            "(c) System Automatically Restart\n"\
            "(d) The computer is frozen\n"\
            "(e) Computer won’t turn on\n"\
            "(f) Noisy Hard Drive\n"\
            "(g) Blue Screen Of Death (BSOD)\n"
        
        print(problem_list)
        problems=["a","b","c","d","e","f","g"]
        problem_types=[]

        for _ in range (problem_number):
            problem_select = str(input("Choose your problems types: "))[:1]

            if problem_select not in problems:        
                problem_select = str(input("Please select from the given option: "))[:1]
                problem_types.append(problem_select)

            elif problem_select in problem_types:        
                problem_select = str(input("You already Choose this, Select another one: "))[:1]
                if problem_select not in problems:        
                    problem_select = str(input("Please select from the given option: "))[:1]
                problem_types.append(problem_select)

            else:
                problem_types.append(problem_select)



        """--------------------------------------------------------------------------------
                            For  output
        --------------------------------------------------------------------------------"""
        print("-"*20,"\n Output\n","-"*20)
        user_one.computer_info()
        list(map(lambda x:function_for_problem(x), problem_types))      #call the solution function utilizing lambda function for each problem




        """"---------------------------------------------------------------------------------------
                        If user wants to know the cost then this portion will work
        ----------------------------------------------------------------------------------------"""
        to_fix=input("\nDo you want to know the cost to solve your problem? Write yes or no:")
        if to_fix=="yes":
            for _ in problem_types:
                fixing_cost = int(function_for_problem(_))
                user_cost=Problem_fixing_cost()
                user_cost.cost_to_fix=fixing_cost

                days = int(input("\nDays(int value) you can Provdie to fix:"))
                if days==1 or days==0:
                    print(user_cost.day_cost(_,days))
                    
                else:
                    print(user_cost.day_cost(_))



""""---------------------------------------------------------------------------------------
            If user wants to see his information stored or not useing UserName and Laptop model
----------------------------------------------------------------------------------------"""
user_info_include = input("If you want to see your information Enter 1 else 0: ")

if user_info_include =="1":
    user_name_to_find = input("Enter User Name: ")
    user_laptop_model = input("Enter Your Laptop Model: ")
    for d in user_information_:
        user_find = ("User Name",user_name_to_find) in d.items()
        laptop_find = ("laptop model",user_laptop_model) in d.items()
        if user_find==True and laptop_find==True:
            
            print("\n\033[1mYour information is here\033[0m")
            print("Name:{}\nMobile:{}\nLaptop Model:{}\nLaptop Problem:{}".format(d["User Name"],d["Mobile"], d["laptop model"], d["laptop_problem"]))
            break
        else:
            print("\nInformation Not Found\n")
            break
else:
    print("-"*100,"\nTake your action to solve your problem. GOOD LUCK!!\n",'-'*100)


print("-"*100,"\nEnd! GOOD LUCK!!\n",'-'*100)
