import random
import pandas as pd
#from fractions import Fraction
import math
from num2words import num2words
import inspect
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as dis

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
decimal_place_values = ["ones", "tenths", "hundredths", "thousandths"]
decimal_place_values_singular = ["whole number", "tenth", "hundredth", "thousandth"]
whole_place_values = ["ones", "tens", "hundreds", "thousands", "ten thousands", "hundred thousands", "millions"]
whole_place_values_no_ones = ["ten", "hundred", "thousand", "ten thousand", "hundred thousand", "million"]
times = ['fastest', 'slowest']
sizes = ['largest', 'smallest']
pets = ['dog', 'cat', 'puppy', 'turtle', 'bunny']
sports = ['basketball', 'soccer', 'football', 'lacrosse', 'volleyball', 'field hockey', 'tennis', 'swimming', 'track']
metric_system = ['centimeters', 'millimeters']
angle_numbers = ['four', 'five', 'six', 'seven', 'eight', 'nine']
shapes = ['triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'decagon']
    
    
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
            feedback = print("You didn't get the right answer this time. Keep trying and don't give up!")
            student_answer = input("Please enter your answer here:")
            return feedback, student_answer
            student_input_integer(student_answer, answer)

def placeValue(N, digit_num):
    number = str(N)
    number = number[::-1]
    number = list(number)
    return int(number[digit_num])*10**digit_num

def get_digit(number, n):
    return number // 10**n % 10

def common_factor(num1,num2,num3):
    n=[]
    for i in range(1, min(num1, num2, num3)+1): 
        if num1%i==num2%i==num3%i==0: 
            n.append(i)
    return n

def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr-input_value)).argmin()
    return i

