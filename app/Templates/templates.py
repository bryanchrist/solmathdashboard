import random
import pandas as pd
#from fractions import Fraction
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
sports = ['basketball', 'soccer', 'football', 'lacrosse', 'volleyball', 'field hockey', 'tennis', 'swimming', 'track']
metric_system = ['centimeters', 'millimeters']

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

def common_factor(num1,num2,num3):
    n=[]
    for i in range(1, min(num1, num2, num3)+1): 
        if num1%i==num2%i==num3%i==0: 
            n.append(i)
    return n

class g4_computation_multplication_specific_method():
    def __init__(self):
        
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 10)
        self.answer = number1 * number2
        self.question= "Use {method} to find {number1} X {number2}.".format(method = random.choice(methods), number1 = number1, number2 = number2)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

#doesn't work
class g4_computation_multiplication_male_bags():
    def __init__(self):
        
        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question = "{male_actor} has {number1} bags of {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 male_actor = random.choice(male_actors), 
                                                                                                                                 male_pronoun = male_pronouns[0])
        
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
    
class g4_computation_multiplication_female_bags():
    def __init__(self):

        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1*number2
        self.question = "{female_actor} has {number1} bags of {number2} {thing}. How many {thing} does {female_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 female_actor = random.choice(female_actors), 
                                                                                                                                 female_pronoun = female_pronouns[0])
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
    

class g4_computation_multiplication_double_bags():
    def __init__(self):
        
        number1= random.randint(2, 20)
        number3 = random.randint(2, 20)
        number4=random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1*number2 + (number3*number4)
        self.question = "{male_actor1} has {number1} bags of {number2} {thing}. {male_actor2} has {number3} bags of {number4} {thing}. How many {thing} do they have altogether?".format(thing = random.choice(bag_objects),
        number1= number1, number3 = number3, number4=number4,
                                                                                                                                 number2 = number2,
                                                                                                                                 male_actor1 = random.choice(male_actors), 
                                                                                                                                 male_actor2 = random.choice(male_actors))
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_computation_multiplication_fortnite():
    def __init__(self):
        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question= "{male_actor} has {number1} profiles with {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = other_objects[0], number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 male_actor = random.choice(male_actors), 
                                                                                                                                 male_pronoun = male_pronouns[0])
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
        

#This will generate a table of different decimal race times students will have the choose the highest or lowest value of 
class g4_number_sense__comparison_running_table():
    def __init__(self):
        
        question_data = [[random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                            [random.choice(female_actors), round(random.uniform(13, 14), 2)], 
                            [random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                           [random.choice(female_actors), round(random.uniform(13, 14), 2)]]
        time = random.choice(times)
        self.question_df = pd.DataFrame(question_data, columns=['Name', 'Time (in seconds)'])
        if time == "fastest":
            self.answer = max(self.question_df['Time (in seconds)'])
        if time =="slowest":
            self.answer = min(self.question_df['Time (in seconds)'])
        self.question = "The table shows the time it took 4 students to run a 40 meter race. Which time was the {time} time?".format(time = time)
    
    def print_question(self):
        return self.question, self.question_df.head()
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"


class g4_computation_decimal_addition():
    def __init__(self):
        
        number1 = round(random.uniform(10, 20), 1)
        number2 = round(random.uniform(10, 20), 1)
        self.answer = number1 + number2
        self.question = "{number1} + {number2} = ___".format(number1 = number1, number2 = number2)
       
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_computation_fraction_addition():
    def __init__(self):
        
        factor = random.randint(2,10)
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 6) *factor 
        number3 = random.randint(1, 10)
        number4 = random.randint(1, 6) *factor 
        self.answer = (number1/number2) + (number3/number4)
        self.question = "What is the {key_word} of {number1}/{number2} and {number3}/{number4}?".format(number1 = number1, 
                                                                                                 number2 = number2, 
                                                                                                 number3 = number3, 
                                                                                                 number4 = number4, 
                                                                                                 key_word = key_words[0])
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_computation_decimal_subtraction_drinks(): 
    def __init__(self):
        number1 = round(random.uniform(1, 2), 2)
        number2 = round(random.uniform(0, 1), 3)
        self.answer = number1 - number2
        self.question = "{male_actor} drinks {number1} liters of {drink}. {female_actor} drinks {number2} liter of {drink}. How much more {drink} does {male_actor} drink than {female_actor}?".format(drink = drinks[0], 
    number1 = number1, number2 = number2, male_actor = random.choice(male_actors), 
    female_actor = random.choice(female_actors))
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_computation_lcm_word_problem():
    def __init__(self):
        
        number2 = random.randint(2, 10)
        number1 = random.randint(2, 10)*number2
        number3 = random.randint(2, 10)*number2
        self.answer = math.lcm(number1, number3)
        self.question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[1], number1 = number1, number2 = number3)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_computation_multiplication_two_digit_word_problem():
    def __init__(self):
        number1 = random.randint(20, 100)
        number2 = random.randint(20, 100)
        self.answer = number1 * number2
        self.question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[2], number1 = number1, number2 = number2)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
        
