import turtle 
screen =turtle.Screen()
screen.title("Indian. State Game")
image = "Day_25 Working with CSV Data and the Pandas Library/India-state.gif"
screen.addshape(image)
turtle.shape(image)


import pandas
data = pandas.read_csv("Day_25 Working with CSV Data and the Pandas Library/50_states.csv")
all_state = data.state.to_list()
guessed_state = []
while len(guessed_state) <31:
    answer_state = turtle.textinput(title=f"{len(guessed_state)}/30 Guess states",prompt="What is the another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_state]
       # missing_states = []
        # for states in all_state:
        #     if states not in guessed_state:
        #         missing_states.append(states)
        # print(missing_states)
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("Day_25 Working with CSV Data and the Pandas Library/States_to_Learn.csv")
        break
    if answer_state in all_state:
            guessed_state.append(answer_state)
            t= turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data =data[data.state == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            # t.write(answer_state)
            t.write(state_data.state.item())
            # t.write(state_data.state)
# screen.exitonclick()

















# def get_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_coor)
# screen.mainloop()
# screen.exitonclick()