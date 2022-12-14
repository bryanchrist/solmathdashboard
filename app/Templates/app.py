import dash
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
import templates
import inspect
import pandas as pd
import numpy as np
import warnings
import dash_bootstrap_components as dbc
import dash_table_experiments as dt
from dash.exceptions import PreventUpdate
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import json

classes = []
standards = []
topics = []
grade_levels = []
for name, obj in inspect.getmembers(templates):
    if inspect.isclass(obj):
        classes.append(obj)

for j in range(len(classes)):
    x = classes[j]()
    standard = x.attr1 
    topic = x.attr2 
    topics.append(topic)
    grade_level = x.attr3 
    standards.append(standard)
    grade_levels.append(grade_level)
    
df = pd.DataFrame({"Class": classes, "Grade_level": grade_levels, "Standard": standards, "Topic": topics})
df=df.reset_index()
df.to_csv("4th grade dataframe")

all_topics = list(df['Topic'])
topics = []
for x in all_topics:
    if x not in topics:
        topics.append(x)

markdown_text = '''
Please use this dashboard to select the type of Virginia Standards of Learning (SOL) 4th grade math questions you would like to practice. Once you select the SOL standard and click the create question button, a question will display directly on the webpage. Please insert your answers directly in the field provided and click the submit answer button. 

After answering the question, you can click create question as many times as you want to encounter unique questions. You can also easily change the standard and click create question to encounter questions from a different standard area.

Good luck!'''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H1("SOL Math Data Dashboard"),    
        
        dcc.Markdown(children = markdown_text),
        
        html.Div([
            
            html.H3("Grade"),

            dcc.RadioItems(id='grade_level',
                options=[4],
                value=4),

            html.H3("Standard"),

            dcc.RadioItems(id='standard',
                options=['Computation and Estimation','Number and Number Sense', 'Measurement and Geometry', 'Probability, Statistics, Patterns, Functions, and Algebra']),
            
            html.H3("Number of Questions"),
            
            html.Button(id='submit', n_clicks=0, children = 'Create Question', style = {'fontsize': '14'}),

        ], style={'width': '24%', 'float': 'left'}),
         html.Div([
            dcc.Markdown(id='question'),
            dcc.Markdown(id='markdown_table'),
            dcc.Graph(id='graph'),
            html.Img(id='image'), 
            dcc.Markdown(id='choices'),
            dcc.Input(id = 'student_answer', type='text', placeholder = "Enter your answer here.", debounce = True),
            html.Div(html.Button('Submit Answer', id= 'submit-val', n_clicks=0)),
            dcc.Markdown(id='feedback'),
            dcc.Store(id = 'correct_answer'),
            dcc.Store(id = 'correct_answer2'),
            dcc.Store(id = 'correct_answer3'),
            dcc.Store(id = 'topic'),
            dcc.Store(id = 'question_index'),
            dcc.Store(id='target_val')
        ], style={'width': '74%', 'float': 'right', 'font-weight': 'bold', 'font-size': '20px'})
        
        
    ]
)

@app.callback([Output(component_id="question",component_property="children"), 
               Output(component_id="choices",component_property="children"), 
              Output(component_id = 'correct_answer', component_property = 'data'),
              Output(component_id='topic', component_property='data'), 
              Output(component_id = 'submit-val', component_property = "n_clicks"),
              Output(component_id = 'markdown_table', component_property = 'children'),
              Output(component_id = 'question_index', component_property = 'data'),
              Output(component_id = 'target_val', component_property = 'data')],
                  [Input(component_id='grade_level',component_property="value"),
                   Input(component_id='standard',component_property="value"),
                  Input(component_id = 'submit', component_property= 'n_clicks')])

def pull_question(grade_level, standard, n_clicks, df=df):
    if n_clicks>0:
        temp_df= df.query("Standard == '{standard}' & Grade_level == {grade_level}".format(standard=standard, grade_level=grade_level))
        temp_df = temp_df.sample(n = 1, replace= True)
        y= str(temp_df['index'].to_list())
        y = json.loads(y)
        target_class = temp_df.iloc[0]['Class']
        x = target_class()
        try: 
            if hasattr(x, 'markdown_table'):
                question = x.print_question()
                choices= x.print_choices()
                answer = x.correct_letter
                topic = x.attr2
                choices = choices.to_markdown()
                return question, choices, answer, topic, 0, x.markdown_table, y, ''
            elif x.attr2=="Graph":
                question = x.print_question()
                choices= x.print_choices()
                answer = x.correct_letter
                topic = x.attr2
                choices = choices.to_markdown()
                target_val=x.target_val
                return question, choices, answer, topic, 0, '', y,target_val
            else:
                question = x.print_question()
                choices= x.print_choices()
                answer = x.correct_letter
                topic = x.attr2
                choices = choices.to_markdown()
                return question, choices, answer, topic, 0, '', y,''
        except:
            if x.attr2 == "Graph" or "Number Line" in x.attr2:
                question = x.print_question()
                choices = ''
                answer=x.correct_letter
                topic = x.attr2
                return question, choices, answer, topic, 0, '', y,''
            else:
                question = x.print_question()
                choices = ''
                answer = x.answer
                topic = x.attr2
                return question, choices, answer, topic, 0, '', y,''
    if n_clicks==0:
        return 'Please select a grade level and standard to get started.', "", "", "", 0, '', '', ''
    
