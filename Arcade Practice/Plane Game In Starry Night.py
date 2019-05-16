import arcade
import random

WIDTH = 1280
HEIGHT = 720

star_x_positions = []
star_y_positions = []
y_plane = HEIGHT / 2
keydown = False
keyup = False
for i in range(10):
    x = random.randrange(0, WIDTH * 2)
    y = random.randrange(HEIGHT)
    star_x_positions.append(x)
    star_y_positions.append(y)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Plane starry knight")
    arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global y_plane
    for x_range in range(len(star_x_positions)):
        star_x_positions[x_range] -= 4
        if star_x_positions[x_range] <= 0:
            star_y_positions[x_range] = random.randrange(0, HEIGHT)
            star_x_positions[x_range] = random.randrange(WIDTH, WIDTH * 2)
    if y_plane >= 50:
        if keydown:
            y_plane -= 8
    if y_plane <= HEIGHT - 50:
        if keyup:
            y_plane += 8
    for detect in range(len(star_x_positions)):
        if (star_x_positions[detect]in range(200, 300)) and (star_y_positions[detect] in range(int(y_plane - 50, y_plane + 50))):
            print('boom')

def on_draw():
    arcade.start_render()
    for x_star, y_star in zip(star_x_positions, star_y_positions):
        arcade.draw_circle_filled(x_star, y_star, 2, arcade.color.WHITE)
    plane = arcade.load_texture('plane.png', 0, 0, 420, 420)
    arcade.draw_texture_rectangle(250, y_plane, 100, 100, plane)


def on_key_press(key, modifiers):
    global keydown
    global keyup
    if key == arcade.key.DOWN:
        keydown = True
    if key == arcade.key.UP:
        keyup = True


def on_key_release(key, modifiers):
    global keyup
    global keydown
    if key == arcade.key.DOWN:
        keydown = False
    if key == arcade.key.UP:
        keyup = False

def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()