class g4_computation_multiplication_with_drinks():
    def __init__(self):
        number1 = random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question= "{female_actor} poured {number1} ounces of {drink} into each of {number2} glasses. Exactly how many ounces of {drink} did {female_actor} pour into all of these glasses?".format(
    drink = drinks[0], female_actor = random.choice(female_actors), number1 = number1, number2 = number2)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"   

class g4_estimation_multiplication_store():
    #NOTE THIS ANSWER IS STRANGE BECAUSE IT REQUIRES ESTIMATION
    def __init__(self):
        number1 = random.randint(10, 30)
        number2 = random.randint(10, 90)
        self.answer = number1*number2
        self.question = "At a store, {thing} cost ${number1} each. Which is closest to the {key_word} of {number2} {thing}?".format(number1 = number1, number2 = number2, thing = random.choice(things), key_word = key_words[3])
#Needs to be multiple choice

    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"   
    

class g4_computation_multiplication_selling_items():
    def __init__(self):
        number1 = random.randint(100,1000)
        number2 = random.randint(2,10)
        self.answer = number1*number2
        self.question = "{female_actor} sold {number1} {thing}. Each box cost ${number2}. What was the {key_word} of all the {thing} sold?".format(number1 = number1, number2 = number2, thing = random.choice(things), key_word = key_words[3], female_actor = random.choice(female_actors))
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"     

class g4_computation_subtraction_word_problem():
    def __init__(self):
        number1 = random.randint(1,4)
        number3=(100,999)
        number2 = random.randint(100,999)
        self.answer = number1 - number2
        self.question = "What is the {key_word} between {number1},{number3} and {number2}?".format(number1 = number1, 
                                                                                 number2 = number2, 
                                                                                  key_word = key_words[4])
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"      

class g4_computation_division_running_problem():
    def __init__(self):
        number2 = random.randint(2, 10)
        number1 = random.randint(20,40)*number2
        self.answer= number1/number2
        self.question = "{male_actor} ran a total of {number1} minutes in a {number2}-day period. He ran the same number of minutes each day. What is the closest to the number of minutes {male_actor} ran each day?".format(
    male_actor = random.choice(male_actors), number2= number2, number1 = number1) 
    #Needs to be multiple choice

    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"      

class g4_computation_fraction_subtraction():
    def __init__(self):
        factor = random.randint(2,10)
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 6) *factor 
        number3 = random.randint(2, 10)
        number4 = random.randint(2, 6) *factor 
        self.answer = (number1/number2) - (number3/number4)
        self.question = "What is the {key_word} between {number1}/{number2} and {number3}/{number4}?".format(key_word = key_words[4], 
                                                                                                       number1 = number1, 
                                                                                                       number2 = number2, 
                                                                                                 number3 = number3, 
                                                                                                       number4 = number4)
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"      


