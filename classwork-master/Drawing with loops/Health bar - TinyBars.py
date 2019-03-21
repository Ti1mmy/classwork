"""
Use Arcade to draw a health bar.
1. Create global variables under `HEIGHT` and `WIDTH` called `player_health`. For now, we will
assume a valid health value is between 0 and 100. Give the variable a value of 100.
2. In the `draw()` function, create a rectangle (somewhere in the middle of the screen)
that will serve as the healthbar background. Color this bar BLACK. Make it 200px wide and 50 px tall.
3. Draw another Rectangle in the exact same way as the background, except, color the bar GREEN.
4. Make this green bar's width change according to the globao `player_health` variable. If the player's
helath is at 50, that means the green bar will be 50% the size of the background bar. If it is at 75,
that means the green bar will be 75% the width of the background bar. Use some math to determine
the pixel width.
5. Use arcade's `draw_text()` function to display a number out of 100 on the healthbar. Place this anywhere on the healthbar.
The text should display something like `89/100`.
6. Create a global variable under `player_health` called `player_max_health`. In RPG games a player's health pool can grow.
Set this number to 350. You will need to change the way you calculate the green health bar's width to accomodate the fact that
the player's health pool can change. The text you draw should also display the health out of the max health, rather than always 100.
"""

import arcade
import math

WIDTH = 640
HEIGHT = 480
player_health = 345
player_max_health = 350
size_multiplier_healthbar = player_max_health / 200
#box numbers
full_bars = int(player_health / (player_max_health / 4))
remaining_bar_health = (player_health % (player_max_health / 4)) / 100
print(remaining_bar_health)
def update(delta_time):
    pass


def on_draw():
    y = 240
    x = 320
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_outline(x, y, 155, 50, arcade.color.BLACK)
    for i in range(0, full_bars + 1):
        x = 247.5 + i * 30
        arcade.draw_xywh_rectangle_filled(x, y - 20, 25, 40, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(x + 30, y - 20, 25 * remaining_bar_health, 40, arcade.color.GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Contemporary art: Diminished life in bar.")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()