class g4_functions_weather_graph():
    def __init__(self):
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Graph"
        self.attr3 = 4
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
        day1= random.randint(0,70)
        day2=random.randint(0,70)
        day3=random.randint(0,70)
        day4=random.randint(0,70)
        self.temperatures = [day1, day2, day3, day4]
        target_val = random.randint(0,70)
        i =closest_value(self.temperatures, target_val)
        self.answer = self.days[i]
        self.question = "This graph shows the morning temperature in a city for each of four days. The morning temperature on Thursday was {target} degrees F. Based on the data in this graph, which day had a temperature closest to Thursday's temperature?".format(target= target_val)
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            wrong = random.choice(self.days)
            if wrong != self.answer and wrong not in self.wrong_answers:
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        plt.plot(self.days, self.temperatures)
        plt.title('Morning Temperature')
        plt.xlabel('Day')
        plt.ylabel('Temperature (Degrees F)')
        plt.show()
        return self.question
        

    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_number_sense_identify_fraction_number_line():

    def __init__(self):
        self.attr1="Number and Number Sense"
        self.attr2= "Fraction Number Line"
        self.attr3 = 4
        self.px = random.randint(0,10)
        if self.px<.625 and self.px>0:
            self.answer = 0

        if self.px>.625 and self.px<1.875:
            self.answer = 1/8

        if self.px>1.875 and self.px<3.125:
            self.answer = 1/4

        if self.px>3.125 and self.px<4.375:
            self.answer = 3/8

        if self.px>4.375 and self.px< 5.625 :
            self.answer = 1/2

        if self.px>5.625 and self.px<6.875:
            self.answer = 5/8

        if self.px>6.875 and self.px<8.125:
            self.answer = 3/4

        if self.px>8.125 and self.px<9.375:
            self.answer = 7/8

        if self.px>9.375 :
            self.answer = 1
        self.question = "Which fraction on the number line is the red point closest to?"
            
    def print_question(self):
        #set up figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)

        # draw lines
        xmin = 0
        xmax = 10
        xmid = 5
        xquarter1 = 2.5
        xeighth1 = 1.25
        xquarter3 = 7.5
        xeighth3 = 3.75
        xeighth5 = 6.25
        xeighth7= 8.75
        y = 5
        height = 1

        plt.hlines(y, xmin, xmax)
        plt.vlines(xmin, y - height / 2., y + height / 2.)
        plt.vlines(xmax, y - height / 2., y + height / 2.)
        plt.vlines(xmid, y-height/2., y+height/2.)
        plt.vlines(xquarter1, y-height/2., y+height/2.)
        plt.vlines(xquarter3, y-height/2., y+height/2.)
        plt.vlines(xeighth1, y-height/2., y+height/2.)
        plt.vlines(xeighth3, y-height/2., y+height/2.)
        plt.vlines(xeighth5, y-height/2., y+height/2.)
        plt.vlines(xeighth7, y-height/2., y+height/2.)

        # draw a point on the line
        plt.plot(self.px,y, 'ro', ms = 15, mfc = 'r')

        # add numbers
        plt.text(xmin, y-.9, '0', horizontalalignment='center')
        plt.text(xmax, y-.9, '1', horizontalalignment='center')
        plt.text(xmid, y-.9, '1/2', horizontalalignment='center')

        plt.axis('off')
        plt.show()
        return self.question
        
        
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_probability_coin_flip_number_line():

    def __init__(self):
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Probability"
        self.attr3 = 4
        self.px = 5
        self.answer = 1/2
        self.question = "{female_actor} has a coin with one side heads and one side tails. Which letter on this number line best represents the probability that this coin flipped one time will land with tails facing up?".format(female_actor= random.choice(female_actors))
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            wrong = random.randint(1,10)
            if wrong != self.px and wrong not in self.wrong_answers:
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
            
    def print_question(self):
        #set up figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)

        # draw lines
        xmin = 0
        xmax = 10
        xmid = 5
        xquarter1 = 2.5
        xeighth1 = 1.25
        xquarter3 = 7.5
        xeighth3 = 3.75
        xeighth5 = 6.25
        xeighth7= 8.75
        y = 5
        height = 1

        plt.hlines(y, xmin, xmax)
        plt.vlines(xmin, y - height / 2., y + height / 2.)
        plt.vlines(xmax, y - height / 2., y + height / 2.)
        plt.vlines(xmid, y-height/2., y+height/2.)
        plt.vlines(xquarter1, y-height/2., y+height/2.)
        plt.vlines(xquarter3, y-height/2., y+height/2.)
        plt.vlines(xeighth1, y-height/2., y+height/2.)
        plt.vlines(xeighth3, y-height/2., y+height/2.)
        plt.vlines(xeighth5, y-height/2., y+height/2.)
        plt.vlines(xeighth7, y-height/2., y+height/2.)

        # draw a point on the line
        plt.plot(self.px,y, 'ro', ms = 5, mfc = 'r')
        plt.annotate(['a', 'b', 'c', 'd'][self.correct_index], (self.px,y), xytext= (self.px - 1, y + 1), 
                 arrowprops=dict(facecolor='black', shrink=0.1), 
                 horizontalalignment='center' )
        for i in self.wrong_answers:
            plt.plot(i,y,'ro', ms=5, mfc='r')
            self.incorrect_index = self.choices.index(i)
            self.incorrect_letter = ['a', 'b', 'c', 'd'][self.incorrect_index]
            plt.annotate(self.incorrect_letter, (i,y), xytext= (i - 1, y + 1), 
                 arrowprops=dict(facecolor='black', shrink=0.1), 
                 horizontalalignment='center' )


        # add numbers
        plt.text(xmin, y-.9, '0', horizontalalignment='center')
        plt.text(xmax, y-.9, '1', horizontalalignment='center')
        plt.text(xmid, y-.9, '1/2', horizontalalignment='center')

        plt.axis('off')
        plt.show()
        return self.question
        #student inputs answer directly 
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_probability_dice_roll_number_line():

    def __init__(self):
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Probability"
        self.attr3 = 4
        self.px = 1.666666666666666666666666666666667
        self.answer = 1/6
        self.question = "{male_actor} rolls a fair number cube labeled 1 through 6. Which point represents the probability that he will roll a {number} on the first roll?".format(male_actor= random.choice(male_actors), number= random.randint(1,6))
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            wrong = random.randint(1,10)
            if wrong != self.px and wrong not in self.wrong_answers:
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
            
    def print_question(self):
        #set up figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)

        # draw lines
        xmin = 0
        xmax = 10
        xmid = 5
        xquarter1 = 2.5
        xeighth1 = 1.25
        xquarter3 = 7.5
        xeighth3 = 3.75
        xeighth5 = 6.25
        xeighth7= 8.75
        y = 5
        height = 1

        plt.hlines(y, xmin, xmax)
        plt.vlines(xmin, y - height / 2., y + height / 2.)
        plt.vlines(xmax, y - height / 2., y + height / 2.)
        plt.vlines(xmid, y-height/2., y+height/2.)
        plt.vlines(xquarter1, y-height/2., y+height/2.)
        plt.vlines(xquarter3, y-height/2., y+height/2.)
        plt.vlines(xeighth1, y-height/2., y+height/2.)
        plt.vlines(xeighth3, y-height/2., y+height/2.)
        plt.vlines(xeighth5, y-height/2., y+height/2.)
        plt.vlines(xeighth7, y-height/2., y+height/2.)

        # draw a point on the line
        plt.plot(self.px,y, 'ro', ms = 5, mfc = 'r')
        plt.annotate(['a', 'b', 'c', 'd'][self.correct_index], (self.px,y), xytext= (self.px - 1, y + 1), 
                 arrowprops=dict(facecolor='black', shrink=0.1), 
                 horizontalalignment='center' )
        for i in self.wrong_answers:
            plt.plot(i,y,'ro', ms=5, mfc='r')
            self.incorrect_index = self.choices.index(i)
            self.incorrect_letter = ['a', 'b', 'c', 'd'][self.incorrect_index]
            plt.annotate(self.incorrect_letter, (i,y), xytext= (i - 1, y + 1), 
                 arrowprops=dict(facecolor='black', shrink=0.1), 
                 horizontalalignment='center' )

        # add numbers
        plt.text(xmin, y-.9, '0', horizontalalignment='center')
        plt.text(xmax, y-.9, '1', horizontalalignment='center')
        plt.text(xmid, y-.9, '1/2', horizontalalignment='center')

        plt.axis('off')
        plt.show()
        return self.question
        #student inputs answer directly 
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_computation_multiplication_specific_method():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 10)
        self.answer = number1 * number2
        self.question= "Use {method} to find {number1} X {number2}.".format(method = random.choice(methods), number1 = number1, number2 = number2)
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=10,size=100)
        wrong2 = np.random.randint(low = 2,high=10,size=100)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_computation_multiplication_male_bags():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question = "{male_actor} has {number1} bags of {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 male_actor = random.choice(male_actors), 
                                                                                                                                 male_pronoun = male_pronouns[0])
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=20,size=10)
        wrong2 = np.random.randint(low = 2,high=20,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
    
class g4_computation_multiplication_female_bags():
    def __init__(self):

        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1*number2
        self.question = "{female_actor} has {number1} bags of {number2} {thing}. How many {thing} does {female_pronoun} have?".format(thing = random.choice(bag_objects), number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 female_actor = random.choice(female_actors), 
                                                                                                                                 female_pronoun = female_pronouns[0])
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=20,size=10)
        wrong2 = np.random.randint(low = 2,high=20,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
    

class g4_computation_multiplication_double_bags():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
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
        self.wrong_answers = []
        wrong = number1 + number2 + number3+number4
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=20,size=10)
        wrong2 = np.random.randint(low = 2,high=20,size=10)
        wrong3=np.random.randint(low = 2,high=20,size=10)
        wrong4= np.random.randint(low = 2,high=20,size=10)
        wrong_1 = wrong1*wrong2 
        wrong_2 = wrong3*wrong4
        wrong = wrong_1+wrong_2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
        