class g4_computation_multiplication_situps():
    def __init__(self):
        number1 = random.randint(10,40)
        number2= random.randint(2,10)
        number3= random.randint(2,10)
        self.answer = (number1 * number2) *number3
        self.question= "{male_actor} does {number1} sit-ups {number2} times per day. What is the total number of sit-ups {male_actor} does in {number3} days?".format(
    male_actor= random.choice(male_actors), number1 = number1, number2= number2, 
        number3= number3)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"      

class g4_computation_common_factor_word_problem():
    def __init__(self):
        factor = random.randint(2, 10)
        number1 = random.randint(2,10)*factor
        number2= random.randint(2,10)*factor
        number3= random.randint(2,10)*factor
        self.answer = common_factor(number1, number2, number3)
        self.question = "Which number is a {key_word} of {number1}, {number2}, and {number3}?".format(number1 = number1, 
                                                                                        number2= number2, 
                                                                                              number3= number3,
                                                                                             key_word= key_words[5])
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
#needs to be multiple choice

class g4_number_sense_decimal_place_value():
    #have no idea how to store answer from this 
    def __init__(self):
        number1=round(random.uniform(10, 20), 3)
        self.question = "What digit is in the {place_value} place in {number1}?".format(place_value= random.choice(decimal_place_values), 
                                                                                  number1=number1)
        self.answer = 1
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
#needs to be multiple choice

class g4_computation_division_statement():
    def __init__(self):
        number1 = random.randint(2,6)
        number2 = random.randint(7,11)
        self.answer = "{number1} divided by {number2}".format(number1=number1, number2=number2)
        self.question = "Which {key_word} statement represents {number1}/{number2}?".format(key_word = key_words[6], 
                                                                                      number1 = number1, number2 = number2)
    #Multiple choice would be good here
   
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"


#question 16 is a number line
#Can come back to this because there is a nice number line function

class g4_number_sense_place_value_big_number():
    #Also have no idea how to store this answer
    def __init__(self):
        number1 = random.randint(100, 999)
        number2 = random.randint(100, 999)
        self.question = "Identify the {key_word} for each digit in the number {number1},{number2}.".format(key_word = key_words[7], 
                                                                                          number1 = number1, 
                                                                                              number2 = number2)
        self.answer = 1
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_number_sense_decimal_largest_value():
    def __init__(self):
        number1 = round(random.uniform(13, 14), 2)
        number2 = round(random.uniform(13, 14), 2)
        number3 = round(random.uniform(13, 14), 2)
        number4 = round(random.uniform(13, 14), 2)
        size = random.choice(sizes)
        if size == "largest":  
            self.answer = max(number1, number2, number3, number4)
        if size == "smallest":  
            self.answer = min(number1, number2, number3, number4)
        self.question= "Which of the four following numbers is {size}? {number1}, {number2}, {number3}, {number4}".format(
    size = size, number1 = number1, number2 = number2, 
    number3 = number3, number4 = number4)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

#Question 19 needs to be multiple choice- it is a comparison of multiple numbers asking which is true

class g4_number_sense_decimal_in_words():
    #Question 20 - also ideally multiple choice- but would be really hard to convert to that. Answer is pretty good but doesn't read like SOL does
    def __init__(self):
        number = round(random.uniform(1, 10), 2)
        self.answer = num2words(number)
        self.question = "How is {number} written in words?".format(number = number)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_number_sense_round_big_number():
    #Don't know how to store this answer 
    def __init__(self):
        number1= random.randint(1,9)
        number2= random.randint(100,999)
        number3=random.randint(100,999)
        self.question= "What is {number1},{number2},{number3} rounded to the nearest {place_value}?".format(place_value = random.choice(whole_place_values), number1= number1, 
                                                                                                     number2= number2, number3= number3)
        self.answer = 1

    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
        
        
#question 22 is about equivalent fractions but it is an image

