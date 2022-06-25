"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Please execute this file to start the game.
"""

from campy.gui.events.timer import pause
from my_graphic import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics(paddle_width=150)
    lives = NUM_LIVES
    brick_num = graphics.brick_rows * graphics.brick_cols
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if lives == 0:
            # when life runs out
            graphics.game_over()
            graphics.window.remove(graphics.img_heart1)
            break
        else:
            # when life runs out>0
            graphics.ball.move(graphics.dv_x, graphics.dv_y)
            graphics.ball_reflect_wall()

            # ball out off the bottom of window and reduce the life
            if graphics.ball_out_off_bottom():
                lives -= 1
                if lives == 2:
                    graphics.window.remove(graphics.img_heart3)
                elif lives == 1:
                    graphics.window.remove(graphics.img_heart2)

            if graphics.brick_num > 0:
                # check the velocity level
                graphics.increasing()
                # check collision is happened at the ball(x,y)
                if graphics.is_collision(graphics.ball.x, graphics.ball.y):
                    pass
                # check collision is happened at the ball(x+2r,y)
                elif graphics.is_collision(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y):
                    pass

                # check collision is happened at the ball(x+2r,y+2r)
                elif graphics.is_collision(graphics.ball.x + graphics.ball_radius * 2,
                                           graphics.ball.y + graphics.ball_radius * 2):
                    pass
                # check collision is happened at the ball(x,y+2r)
                elif graphics.is_collision(graphics.ball.x, graphics.ball.y + graphics.ball_radius * 2):
                    pass

            else:
                graphics.finish()
                break


if __name__ == '__main__':
    main()