class g4_computation_multiplication_fortnite():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1= random.randint(2, 20)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question= "{male_actor} has {number1} profiles with {number2} {thing}. How many {thing} does {male_pronoun} have?".format(thing = other_objects[0], number1= number1, 
                                                                                                                                 number2 = number2,
                                                                                                                                 male_actor = random.choice(male_actors), 
                                                                                                                                 male_pronoun = male_pronouns[0])
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=20,size=10)
        wrong2 = np.random.randint(low = 2,high=20,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        

#This will generate a table of different decimal race times students will have the choose the highest or lowest value of 
class g4_number_sense__comparison_running_table():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Decimal Comparison"
        self.attr3 = 4
        question_data = [[random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                            [random.choice(female_actors), round(random.uniform(13, 14), 2)], 
                            [random.choice(male_actors), round(random.uniform(13, 14), 2)], 
                           [random.choice(female_actors), round(random.uniform(13, 14), 2)]]
        time = random.choice(times)
        self.question_df = pd.DataFrame(question_data, columns=['Name', 'Time (in seconds)'])
        self.markdown_table = f'''| Name  | Time (in seconds) |
|-------|-------------------|
| {question_data[0][0]} | {question_data[0][1]}|
| {question_data[1][0]} | {question_data[1][1]}|
| {question_data[2][0]} | {question_data[2][1]}|
| {question_data[3][0]}  | {question_data[3][1]}|'''  
        if time == "fastest":
            self.answer = max(self.question_df['Time (in seconds)'])
        if time =="slowest":
            self.answer = min(self.question_df['Time (in seconds)'])
        self.question = "The table shows the time it took 4 students to run a 40 meter race. Which time was the {time} time?".format(time = time)
        self.choices = self.question_df['Time (in seconds)'].tolist()
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        dis.display(dis.Markdown(self.markdown_table))
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_computation_big_num_subtraction():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Addition/Subtraction"
        self.attr3 = 4
        number1 = random.randint(5001,12001)
        number2 = random.randint(1001,4999)
        answer = number1 - number2
        if answer>9999:
            answer = str(answer)
            self.answer = answer[0:2] + "," + answer[2:5]
        elif answer<=9999 and answer>=1000:
            answer = str(answer)
            self.answer = answer[0]+ "," +answer[1:4]
        else:
            self.answer= answer
        number1 = str(number1)
        number2 = str(number2)
        formatted_number1 = number1[0] + "," + number1[1:4]
        formatted_number2 = number2[0] + "," + number2[1:4]
        self.question = "{number1} - {number2} = ___".format(number1 = formatted_number1, number2 = formatted_number2)
        self.wrong_answers = []
        wrong1 = np.random.randint(low = 5001,high=12001,size=10)
        wrong2 = np.random.randint(low = 1001,high=4999,size=10)
        wrong = wrong1-wrong2
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            if i>9999:
                i = str(i)
                i = i[0:2] + "," + i[2:5]
            elif i<=9999 and i>=1000:
                i = str(i)
                i = i[0]+ "," +i[1:4]
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_computation_big_num_addition():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Addition/Subtraction"
        self.attr3 = 4
        number1 = random.randint(1001,9999)
        number2 = random.randint(1001,9999)
        answer = number1 + number2
        if answer>9999:
            answer = str(answer)
            self.answer = answer[0:2] + "," + answer[2:5]
        elif answer<=9999 and answer>=1000:
            answer = str(answer)
            self.answer = answer[0]+ "," +answer[1:4]
        else:
            self.answer= answer
        number1 = str(number1)
        number2 = str(number2)
        formatted_number1 = number1[0] + "," + number1[1:4]
        formatted_number2 = number2[0] + "," + number2[1:4]
        self.question = "{number1} + {number2} = ___".format(number1 = formatted_number1, number2 = formatted_number2)
        self.wrong_answers = []
        wrong1 = np.random.randint(low = 1001,high=9999,size=10)
        wrong2 = np.random.randint(low = 1001,high=9999,size=10)
        wrong = wrong1+wrong2
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            if i>9999:
                i = str(i)
                i = i[0:2] + "," + i[2:5]
            elif i<=9999 and i>=1000:
                i = str(i)
                i = i[0]+ "," +i[1:4]
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_computation_decimal_addition():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Decimal Addition/Subtraction"
        self.attr3 = 4
        number1 = round(random.uniform(10, 20), 1)
        number2 = round(random.uniform(10, 20), 1)
        self.answer = number1 + number2
        self.question = "{number1} + {number2} = ___".format(number1 = number1, number2 = number2)
        self.wrong_answers = []
        wrong1 = np.random.uniform(low = 10,high=20,size=10)
        wrong2 = np.random.uniform(low = 10,high=20,size=10)
        wrong1 = np.round(wrong1, 1)
        wrong2 = np.round(wrong2, 1)
        wrong = wrong1+wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
       
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"


# Not sure how to convert to MC 
class g4_computation_fraction_addition():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Fraction Addition/Subtraction"
        self.attr3 = 4
        factor = random.randint(2,10)
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 6) *factor 
        number3 = random.randint(1, 10)
        number4 = random.randint(1, 6) *factor 
        commondenom = math.lcm(number2, number4)
        while commondenom>20:
            factor = random.randint(2,10)
            number2 = random.randint(2, 6) *factor 
            number4 = random.randint(2, 6) *factor 
            commondenom = math.lcm(number2,number4)
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
            return "You didn't get the right answer this time. Keep trying and don't give up!"
       

class g4_computation_decimal_subtraction_drinks(): 
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Decimal Addition/Subtraction"
        self.attr3 = 4
        number1 = round(random.uniform(1, 2), 2)
        number2 = round(random.uniform(0, .99), 3)
        self.answer = number1 - number2
        self.question = "{male_actor} drinks {number1} liters of {drink}. {female_actor} drinks {number2} liters of {drink}. How much more {drink} does {male_actor} drink than {female_actor}?".format(drink = drinks[0], 
    number1 = number1, number2 = number2, male_actor = random.choice(male_actors), 
    female_actor = random.choice(female_actors))
        self.wrong_answers = []
        wrong1 = np.random.uniform(low = 1,high=2,size=10)
        wrong2 = np.random.uniform(low = 0,high=.99,size=10)
        wrong1 = np.round(wrong1, 2)
        wrong2 = np.round(wrong2, 3)
        wrong = wrong1-wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

#Weary about the numbers I chose here
class g4_computation_lcm_word_problem():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Least Common Multiple"
        self.attr3 = 4
        number2 = random.randint(2, 6)
        number1 = random.randint(1, 6)*number2
        number3 = random.randint(1, 6)*number2
        self.answer = math.lcm(number1, number3)
        self.question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[1], number1 = number1, number2 = number3)
        self.wrong_answers = []
        wrong1 = np.random.randint(low = 2,high=6,size=10)
        wrong2 = np.random.randint(low = 1,high=6,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_computation_multiplication_two_digit_word_problem():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(20, 100)
        number2 = random.randint(20, 100)
        answer = number1 * number2
        if  answer>9999:
                self.answer = str(answer)
                self.answer = self.answer[0:2] + "," + self.answer[2:5]
        elif answer<=9999 and answer>=1000:
                self.answer = str(answer)
                self.answer = self.answer[0]+ "," +self.answer[1:4]
        else:
            self.answer=answer
        self.question = "What is the {key_word} of {number1} and {number2}?".format(key_word = key_words[2], number1 = number1, number2 = number2)
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 20,high=100,size=10)
        wrong2 = np.random.randint(low = 20,high=100,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            if i>9999:
                i = str(i)
                i = i[0:2] + "," + i[2:5]
            elif i<=9999 and i>=1000:
                i = str(i)
                i = i[0]+ "," +i[1:4]
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"
        
class g4_computation_multiplication_with_drinks():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 20)
        self.answer = number1 * number2
        self.question= "{female_actor} poured {number1} ounces of {drink} into each of {number2} glasses. Exactly how many ounces of {drink} did {female_actor} pour into all of these glasses?".format(
    drink = drinks[0], female_actor = random.choice(female_actors), number1 = number1, number2 = number2)
        self.wrong_answers = []
        wrong = number1 + number2
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=20,size=10)
        wrong2 = np.random.randint(low = 2,high=10,size=10)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"  

