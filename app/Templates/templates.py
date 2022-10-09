import random
import pandas as pd
from fractions import Fraction
import math
from num2words import num2words

methods = ["repeated addition", "grouping", "the box method", "the standard algorithm", "any method you want"]
male_actors = ["Sam", "Levi", "Nyzir", "Tyrek", "Antonio", "Batman", "Robin"]
male_pronouns = ["he", "him", "his"]
female_actors = ["Flora", "Reese", "Denari", "Katie", "Gina"]
female_pronouns = ["she", "her", "hers"]
bag_objects = ["Skittles", "Reese's Pieces", "Pretzels", "M&Ms"]
other_objects= ["Fornite skins", "books"]
key_words = ["sum", "least common multiple", "product", "total cost", "difference", "common factor", "division", "place value"]
drinks = ["Gatorade", "soda", "iced tea", "water"]
things = ["Fortnite action figures", "Girlscout cookie boxes"]
decimal_place_values = ["tenths", "hundredths", "thousandths"]
whole_place_values = ["ten", "hundred", "thousand", "ten thousand", "hundred thousand", "million"]
times = ['fastest', 'slowest']
sizes = ['largest', 'smallest']
pets = ['dog', 'cat', 'puppy', 'turtle', 'bunny']

def student_input_integer(student_answer, answer):
    condition = False
    while condition == False:
        try: 
            student_answer = int(student_answer)
            condition = True 
        except: 
            feedback = print("Please input your answer as a whole number.")
            student_answer = input("Please enter your answer here:")
            return feedback, student_answer
    while condition == True:
        if student_answer == answer:
            feedback = print("Nice work! You got the right answer.")
            return feedback
            condition = False
        else:
            feedback = print("Your answer is incorrect. Please try again!")
            student_answer = input("Please enter your answer here:")
            return feedback, student_answer
            student_input_integer(student_answer, answer)
            
            
def student_input_float():
    return 1

def student_input_string():
    return 1 

def common_factor(num1,num2,num3):
    n=[]
    for i in range(1, min(num1, num2, num3)+1): 
        if num1%i==num2%i==num3%i==0: 
            n.append(i)
    return n

def g4_computation_multplication_specific_method():
    number1 = random.randint(2, 10)
    number2 = number2 = random.randint(2, 10)
    answer = number1 * number2
    question = "Use {method} to find {number1} X {number2}.".format(method = random.choice(methods), number1 = number1, number2 = number2)
    student_answer = input(question + " Please enter your answer here:")
    return student_answer
    feedback = student_input_integer(student_answer, answer)
    return 2

def g4_computation_multiplication_male_bags():
    number1= random.randint(2, 20)
    number2 = random.randint(2, 20)
    answer = number1*number2
    question = "{male_actor} has {number1} bags of {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                             number2 = number2,
                                                                                                                             male_actor = random.choice(male_actors), 
                                                                                                                             male_pronoun = male_pronouns[0])
    return question

def g4_computation_multiplication_female_bags():
    number1= random.randint(2, 20)
    number2 = random.randint(2, 20)
    answer = number1*number2
    question = "{female_actor} has {number1} bags of {number2} {thing}. How many {thing} does {female_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                             number2 = number2,
                                                                                                                             female_actor = random.choice(female_actors), 
                                                                                                                             female_pronoun = female_pronouns[0])
    return question

def g4_computation_multiplication_double_bags():
    number1= random.randint(2, 20)
    number3 = random.randint(2, 20)
    number4=random.randint(2, 20)
    number2 = random.randint(2, 20)
    answer = number1*number2 + (number3*number4)
    question = "{male_actor1} has {number1} bags of {number2} {thing}. {male_actor2} has {number3} bags of {number4} {thing}. How many {thing} do they have altogether?".format(thing = random.choice(bag_objects),
    number1= number1, number3 = number3, number4=number4,
                                                                                                                             number2 = number2,
                                                                                                                             male_actor1 = random.choice(male_actors), 
                                                                                                                             male_actor2 = random.choice(male_actors))
    return question

def g4_computation_multiplication_fortnite():
    number1= random.randint(2, 20)
    number2 = random.randint(2, 20)
    answer = number1 * number2
    question= "{male_actor} has {number1} profiles with {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = other_objects[0], number1= number1, 
                                                                                                                             number2 = number2,
                                                                                                                             male_actor = random.choice(male_actors), 
                                                                                                                             male_pronoun = male_pronouns[0])
    return question

