# Randomlly generate the operators and operands like 7 * 8 and let the user give the answer of the question and then proggram will also do generate the answer so that we can compare with the answers that user have given, Like this we can give multiple problems to the user and in the last we can check the time in which those problems have been done. Also we will set a limited time probably of 30 seconds and if the user fails to give all the answers in the given time, the program will say that the user have failed the test. And in the end, the program will also give, how many questions were answered correctly by user.

import random
import time

def randomly():
    first_operand = random.randint(1,12)
    second_operand = random.randint(1,12)
    operators = ['+','-','*','//']
    random_operator = random.choice(operators)
    # expression = 
    if ( random_operator == '//' ):
        first_operand = random.randint(5,50)
        second_operand = random.randint(5,50)
        if ( first_operand < second_operand ):
            first_operand , second_operand = second_operand , first_operand
        if ( first_operand % second_operand != 0 ):
            while ( first_operand % second_operand != 0 ):
                second_operand = random.randint(1,10)
    return first_operand , second_operand , random_operator


number = int( input( "How many questions do you want: " ) )

input("Press Enter to start: ")
print("----------------------")
start_time = time.time()
i = 1
correct = 0
wrong = 0

while i <= number :
    f_o,s_o,r_o = randomly()
    answer = int( input(f"{f_o} {r_o} {s_o} = ") )
    result : int = eval(f"{f_o} {r_o} {s_o}")
    if ( result == answer ):
        correct += 1
        # print("Correct answer!")
    else:
        wrong += 1
        # print("Wrong answer!")
    end_time = time.time()
    total_time = int(round(end_time - start_time,0))
    if ( total_time >= 30 ):
        break
    i += 1
print("----------------------")

end_time = time.time()
total_time = int(round(end_time - start_time,0))
print ( f"You have answered {correct} questions correctly in {total_time} seconds" )