class g4_estimation_multiplication_store():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(10, 30)
        number2 = random.randint(10, 90)
        answer = round(number1*number2, -2)
        if answer >=1000:
            self.answer= str(answer)
            self.answer = "$"+self.answer[0]+"," +self.answer[1:]
        elif answer<1000:
            self.answer= str(answer)
            self.answer = "$"+self.answer
        self.question = "At a store, {thing} cost ${number1} each. Which is closest to the {key_word} of {number2} {thing}?".format(number1 = number1, number2 = number2, thing =       random.choice(things), key_word = key_words[3])
        self.wrong_answers = []
        wrong = number1 + number2
        wrong= "$"+str(wrong)
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 10,high=30,size=10)
        wrong2 = np.random.randint(low = 10,high=90,size=10)
        wrong = wrong1*wrong2
        wrong = np.round(wrong, -2)
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            if i>=1000:
                i= str(i)
                i= "$"+i[0]+","+ i[1:]
            elif i<1000:
                i = str(i)
                i = "$"+i
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_computation_multiplication_selling_items():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(100,999)
        number2 = random.randint(2,10)
        answer = number1*number2
        if answer >=1000:
            answer= str(answer)
            self.answer = "$"+answer[0]+"," +answer[1:]
        elif answer<1000:
            answer= str(answer)
            self.answer = "$"+answer
        self.question = "{female_actor} sold {number1} {thing}. Each box cost ${number2}. What was the {key_word} of all the {thing} sold?".format(number1 = number1, number2 = number2, thing = random.choice(things), key_word = key_words[3], female_actor = random.choice(female_actors))
        self.wrong_answers = []
        wrong = number1 + number2
        wrong= "$"+str(wrong)
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 100,high=999,size=200)
        wrong2 = np.random.randint(low = 2,high=10,size=200)
        wrong = wrong1*wrong2
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            if i>=1000:
                i= str(i)
                i= "$"+i[0]+","+ i[1:]
            elif i<1000:
                i = str(i)
                i = "$"+i
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"    


class g4_computation_subtraction_word_problem():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Addition/Subtraction"
        self.attr3 = 4
        number1= random.randint(1000,5000)
        number2 = random.randint(100,999)
        answer = number1 - number2
        if answer>9999:
            answer = str(answer)
            self.answer = answer[0:2] + "," + answer[2:5]
        elif answer<=9999 and answer>=1000:
            answer = str(answer)
            self.answer = answer[0]+ "," +answer[1:4]
        else:
            self.answer= answer
        number1 = str(number1)
        formatted_number1 = number1[0] + "," + number1[1:4]
        self.question = "What is the {key_word} between {number1} and {number2}?".format(number2 = number2, 
                                                                                  key_word = key_words[4], number1= formatted_number1)
        self.wrong_answers = []
        wrong1 = np.random.randint(low = 1000,high=5000,size=10)
        wrong2 = np.random.randint(low = 100,high=999,size=10)
        wrong = wrong1-wrong2
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            if i>9999:
                i = str(i)
                i = i[0:2] + "," + i[2:5]
            elif i<=9999 and i>=1000:
                i = str(i)
                i = i[0]+ "," +i[1:4]
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"    



        
#same problem with fractions
class g4_computation_fraction_subtraction():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Fraction Addition/Subtraction"
        self.attr3 = 4
        factor = random.randint(2,10)
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 6) *factor 
        number3 = random.randint(2, 10)
        number4 = random.randint(2, 6) *factor 
        commondenom=math.lcm(number2,number4)
        while commondenom>20:
            factor = random.randint(2,10)
            number2 = random.randint(2, 6) *factor 
            number4 = random.randint(2, 6) *factor 
            commondenom = math.lcm(number2,number4)
        self.answer = abs((number1/number2) - (number3/number4))
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
            return "You didn't get the right answer this time. Keep trying and don't give up!"      