#This will generate a table of different decimal race times students will have the choose the highest or lowest value of 
def g4_number_sense__comparison_running_table ():
    question_data = [[random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                        [random.choice(female_actors), round(random.uniform(13, 14), 2)], 
                        [random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                       [random.choice(female_actors), round(random.uniform(13, 14), 2)]]
    time = random.choice(times)
    if time == "fastest":
        answer = max(question_data)
    if time =="slowest":
        answer = min(question_data)
    question_df = pd.DataFrame(question_data, columns=['Name', 'Time (in seconds)'])
    question = "The table shows the time it took 4 students to run a 40 meter race. Which student had the {time} time?".format(time = time)
    return question, question_df.head()

def g4_computation_decimal_addition ():
    number1 = round(random.uniform(10, 20), 1)
    number2 = round(random.uniform(10, 20), 1)
    answer = number1 + number2
    question = "{number1} + {number2} = ___".format(number1 = number1, number2 = number2)
    return question

def g4_computation_fraction_addition():
    factor = random.randint(2,10)
    number1 = random.randint(2, 10)
    number2 = random.randint(2, 10) *factor 
    number3 = random.randint(2, 10)
    number4 = random.randint(2, 10) *factor 
    raw_answer = (number1/number2) + (number3/number4)
    string = "{string}".format(string=raw_answer)
    answer = Fraction(string)
    question = "What is the {key_word} of {number1}/{number2} and {number3}/{number4}?".format(number1 = number1, 
                                                                                             number2 = number2, 
                                                                                             number3 = number3, 
                                                                                             number4 = number4, 
                                                                                             key_word = key_words[0])
    return question

def g4_computation_decimal_subtraction_drinks(): 
    number1 = round(random.uniform(1, 20), 2)
    number2 = round(random.uniform(0, 1), 3)
    question = "{male_actor} drinks {number1} liters of {drink}. {female_actor} drinks {number2} liter of {drink}. How much more {drink} does {male_actor} drink than {female_actor}?".format(drink = drinks[0], 
number1 = number1, number2 = number2, male_actor = random.choice(male_actors), 
female_actor = random.choice(female_actors))
    return question

def g4_computation_lcm_word_problem():
    number2 = random.randint(2, 10)
    number1 = random.randint(2, 10)*number2
    number3 = random.randint(2, 10)*number2
    answer = math.lcm(number1, number3)
    question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[1], number1 = number1, number2 = number3)
    return question

#Left off here 
def g4_computation_multiplication_two_digit_word_problem():
    number1 = random.randint(20, 100)
    number2 = random.randint(20, 100)
    answer = number1 * number2
    question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[2], number1 = number1, number2 = number2)
    return question

def g4_computation_multiplication_with_drinks():
    number1 = random.randint(2, 20)
    number2 = random.randint(2, 20)
    answer = number1 * number2
    question= "{female_actor} poured {number1} ounces of {drink} into each of {number2} glasses. Exactly how many ounces of {drink} did {female_actor} pour into all of these glasses?".format(
drink = drinks[0], female_actor = random.choice(female_actors), number1 = number1, number2 = number2)
    return question

def g4_estimation_multiplication_store():
    #NOTE THIS ANSWER IS STRANGE BECAUSE IT REQUIRES ESTIMATION
    number1 = random.randint(10, 30)
    number2 = random.randint(10, 90)
    exact_answer = number1*number2
    question = "At a store, {thing} cost ${number1} each. Which is closest to the {key_word} of {number2} {thing}?".format(number1 = number1, 
                                                                                                                         number2 = number2,
                                                                                                                        thing = random.choice(things), key_word = key_words[3])
    return question
#Needs to be multiple choice

def g4_computation_multiplication_selling_items():
    number1 = random.randint(100,1000)
    number2 = random.randint(2,10)
    answer = number1*number2
    question = "{female_actor} sold {number1} {thing}. Each box cost ${number2}. What was the {key_word} of all the {thing} sold?".format(number1 = number1, 
                                                                                                                                           number2 = number2, 
                                                                                                                                        thing = random.choice(things), 
                                                                                                                                           key_word = key_words[3],
                                                                                                                                           female_actor = random.choice(female_actors))
    return question

def g4_computation_subtraction_word_problem():
    number1 = random.randint(1000,4000)
    number2 = random.randint(100,999)
    answer = number1 - number2
    question = "What is the {key_word} between {number1} and {number2}".format(number1 = number1, 
                                                                             number2 = number2, 
                                                                              key_word = key_words[4])
    return question

def g4_computation_division_running_problem():
    number2 = random.randint(2, 10)
    number1 = random.randint(20,40)*number2
    answer= number1/number2
    question = "{male_actor} ran a total of {number1} minutes in a {number2}-day period. He ran the same number of minutes each day. What is the closest to the number of minutes {male_actor} ran each day?".format(
male_actor = random.choice(male_actors), number2= number2, number1 = number1)
    return question
#Needs to be multiple choice

def g4_computation_fraction_subtraction():
    factor = random.randint(2,10)
    number1 = random.randint(2, 10)
    number2 = random.randint(2, 10) *factor 
    number3 = random.randint(2, 10)
    number4 = random.randint(2, 10) *factor 
    raw_answer = (number1/number2) + (number3/number4)
    string = "{string}".format(string=raw_answer)
    answer = Fraction(string)
    question = "What is the {key_word} between {number1}/{number2} and {number3}/{number4}?".format(key_word = key_words[4], 
                                                                                                   number1 = number1, 
                                                                                                   number2 = number2, 
                                                                                             number3 = number3, 
                                                                                                   number4 = number4)
    return question
#Consider if this needs to be multiplied by a common factor

