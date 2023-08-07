#U.S. States Game
import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_state_img.gif"
screen.addshape("image")
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt= "What is another State's name?")
print(answer_state)