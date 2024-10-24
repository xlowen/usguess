import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
screen.title("Adivinhar estados dos EUA")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")

dict_data = data.to_dict()

my_turtle = turtle.Turtle()
correct_guesses = []

print(data["state"])
print(data.state.str.lower())

for state in data.state.str.lower():
    print(state)

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Corretos: {len(correct_guesses)}/50", prompt="Digite um estado.").lower()
    if answer_state == "sair":
        break
    for state in data.state.str.lower():
        if state == answer_state:
            x = int(data[data["state"].str.lower() == f'{answer_state}'].x.iloc[0])
            y = int(data[data["state"].str.lower() == f'{answer_state}'].y.iloc[0])
            my_turtle.penup()
            my_turtle.goto(int(x), int(y))
            my_turtle.ht()
            my_turtle.write(f'{answer_state}', False, "center", font=('Arial', 8, 'normal'))
            if answer_state not in correct_guesses:
                correct_guesses.append(answer_state)


all_states = data["state"].str.lower().to_list()
missing_states = []

for state in all_states:
    if state in correct_guesses:
        continue
    else:
        print(f"adicionando: {state} na lista.")
        missing_states.append(state)


print("missing states: ", missing_states)
missing_states = pandas.DataFrame(missing_states)

missing_states.to_csv("estados_faltando.csv")
# states_to_learn.csv