def g4_computation_multiplication_situps():
    number1 = random.randint(10,40)
    number2= random.randint(2,10)
    number3= random.randint(2,10)
    answer = (number1 * number2) *number3
    question= "{male_actor} does {number1} sit-ups {number2} times per day. What is the total number of sit-ups {male_actor} does in {number3} days?".format(
male_actor= random.choice(male_actors), number1 = number1, number2= number2, 
    number3= number3)
    return question

def g4_computation_common_factor_word_problem():
    factor = random.randint(2, 10)
    number1 = random.randint(2,10)*factor
    number2= random.randint(2,10)*factor
    number3= random.randint(2,10)*factor
    answer = common_factor(number1, number2, number3)
    question = "Which number is a {key_word} of {number1}, {number2}, and {number3}?".format(number1 = number1, 
                                                                                    number2= number2, 
                                                                                          number3= number3,
                                                                                         key_word= key_words[5])
    return question

def g4_number_sense_decimal_place_value():
    #have no idea how to store answer from this 
    number1=round(random.uniform(10, 20), 3)
    question = "What digit is in the {place_value} place in {number1}?".format(place_value= random.choice(decimal_place_values), 
                                                                              number1=number1)
    return question

def g4_computation_division_statement():
    number1 = random.randint(2,6)
    number2 = random.randint(7,11)
    answer = "{number1} divided by {number2}".format(number1=number1, number2=number2)
    question = "Which {key_word} statement represents {number1}/{number2}?".format(key_word = key_words[6], 
                                                                                  number1 = number1, number2 = number2)
#Multiple choice would be good here
    return question

#question 16 is a number line
#Can come back to this because there is a nice number line function

def g4_number_sense_place_value_big_number():
    #Also have no idea how to store this answer
    number1 = random.randint(100, 999)
    number2 = random.randint(100, 999)
    question = "Identify the {key_word} for each digit in the number {number1},{number2}.".format(key_word = key_words[7], 
                                                                                      number1 = number1, 
                                                                                               number2 = number2)
    return question

def g4_number_sense_decimal_largest_value():
    number1 = round(random.uniform(13, 14), 2)
    number2 = round(random.uniform(13, 14), 2)
    number3 = round(random.uniform(13, 14), 2)
    number4 = round(random.uniform(13, 14), 2)
    answer = max(number1, number2, number3, number4)
    question= "Which of the four following numbers is {size}? {number1}, {number2}, {number3}, {number4}".format(
size = random.choice(sizes), number1 = number1, number2 = number2, 
number3 = number3, number4 = number4)
    return question

#Question 19 needs to be multiple choice- it is a comparison of multiple numbers asking which is true

def g4_number_sense_decimal_in_words():
    #Question 20 - also ideally multiple choice- but would be really hard to convert to that
    number = round(random.uniform(1, 10), 2)
    answer = num2words(number)
    question = "How is {number} written in words?".format(number = number)
    return question

def g4_number_sense_round_big_number():
    #Don't know how to store this answer 
    number1= random.randint(1,9)
    number2= random.randint(100,999)
    number3=random.randint(100,999)
    question= "What is {number1},{number2},{number3} rounded to the nearest {place_value}?".format(place_value = random.choice(whole_place_values), number1= number1, 
                                                                                                 number2= number2, number3= number3)
    return question

#question 22 is about equivalent fractions but it is an image

#question 23 is also a fraction picture

def g4_number_sense_fraction_ordering():
    #Question 24 would be better as a drag and drop 
    #don't know how to store this answer
    num1= random.randint(1,9)
    num2= random.randint(1,9)
    num3= random.randint(1,9)
    num4 = random.randint(1,9)
    num5= random.randint(1,9)
    num6= random.randint(1,9)
    question = "Order these fractions from least to greatest: {num1}/{num2}, {num3}/{num4}, {num5}/{num6}".format(
        num1= num1, num2= num2, num3= num3, num4 = num4, 
        num5= num5, num6= num6)
    return question

def g4_number_sense_decimal_round_hundredth():
    number1 = round(random.uniform(1, 10), 2)
    answer = number1
    question = "Which number, when rounded to the nearest hundredth, is equal to {number1}".format(number1 = number1)
    return question
# Needs to be multiple choice

def g4_geometry_shapes_four_angles():
    question = "Which figure has less than four angles?"
    return question
#needs to be multiple choice 

#question 27 is a picture of a comb asking about length 

#question 28 is about parallel lines

def g4_measurement_pounds_to_ounces():
    number1 = random.randint(1,9)
    answer = number1*16
    question = "{female_actor}'s {pet} weighted {number1} pounds. What is the total number of ounces {female_actor}'s {pet} weighed?".format(number1 = number1, female_actor = random.choice(female_actors), pet = random.choice(pets))
    return question

#30 is about figures that are congruent

def g4_measurement_gallons_to_pints():
    number1 = random.randint(1,9)
    answer = number1*8
    question = "{female_actor} has {number1} gallons of {drink}. What is the total number of pints of {drink} {female_pronoun} has?".format(number1 = number1, female_actor = random.choice(female_actors), drink = random.choice(drinks), female_pronoun= female_pronouns[0])
    return question