@app.callback([Output(component_id= 'graph', component_property= 'figure'),
               Output(component_id = 'correct_answer2', component_property = 'data')],
              [Input(component_id = 'question_index', component_property='data'),
               Input(component_id = 'submit', component_property= 'n_clicks'),
               Input(component_id = 'target_val', component_property= 'data')])
              
def return_graph(question_index, n_clicks, target_val, df = df):
    if n_clicks == 0:
        return {}, {}
    if n_clicks > 0 :
        temp_df = df.iloc[question_index]
        target_class = temp_df.iloc[0]['Class']
        x = target_class()
        try:
            x.target_val= target_val
            i =templates.closest_value(x.temperatures, x.target_val)
            x.answer = x.days[i]
            x.correct_index = x.choices.index(x.answer)
            x.correct_letter = ['a', 'b', 'c', 'd'][x.correct_index]
            answer= x.correct_letter
            fig = x.print_graph()
            answer=answer
            return fig, answer
        except:
            return {},{}

@app.callback([Output(component_id= 'image', component_property= 'src'),
              Output(component_id = 'correct_answer3', component_property = 'data')],
              [Input(component_id = 'question_index', component_property='data'), 
              Input(component_id = 'submit', component_property= 'n_clicks')])
              
def return_picture(question_index, n_clicks, df = df):
    if n_clicks == 0:
        return '', ''
    if n_clicks > 0 :
        temp_df = df.iloc[question_index]
        target_class = temp_df.iloc[0]['Class']
        x = target_class()
        try:
            if "Identify Fraction" not in x.attr2:
                image = x.display_graph()
                answer=x.correct_letter
                return image, answer
            else:
                image = x.display_graph()
                answer= x.answer
                return image, answer
        except:
            return '',''
            
@app.callback(Output(component_id='graph', component_property='style'),
             [Input(component_id = 'question_index', component_property='data'), 
              Input(component_id = 'submit', component_property= 'n_clicks')]) 

def graph_style(question_index, n_clicks, df = df):
    if n_clicks == 0:
        style = {'display':'none'}
        return style
    if n_clicks > 0 :
        temp_df = df.iloc[question_index]
        target_class = temp_df.iloc[0]['Class']
        x = target_class()
        if hasattr(x, 'print_graph'):
            style = {'borderStyle':'solid','display':'inline-block'}
        else:
            style = {'display':'none'}
        return style

@app.callback(Output(component_id="feedback",component_property="children"),
              [Input(component_id = 'correct_answer', component_property = 'data'),
               Input(component_id = 'correct_answer2', component_property = 'data'),
               Input(component_id = 'correct_answer3', component_property = 'data'),
               Input(component_id = 'student_answer', component_property='value'),
              Input(component_id='topic', component_property = 'data'), 
              Input(component_id = 'submit-val', component_property='n_clicks')])

def answer_question(correct_answer, correct_answer2, correct_answer3, student_answer, topic, n_clicks):
    if n_clicks==0:
        return ""
    if n_clicks == 1:
        if "Fraction Addition/Subtraction" in topic:
            try:
                student_answer= student_answer.split("/")
                num = int(student_answer[0])
                denom = int(student_answer[1])
                student_answer = num/denom
                if student_answer == correct_answer:
                    return "You got the right answer. Nice work!"
                if student_answer != correct_answer:
                    return "You didn't get the right answer this time. Keep trying and don't give up!"
            except:
                return "Next time, please enter your answer as a fraction such as 1/8."
        if "Identify Fraction" in topic:
            try:
                student_answer= student_answer.split("/")
                num = int(student_answer[0])
                denom = int(student_answer[1])
                student_answer = num/denom
                if student_answer == correct_answer3:
                    return "You got the right answer. Nice work!"
                if student_answer != correct_answer3:
                    return "You didn't get the right answer this time. Keep trying and don't give up!"
            except:
                return "Next time, please enter your answer as a fraction such as 1/8."
        if topic == "Graph":
            if student_answer == correct_answer2:
                return "You got the right answer. Nice work!"
            if student_answer != correct_answer2:
                return "You didn't get the right answer this time. Keep trying and don't give up!"
            
        if "Number Line" in topic:
            if student_answer == correct_answer3:
                return "You got the right answer. Nice work!"
            if student_answer != correct_answer3:
                return "You didn't get the right answer this time. Keep trying and don't give up!"
        if "Fraction Ordering" in topic:
            try:
                fraction = student_answer.split(", ")
                numbers= []
                for item in fraction:
                    item = item.split("/")
                    numbers.append(item)
                numbers2= []
                for number in numbers:
                    num = int(number[0])
                    denom= int(number[1])
                    answer = num/denom
                    numbers2.append(answer)
                if numbers2 == correct_answer:
                    return "You got the right answer. Nice work!"
                if numbers2 != correct_answer:
                    return "You didn't get the right answer this time. Keep trying and don't give up!"
            except:
                return "Next time, please enter your answer as a list of fractions separated by commas and a space."
        else:
            if student_answer == correct_answer:
                return "You got the right answer. Nice work!"
            if student_answer != correct_answer:
                return "You didn't get the right answer this time. Keep trying and don't give up!"
    else:
        return "Please select a new question."
    
if __name__== "__main__":
    app.run_server(mode= 'external', host = "0.0.0.0", debug=True)