#question 23 is also a fraction picture

class g4_number_sense_fraction_ordering():
    #Question 24 would be better as a drag and drop 
    #don't know how to store this answer
    def __init__(self):
        num1= random.randint(1,9)
        num2= random.randint(1,9)
        num3= random.randint(1,9)
        num4 = random.randint(1,9)
        num5= random.randint(1,9)
        num6= random.randint(1,9)
        self.question = "Order these fractions from least to greatest: {num1}/{num2}, {num3}/{num4}, {num5}/{num6}".format(
            num1= num1, num2= num2, num3= num3, num4 = num4, 
            num5= num5, num6= num6)
        self.answer = 1
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_number_sense_decimal_round_hundredth():
    def __init__(self):
        number1 = round(random.uniform(1, 10), 2)
        self.answer = 1
        self.question = "Which number, when rounded to the nearest hundredth, is equal to {number1}?".format(number1 = number1)
    # Needs to be multiple choice
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

    
class g4_geometry_shapes_four_angles():
    def __init__(self):
        self.question = "Which figure has less than four angles?"
        self.answer= 1
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"
    #needs to be multiple choice 

#question 27 is a picture of a comb asking about length 

#question 28 is about parallel lines

class g4_measurement_pounds_to_ounces():
    def __init__(self):
        number1 = random.randint(1,9)
        self.answer = number1*16
        self.question = "{female_actor}'s {pet} weighed {number1} pounds. What is the total number of ounces {female_actor}'s {pet} weighed?".format(number1 = number1, female_actor = random.choice(female_actors), pet = random.choice(pets))
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

#30 is about figures that are congruent

class g4_measurement_gallons_to_pints():
    def __init__(self):
        number1 = random.randint(2,9)
        self.answer = number1*8
        self.question = "{female_actor} has {number1} gallons of {drink}. What is the total number of pints of {drink} {female_pronoun} has?".format(number1 = number1, female_actor = random.choice(female_actors), drink = random.choice(drinks), female_pronoun= female_pronouns[0])
        
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

class g4_measurement_time_elapsed_sports_team():
    def __init__(self):
        hour1 = random.randint(1,4)
        hour2 = random.randint(5,11)
        minute1 = random.randint(10,60)
        minute2 = random.randint(10,60)
        time1 = (hour1*60) + minute1
        time2= (hour2*60) + minute2
        self.answer = (time2 - time1)/60
        #not sure how to log the answer here- looks right but would need to double check and the formatting might need to change, consider changing so there can be less than 10 minutes in minute
        self.question = "A {sports} team left the school at {hour1}:{minute1} P.M. and returned at {hour2}:{minute2} P.M. What was the total amount of time that passed between the time this team left and returned to the school?".format(sports = random.choice(sports), hour1= hour1, 
        minute1=minute1, hour2=hour2, minute2=minute2)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

##Not sure how to put 33 into a question- asks for objects that weigh 1 KG - would need to be multiple choice
#34 is a picture problem
#35 is also a picture

class g4_measurement_meters_to_millimeters():
    def __init__(self):
        number1 = random.randint(1,9)
        unit = random.choice(metric_system)
        if unit =="millimeters":
            self.answer = number1*1000
        if unit == "centimeters":
            self.answer = number1 *100
        self.question = "{number} meters = ___ {unit}".format(number=number1, unit = unit)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

#37 is a graphical picture
#38 is also a picture for measurement and geometry
#39 is also a picture

#40 needs to be multiple choice- multiple equations and asking which is true- this is my best try:
class g4_algebra_make_equation_true():
    def __init__(self):
        number1 = random.randint(1,9) 
        number2 = random.randint(9,12) * number1
        self.answer = number2/number1
        self.question = "Which number makes this equation true? {number1} X ___ = {number2}".format(number1=number1, number2=number2)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "Your answer is incorrect. Please try again!"

#41 needs to be a point and click graph- don't know how to build one but know it is possible