class g4_computation_multiplication_situps():
    def __init__(self):
        
        self.attr1= "Computation and Estimation"
        self.attr2 = "Multiplication"
        self.attr3 = 4
        number1 = random.randint(10,40)
        number2= random.randint(2,10)
        number3= random.randint(2,10)
        answer = (number1 * number2) *number3
        if  answer>9999:
                self.answer = str(answer)
                self.answer = self.answer[0:2] + "," + self.answer[2:5]
        elif answer<=9999 and answer>=1000:
                self.answer = str(answer)
                self.answer = self.answer[0]+ "," +self.answer[1:4]
        else: 
            self.answer = answer
        self.question= "{male_actor} does {number1} sit-ups {number2} times per day. What is the total number of sit-ups {male_actor} does in {number3} days?".format(
    male_actor= random.choice(male_actors), number1 = number1, number2= number2, 
        number3= number3)
        self.wrong_answers = []
        wrong = number1 + number2 + number3
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 10,high=40,size=100)
        wrong2 = np.random.randint(low = 2,high=10,size=100)
        wrong3 = np.random.randint(low = 2,high=10,size=100)
        wrong = (wrong1*wrong2)*wrong3
        wrong = np.unique(wrong[wrong!=answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            if i>9999:
                i = str(i)
                i = i[0:2] + "," + i[2:5]
            elif i<=9999 and i>=1000:
                i = str(i)
                i = i[0]+ "," +i[1:4]
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_computation_largest_common_factor_word_problem():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Common Factor"
        self.attr3 = 4
        factor = random.randint(2, 10)
        number1 = random.randint(2,10)*factor
        number2= random.randint(2,10)*factor
        number3= random.randint(2,10)*factor
        common_factors = common_factor(number1, number2, number3)
        self.answer = max(common_factors)
        self.question = "Which number is the largest common factor of {number1}, {number2}, and {number3}?".format(number1 = number1, 
                                                                                        number2= number2, 
                                                                                              number3= number3)
        self.wrong_answers = []
        wrong = np.random.randint(low = 2,high=10,size=12)
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:3].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_number_sense_decimal_place_value():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Decimal Place Value"
        self.attr3 = 4
        number1=round(random.uniform(10, 20), 3)
        place_value= random.choice(decimal_place_values)
        self.question = "What digit is in the {place_value} place in {number1}?".format(place_value= place_value, 
                                                                                  number1=number1)
        number1= number1+0.00001
        if place_value == "ones":
            self.answer = int(get_digit(number1, 0))
            
        if place_value == "tenths":
            self.answer= int(get_digit(number1, -1))
            
        if place_value == "hundredths":
            self.answer= int(get_digit(number1, -2))
            
        if place_value == "thousandths":
            self.answer= int(get_digit(number1, -3))
      
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            place_value = random.choice(decimal_place_values)

            if place_value == "ones":
                wrong = int(get_digit(number1, 0))
            
            if place_value == "tenths":
                wrong= int(get_digit(number1, -1))
                
            if place_value == "hundredths":
                wrong= int(get_digit(number1, -2))
                
            if place_value == "thousandths":
                wrong= int(get_digit(number1, -3))
            
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
            
            elif wrong == self.answer or wrong in self.wrong_answers:
                digit = random.randint(1,9)
                if digit != self.answer and digit not in self.wrong_answers:
                    self.wrong_answers.append(digit)
    
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_computation_division_statement():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Division"
        self.attr3 = 4
        number1 = random.randint(2,6)
        number2 = random.randint(7,11)
        self.answer = "{number1} divided by {number2}".format(number1=number1, number2=number2)
        self.question = "Which {key_word} statement represents {number1}/{number2}?".format(key_word = key_words[6], 
                                                                                      number1 = number1, number2 = number2)
        self.wrong_answers = []
        wrong = "{number1} divided by {number2}".format(number1=number2, number2=number1)
        self.wrong_answers.append(wrong)
        while len(self.wrong_answers)<3:
            number1 = random.randint(2,6)
            number2 = random.randint(7,11)
            wrong =  "{number1} divided by {number2}".format(number1=number1, number2=number2)
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_number_sense_place_value_big_number_digit():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Place Value"
        self.attr3 = 4
        number1 = random.randint(1000001,9999999)
        number = str(number1)
        formatted_number = number[0] + "," + number[1:4] + "," + number[4:]
        place_value = random.choice(whole_place_values)
        self.question = "What digit is in the {place_value} place in the number {number1}?".format(place_value = place_value, 
                                                                                          number1 = formatted_number)
        if place_value == "ones":
            self.answer= get_digit(number1,0)
        
        if place_value == "tens":
            self.answer= get_digit(number1,1)
        
        if place_value == "hundreds":
            self.answer= get_digit(number1,2)
            
        if place_value == "thousands":
            self.answer= get_digit(number1,3)
            
        if place_value == "ten thousands":
            self.answer= get_digit(number1,4)
            
        if place_value == "hundred thousands":
            self.answer= get_digit(number1,5)
            
        if place_value == "millions":
            self.answer= get_digit(number1,6)
        
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            place_value = random.choice(whole_place_values)
            if place_value == "ones":
                wrong= get_digit(number1,0)

            if place_value == "tens":
                wrong= get_digit(number1,1)

            if place_value == "hundreds":
                wrong= get_digit(number1,2)

            if place_value == "thousands":
                wrong= get_digit(number1,3)

            if place_value == "ten thousands":
                wrong= get_digit(number1,4)

            if place_value == "hundred thousands":
                wrong= get_digit(number1,5)
            
            if place_value == "millions":
                wrong= get_digit(number1,6)
            
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
            
            elif wrong == self.answer or wrong in self.wrong_answers:
                digit = random.randint(1,9)
                if digit != self.answer and digit not in self.wrong_answers:
                    self.wrong_answers.append(digit)
                    
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_number_sense_place_value_big_number_value():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Place Value"
        self.attr3 = 4
        number1 = random.randint(1000001,9999999)
        number = str(number1)
        formatted_number = number[0] + "," + number[1:4] + "," + number[4:]
        digit = random.randint(1,7)
        place = digit -1
        place_value = whole_place_values[place]
        d = get_digit(number1, digit-1)
        self.question = "What is the value of the {place} place in the number {number1}?".format(place=place_value, 
                                                                                          number1 = formatted_number)
        if digit==1:
            self.answer = placeValue(number1,0)
        
        if digit ==2:
            self.answer = placeValue(number1,1)
        
        if digit==3:
            self.answer = placeValue(number1,2)
            
        if digit==4:
            D= get_digit(number1,3)
            if D!=0:
                answer = placeValue(number1,3)
                answer= str(answer)
                self.answer = answer[0]+","+answer[1:]
            if D==0:
                self.answer=0
            
        if digit==5:
            D= get_digit(number1,4)
            if D!=0:
                answer = placeValue(number1,4)
                answer= str(answer)
                self.answer = answer[0:2]+","+answer[2:]
            if D==0:
                self.answer=0
                
        if digit==6:
            D= get_digit(number1,5)
            if D!=0:
                answer = placeValue(number1,5)
                answer= str(answer)
                self.answer = answer[0:3]+","+answer[3:]
            if D==0:
                self.answer=0
        
        if digit==7:
            D= get_digit(number1,6)
            if D!=0:
                answer = placeValue(number1,6)
                answer= str(answer)
                self.answer = answer[0]+","+answer[1:4] + "," + answer[4:]
            if D==0:
                self.answer=0
            
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            digit = random.randint(1,6)
            if digit==1:
                wrong = placeValue(number1,0)

            if digit ==2:
                wrong = placeValue(number1,1)

            if digit==3:
                wrong = placeValue(number1,2)

            if digit==4:
                D= get_digit(number1,3)
                if D!=0:
                    wrong = placeValue(number1,3)
                    wrong= str(wrong)
                    wrong = wrong[0:1]+","+wrong[1:]
                if D==0:
                    wrong=0

            if digit==5:
                D= get_digit(number1,4)
                if D!=0:
                    wrong = placeValue(number1,4)
                    wrong= str(wrong)
                    wrong = wrong[0:2]+","+wrong[2:]
                if D==0:
                    wrong=0

            if digit==6:
                D= get_digit(number1,5)
                if D!=0:
                    wrong = placeValue(number1,5)
                    wrong= str(wrong)
                    wrong = wrong[0:3]+","+wrong[3:]
                if D==0:
                    wrong=0

            if digit==7:
                D= get_digit(number1,6)
                if D != 0:
                    wrong = placeValue(number1,6)
                    wrong= str(wrong)
                    wrong = wrong[0]+","+wrong[1:4] + "," + wrong[4:]
                if D==0:
                    wrong= 0 

            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_number_sense_big_num_comparison():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Number Comparison"
        self.attr3 = 4
        number1 = random.randint(8400,8499)
        number2 = random.randint(8500,8599)
        number_one = str(number1)
        number_two = str(number2)
        formatted_number_one = number_one[0] + "," + number_one[1:]
        formatted_number_two = number_two[0] + "," + number_two[1:]
        self.answer = "{number1} < {number2}".format(number1=formatted_number_one, number2=formatted_number_two)
        self.question= "Which statement is true?"
        self.wrong_answers = []
        wrong = "{number1} < {number2}".format(number1=formatted_number_two, number2=formatted_number_one)
        self.wrong_answers.append(wrong)
        while len(self.wrong_answers)<3:
            number1 = random.randint(8200000,8299999)
            number2= random.randint(8300000, 8400000)
            number_one = str(number1)
            number_two = str(number2)
            formatted_number_one = number_one[0] + "," + number_one[1:4] + "," + number_one[4:]
            formatted_number_two = number_two[0] + "," + number_two[1:4] + "," + number_two[4:]
            wrong= "{number1} < {number2}".format(number1=formatted_number_two, number2=formatted_number_one)
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_number_sense_big_number_in_words():
    
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Number in Words"
        self.attr3 = 4
        number1 = random.randint(1000001, 9999999)
        self.answer = num2words(number1)
        number = str(number1)
        formatted_number = number[0] + "," + number[1:4] + "," + number[4:]
        self.question = "How is {number} written in words?".format(number = formatted_number)
        self.wrong_answers = []
        number_wrong = number1-100
        wrong = num2words(number_wrong)
        self.wrong_answers.append(wrong)
        number_wrong = number1 - 1000
        wrong = num2words(number_wrong)
        self.wrong_answers.append(wrong)
        number_wrong = number1 - random.randint(101,100000)
        wrong= num2words(number_wrong)
        self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        pd.set_option('max_colwidth', 600)
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"         

class g4_number_sense_decimal_in_words():
    
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Decimal in Words"
        self.attr3 = 4
        number = round(random.uniform(1, 10), 2)
        self.answer = num2words(number)
        self.question = "How is {number} written in words?".format(number = number)
        self.wrong_answers = []
        number = number-.01
        wrong = num2words(round(number,1))
        self.wrong_answers.append(wrong)
        wrong = num2words(round(number,2))
        self.wrong_answers.append(wrong)
        number = (number+.01)*100
        wrong= num2words(number)
        self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_number_sense_round_big_number():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Rounding"
        self.attr3 = 4
        number1= random.randint(1000001,9999999)
        number = str(number1)
        formatted_number = number[0] + "," + number[1:4] + "," + number[4:]
        place_value = random.choice(whole_place_values_no_ones)
        self.question= "What is {number} rounded to the nearest {place_value}?".format(place_value = place_value, number=formatted_number)
        
        if place_value == "ten":
            answer= round(number1, -1)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
        
        if place_value == "hundred":
            answer= round(number1, -2)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
            
        if place_value == "thousand":
            answer= round(number1, -3)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
            
        if place_value == "ten thousand":
            answer= round(number1,-4)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
            
        if place_value == "hundred thousand":
            answer= round(number1,-5)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
            
        if place_value == "million":
            answer= round(number1,-6)
            answer= str(answer)
            self.answer = answer[0] + "," + answer[1:4] + "," + answer[4:]
        
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            place_value = random.choice(whole_place_values_no_ones)

            if place_value == "ten":
                wrong= round(number1,-1)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]

            if place_value == "hundred":
                wrong= round(number1,-2)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]

            if place_value == "thousand":
                wrong= round(number1,-3)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]

            if place_value == "ten thousand":
                wrong= round(number1,-4)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]

            if place_value == "hundred thousand":
                wrong= round(number1,-5)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]
            
            if place_value == "million":
                wrong= round(number1,-6)
                wrong= str(wrong)
                wrong = wrong[0] + "," + wrong[1:4] + "," + wrong[4:]
            
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 
        
        
#question 22 is about equivalent fractions but it is an image

