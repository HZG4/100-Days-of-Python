# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# average_temp = data.temp.mean()
# max_temp = data.temp.max()
#
# # Give me the data (full row) with maximum temp value.
# row = data[data.temp == data.temp.max()]
# print(row)
#
# # Access data using a variable
# monday = data[data.day == "Monday"]
# num = monday.temp[0]
# farhenheit = (num * 9/5) + 32
# print(farhenheit)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students" : ["amy" , "mia", "angela"],
#     "scores" : [8, 10, 9]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
import turtle
import pandas
from turtle import Turtle, Screen

def game_over(self):
    self.goto(-120, 0)
    self.color("Red")
    self.write(f"GAME OVER", font=("Arial", 30, "bold"))

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width= 725, height=491)

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()
state_xcor = data.x.to_list()
state_ycor = data.y.to_list()
answers = []
points = 0

game_is_on = True
while game_is_on:
    answer = screen.textinput(title="Name a state", prompt="Enter a state name: ").title()
    if answer in state_names:
        if answer not in answers:
            row = data[data.state == answer]

            # Extract coordinates as int. Hint: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
            xcor = int(row.iloc[0].x)
            ycor = int(row.iloc[0].y)
            name = Turtle()
            name.penup()
            name.hideturtle()
            name.goto(xcor, ycor)
            name.write(f"{answer}")

            answers.append(answer)
        elif len(answers) == len(state_names):
            game_over()
            game_is_on = False
    else:
        continue


turtle.mainloop()



