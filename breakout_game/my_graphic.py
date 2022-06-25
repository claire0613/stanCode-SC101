"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Please execute this file to start the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 80  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 6  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 8  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
# Global
score = 0


class BreakoutGraphics:
    global score

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # # Initialize our mouse listeners
        onmouseclicked(self.ball_velocity)
        onmousemoved(self.move_paddle)

        # Draw bricks
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        self.colors = ['#9C7E03','#D3AA00', '#F3D147','#FEE787', '#E6DEC0']
        color_ct = -1
        for i in range(brick_rows):
            if i % 2 == 0:
                color_ct += 1
            for j in range(brick_cols):
                brick = GRect(brick_width,brick_height)
                brick.filled = True
                brick.color = brick.fill_color = self.colors[color_ct % len(self.colors)]
                self.window.add(brick,j*(brick_width+brick_spacing),brick_offset + i*(brick_height+brick_spacing))

        self.score = score
        self.score_label = GLabel('SCORE: ' + str(score))
        self.score_label.font = '-10'
        self.window.add(self.score_label, x=10, y=self.window.height - 10)

        # set image
        self.img_heart1 = GImage('heart-icon.jpg')
        self.window.add(self.img_heart1, x=self.window.width - 100, y=self.window.height - 30)
        self.img_heart2 = GImage('heart-icon.jpg')
        self.window.add(self.img_heart2, x=self.window.width - 75, y=self.window.height - 30)
        self.img_heart3 = GImage('heart-icon.jpg')
        self.window.add(self.img_heart3, x=self.window.width - 50, y=self.window.height - 30)

        # calculate the  total number of the brick
        self.brick_num = self.brick_rows * self.brick_cols

        self.level = GLabel('Level_1')
        self.level.font = '-10'
        self.window.add(self.level, x=200, y=self.window.height - 10)

    def set_brick(self, color, column):
        x_1 = 0
        for i in range(0, self.brick_rows):
            brick = GRect(self.brick_width, self.brick_height)
            brick.filled = True
            brick.fill_color = color
            self.window.add(brick, x=x_1, y=column)
            x_1 += self.brick_width + self.brick_spacing

    def move_paddle(self, event):
        self.window.add(self.paddle, x=event.x - self.paddle.width//2, y=self.window.height - self.paddle_offset)
        if event.x <= self.paddle.width//2:
            self.window.add(self.paddle, x=0, y=self.window.height - self.paddle_offset)
        if event.x >= self.window.width - self.paddle.width:
            self.window.add(self.paddle, x=self.window.width - self.paddle.width,
                            y=self.window.height - self.paddle_offset)

    def ball_velocity(self, event):

        is_ball_moving = self.__dx != 0 and self.__dy != 0
        if not is_ball_moving:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx *= -1

    def ball_out_off_bottom(self):
        if self.ball.y >= self.window.height:
            self.window.add(self.ball, x=self.window.width / 2 - self.ball_radius,
                            y=self.window.height / 2 - self.ball_radius)
            self.__dx = 0
            self.__dy = 0
            return True







    def ball_reflect_wall(self):
        # ball reflect on the wall of the left and right side
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        # ball reflect on the wall of the top side
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def is_collision(self, x, y):
        # check if collision is happened or not.
        may_collision = self.window.get_object_at(x, y)
        if may_collision is not None and may_collision is not self.score_label and may_collision is not self.img_heart1 \
                and may_collision is not self.img_heart2 and may_collision is not self.img_heart3 \
                and may_collision is not self.level:
            if self.paddle.x == may_collision.x and self.paddle.y == may_collision.y:
                self.__dy = -abs(self.__dy)
                return True
            if self.ball.y + self.ball_radius * 2 >= may_collision.y:
                self.__dy = -abs(self.__dy)
                self.__dy *= -1
                self.window.remove(may_collision)
                self.get_score()
                self.brick_num -= 1
                return True
        return False

    def get_score(self):
        self.score += 1
        self.score_label.text = 'SCORE: ' + str(self.score)

    def finish(self):
        finish = GLabel('Finish!')
        finish.font = '-40'
        self.window.add(finish, x=self.window.width / 2 - 100, y=self.window.height / 2)

    def game_over(self):
        finish = GLabel('GameOver!')
        finish.font = '-40'
        self.window.add(finish, x=self.window.width / 2 - 150, y=self.window.height / 2)

    def increasing(self):
        # Increasing the velocity of level by decreased the brick
        if self.brick_num==57:
            self.__dx *= 1.0025
            self.__dy *= 1.0025
            self.level.text = 'INCREASING!Level_2'

        elif self.brick_num==53:
            self.__dx *= 1.005
            self.__dy *= 1.005
            self.level.text = 'INCREASING!Level_3'

    @property
    def dv_x(self):
        return self.__dx

    @property
    def dv_y(self):
        return self.__dy