#question 23 is also a fraction picture

class g4_number_sense_fraction_ordering():
    #Question 24 would be better as a drag and drop 
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Fraction Ordering"
        self.attr3 = 4
        num1= random.randint(1,9)
        num2= random.randint(1,9)
        num3= random.randint(1,9)
        num4 = random.randint(1,9)
        num5= random.randint(1,9)
        num6= random.randint(1,9)
        numbers = [num1/num2, num3/num4, num5/num6]
        self.question = "Order these fractions from least to greatest: {num1}/{num2}, {num3}/{num4}, {num5}/{num6}".format(
            num1= num1, num2= num2, num3= num3, num4 = num4, 
            num5= num5, num6= num6)
        self.answer = sorted(numbers)
    
    def print_question(self):
        return self.question
    
    def student_answer(self, student_answer):
        if student_answer == self.answer:
            return "You got the right answer. Nice work!"
        if student_answer!= self.answer:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_number_sense_decimal_round():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Decimal Rounding"
        self.attr3 = 4
        place_value = random.choice(decimal_place_values_singular)
       
        number1= round(random.uniform(2, 10), 4)
        
        if place_value == "whole number":
            self.answer = round(number1,1)
            number = round(number1,0)
            
        if place_value == "tenth":
            self.answer = round(number1,2)
            number = round(number1,1)  
            
        if place_value == "hundredth":
            self.answer = round(number1,3)
            number = round(number1,2)
            
        if place_value == "thousandth":
            self.answer = round(number1,4)
            number = round(number1,3)
        self.question = "Which number, when rounded to the nearest {place}, is equal to {number}?".format(number = number, place=place_value)
    
        self.wrong_answers = []
        
        while len(self.wrong_answers)<3:
            place_value = random.choice(decimal_place_values_singular)
            
            if place_value == "whole number":
                number1=number1-1
                wrong = round(number1,1)
                
            if place_value == "tenth":
                number1=number1-.5
                wrong = round(number1,2)
                
            if place_value == "hundredth":
                number1=number1-.05
                wrong = round(number1,3)
                
            if place_value == "thousandth":
                number1=number1-.005
                wrong = round(number1,4)
            
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 


