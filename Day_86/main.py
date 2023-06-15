import time
from turtle import Screen
from Day_86.bricks import Bricks
from paddle import Paddle
from Day_86.ball import Ball
from scoreboard import Scoreboard

# set up screen
my_screen = Screen()
my_screen.title("Break Out Game")
my_screen.bgcolor("#FFF4F4")
my_screen.setup(width=600, height=700)
my_screen.tracer(0)

# initialised respective classes
bricks = Bricks()
bricks.create_bricks()
paddle = Paddle()
ball = Ball()
my_score_card = Scoreboard()

# set the paddle to move right and left using right and left
# arrow in the keyboard.
my_screen.listen()
my_screen.onkeypress(paddle.move_left, "Left")
my_screen.onkeypress(paddle.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Detect wall collision
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # detect paddle collision
    if ball.distance(paddle) < 40 and ball.ycor() < -220:
        ball.bounce_y()

    if ball.ycor() > 330:
        ball.beyond_reset_position()

    # ball goes behand the paddle and lose a life
    if ball.ycor() < -260:
        ball.reset_position()
        my_score_card.update_lives()
        if my_score_card.lives == 0:
            my_score_card.game_over()
            game_is_on = False

    # check for ball collision with the brick. if yes, hide the brick
    # and update point
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            my_score_card.get_point()
            if len(bricks.all_bricks) == 0:
                bricks.win()

my_screen.exitonclick()