#Not sure if this is too hard
class g4_geometry_shapes_angles():
    def __init__(self):
        
        angles = random.choice(angle_numbers)
        self.attr1 = "Measurement and Geometry"
        self.attr2 = "Geometry"
        self.attr3 = 4
        self.question = "Which figure with less than {angles} angles has the most angles?".format(angles= angles)
        if angles == "four":
            self.answer= shapes[0]
        if angles == 'five':
            self.answer = shapes[1]
        if angles == 'six':
            self.answer = shapes[2]
        if angles == 'seven':
            self.answer= shapes[3]
        if angles == 'eight':
            self.answer= shapes[4]
        if angles == 'nine':
            self.answer = shapes[5]
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            wrong= random.choice(shapes)
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 


#question 27 is a picture of a comb asking about length 

#question 28 is about parallel lines

class g4_measurement_pounds_to_ounces():
    def __init__(self):
        
        self.attr1 = "Measurement and Geometry"
        self.attr2 = "Measurement"
        self.attr3 = 4
        number1 = random.randint(1,9)
        self.answer = number1*16
        self.question = "{female_actor}'s {pet} weighed {number1} pounds. What is the total number of ounces {female_actor}'s {pet} weighed?".format(number1 = number1, female_actor = random.choice(female_actors), pet = random.choice(pets))
        self.wrong_answers = []
        wrong = number1 + 16
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 1,high=9,size=10)
        wrong = wrong1*16
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

#30 is about figures that are congruent

class g4_measurement_gallons_to_pints():
    def __init__(self):
        
        self.attr1 = "Measurement and Geometry"
        self.attr2 = "Measurement"
        self.attr3 = 4
        number1 = random.randint(2,9)
        self.answer = number1*8
        self.question = "{female_actor} has {number1} gallons of {drink}. What is the total number of pints of {drink} {female_pronoun} has?".format(number1 = number1, female_actor = random.choice(female_actors), drink = random.choice(drinks), female_pronoun= female_pronouns[0])
        self.wrong_answers = []
        wrong = number1 + 8
        self.wrong_answers.append(wrong)
        wrong1 = np.random.randint(low = 2,high=9,size=10)
        wrong = wrong1*8
        wrong = np.unique(wrong[wrong!=self.answer])
        np.random.shuffle(wrong)
        wrong = wrong[0:2].tolist()
        for i in wrong:
            self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_measurement_time_elapsed_sports_team():
    def __init__(self):
        
        self.attr1 = "Measurement and Geometry"
        self.attr2 = "Time Elapsed"
        self.attr3 = 4
        hour1 = random.randint(1,4)
        hour2 = random.randint(5,11)
        minute1 = random.randint(10,59)
        minute2 = random.randint(10,59)
        time1 = (hour1*60) + minute1
        time2= (hour2*60) + minute2
        answer = (time2 - time1)/60
        remainder = answer - int(answer)
        hours = int(answer)
        minutes = remainder * 60
        minutes= round(minutes)
        self.answer = str(hours) + " hours " + str(minutes) + " minutes"
        #not sure how to log the answer here- looks right but would need to double check and the formatting might need to change, consider changing so there can be less than 10 minutes in minute
        self.question = "A {sports} team left the school at {hour1}:{minute1} P.M. and returned at {hour2}:{minute2} P.M. What was the total amount of time that passed between the time this team left and returned to the school?".format(sports = random.choice(sports), hour1= hour1, 
        minute1=minute1, hour2=hour2, minute2=minute2)
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            hour1 = random.randint(1,4)
            hour2 = random.randint(5,12)
            minute1 = random.randint(0,59)
            minute2 = random.randint(0,59)
            time1 = (hour1*60) + minute1
            time2= (hour2*60) + minute2
            answer = (time2 - time1)/60
            remainder = answer - int(answer)
            hours = int(answer)
            minutes = remainder * 60
            minutes= round(minutes)
            wrong= str(hours) + " hours " + str(minutes) + " minutes"
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

##Not sure how to put 33 into a question- asks for objects that weigh 1 KG - would need to be multiple choice
#34 is a picture problem
#35 is also a picture

class g4_measurement_meters_to_millimeters():
    def __init__(self):
        
        self.attr1 = "Measurement and Geometry"
        self.attr2 = "Measurement"
        self.attr3 = 4
        number1 = random.randint(2,9)
        unit = random.choice(metric_system)
        if unit =="millimeters":
            self.answer = number1*1000
        if unit == "centimeters":
            self.answer = number1 *100
        self.question = "{number} meters = ___ {unit}".format(number=number1, unit = unit)
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            number1 = random.randint(2,9)
            if unit =="millimeters":
                wrong = number1*1000
            if unit == "centimeters":
                wrong = number1 *100
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

#37 is a graphical picture
#38 is also a picture for measurement and geometry
#39 is also a picture

#40 needs to be multiple choice- multiple equations and asking which is true- this is my best try:
class g4_algebra_make_equation_true():
    def __init__(self):
        
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Algebra"
        self.attr3 = 4
        number1 = random.randint(1,9) 
        number2 = random.randint(9,12) * number1
        self.answer = int(number2/number1)
        self.question = "Which number makes this equation true? {number1} X ___ = {number2}".format(number1=number1, number2=number2)
        self.wrong_answers = []
        while len(self.wrong_answers)<3:
            wrong= random.randint(1,9) 
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

#41 needs to be a point and click graph- don't know how to build one but know it is possible

class g4_pattern_number_of_teams_table():
    def __init__(self):
        
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Patterns"
        self.attr3 = 4
        factor = random.randint(2,9)
        number1 = random.randint(2,4)*factor
        number1_b = int(number1/factor)
        number2 = random.randint(5,7)*factor
        number2_b = int(number2/factor)
        number3 = random.randint(8,10)*factor
        number3_b= int(number3/factor)
        number4 = random.randint(11,13)*factor
        self.answer = int(number4/factor)
        question_data = [[number1, number1_b], 
                            [number2, number2_b], 
                            [number3, number3_b], 
                           [number4, "?"]]
        self.markdown_table = f"""| Total Number of Players | Number of Teams |
|-------------------------|-----------------|
| {number1}               | {number1_b}               |
| {number2}               | {number2_b}               |
| {number3}                      | {number3_b}               |
| {number4}                      | ?               |"""
        self.question_df = pd.DataFrame(question_data, columns=['Total Number of Players', 'Number of Teams'])
        self.question = "The table shows the total number of players on different numbers of {sport} teams in a tournament. The pattern continues in the same way. How many {sport} teams are needed for a total of {number4} players?".format(number4=number4, sport = random.choice(sports))
        self.wrong_answers = []
        wrong = number4+factor
        self.wrong_answers.append(wrong)
        while len(self.wrong_answers)<3:
            factor = random.randint(2,9)
            number= random.randint(11,13)*factor
            wrong = int(number/factor)
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        dis.display(dis.Markdown(self.markdown_table))
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

#43 is a number line

#44 is a graph 

class g4_probability_no_chance():
    def __init__(self):
        
        self.attr1= "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Probability"
        self.attr3 = 4
        number = random.randint(1,9)
        name = random.choice(male_actors)
        self.question = "{name} has {number} blue, {number} red, {number} yellow, and {number} purple folders in his backpack. {name} reaches into his backpack and selects one folder without looking. What is the likelihood the folder will be green?".format(name = name, number = number)
        self.answer = "Impossible"
        self.wrong_answers = []
        wrong = "Likely, but not certain"
        self.wrong_answers.append(wrong)
        wrong = "Unlikely, but not impossible"
        self.wrong_answers.append(wrong)
        wrong = "Certain"
        self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

        
#46 and 47 need to be multiple choice
#48 is a point and click number line
#49 needs to print 4 random dfs 

class g4_pattern_increasing_numbers():
    def __init__(self):
    
        self.attr1 = "Probability, Statistics, Patterns, Functions, and Algebra"
        self.attr2 = "Patterns"
        self.attr3 = 4
        factor= random.randint(2,9)
        number1 = random.randint(2,9)
        number2 = number1 + factor
        number3= number2+ factor
        number4= number3+factor
        number5 = number4 +factor
        self.question = "This is an increasing pattern: {number1}, {number2}, {number3}, {number4}, {number5}. What rule does this pattern use?".format(number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)
        self.wrong_answers = []
        self.answer = "Add " + str(factor)
        while len(self.wrong_answers)<3:
            factor = random.randint(2,9)
            wrong = "Add " + str(factor)
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]

    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"

class g4_number_sense_decimal_largest_value():
    def __init__(self):
        
        self.attr1 = "Number and Number Sense"
        self.attr2 = "Decimal Comparison"
        self.attr3 = 4
        number1 = round(random.uniform(13, 14), 2)
        number2 = round(random.uniform(13, 14), 2)
        number3 = round(random.uniform(13, 14), 2)
        number4 = round(random.uniform(13, 14), 2)
        numbers = [number1, number2, number3, number4]
        size = random.choice(sizes)
        if size == "largest":  
            self.answer = max(number1, number2, number3, number4)
        if size == "smallest":  
            self.answer = min(number1, number2, number3, number4)
        self.question= "Which of the four following numbers is {size}? {number1}, {number2}, {number3}, {number4}".format(
    size = size, number1 = number1, number2 = number2, 
    number3 = number3, number4 = number4)
        self.wrong_answers = []
        for number in numbers:
            wrong = number
            if wrong != self.answer and wrong not in self.wrong_answers: 
                self.wrong_answers.append(wrong)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
        
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!" 

class g4_estimation_division_running_problem():
    def __init__(self):
        
        self.attr1 = "Computation and Estimation"
        self.attr2 = "Division"
        self.attr3 = 4
        number2 = random.randint(2, 10)
        number1 = random.randint(20,60)*number2
        answer = number1/number2
        self.answer= int(round(answer, -1))
   
        self.question = "{male_actor} ran a total of {number1} minutes in a {number2}-day period. He ran the same number of minutes each day. What is the closest to the number of minutes {male_actor} ran each day?".format(male_actor = random.choice(male_actors), number2= number2, number1 = number1) 
        self.wrong_answers = []
        wrong = [20, 30, 40, 50, 60]
        for i in wrong:
            if i != self.answer and len(self.wrong_answers)<=2:
                self.wrong_answers.append(i)
        self.choices = [self.answer] + self.wrong_answers
        random.shuffle(self.choices)
        self.correct_index = self.choices.index(self.answer)
        self.correct_letter = ['a', 'b', 'c', 'd'][self.correct_index]
       
    def print_question(self):
        return self.question
    
    def print_choices(self):
        d = pd.DataFrame(self.choices, ['a', 'b', 'c', 'd'])
        d.columns = ['']
        return d
    
    def student_answer(self, student_answer):
        if student_answer not in ['a', 'b', 'c', 'd']:
            return "Please type a, b, c, or d."
        if student_answer == self.correct_letter:
            return "You got the right answer. Nice work!"
        if student_answer!= self.correct_letter:
            return "You didn't get the right answer this time. Keep trying and don't give up!"   