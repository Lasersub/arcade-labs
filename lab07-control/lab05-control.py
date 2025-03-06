
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10
DEAD_ZONE = 0.02


# DRAWINGS

def grass():
    """Grass"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)


def leaves():
    """Tree's leaves"""
    # HOJA1
    arcade.draw_triangle_filled(250, 200, 550, 200, 400, 350, arcade.color.LIME_GREEN)
    # HOJA2
    arcade.draw_triangle_filled(270, 290, 530, 290, 400, 430, arcade.color.LIME_GREEN)
    # HOJA3
    arcade.draw_triangle_filled(290, 380, 510, 380, 400, 510, arcade.color.LIME_GREEN)


def christmas_lightbulbs():
    """Christmas lightbulbs"""
    # BOLA1
    arcade.draw_circle_filled(350, 240, 15, arcade.color.RED)
    # BOLA2
    arcade.draw_circle_filled(430, 300, 15, arcade.color.PURPLE)
    # BOLA3
    arcade.draw_circle_filled(365, 345, 15, arcade.color.DARK_BLUE)
    # BOLA4
    arcade.draw_circle_filled(455, 410, 15, arcade.color.RED)
    # BOLA5
    arcade.draw_circle_filled(375, 430, 15, arcade.color.PURPLE)
    # BOLA6
    arcade.draw_circle_filled(460, 240, 15, arcade.color.DARK_BLUE)


def star():
    """Star"""
    arcade.draw_polygon_filled([[400, 480],
                                [420, 455],
                                [425, 490],
                                [445, 500],
                                [410, 510],
                                [400, 540],
                                [390, 510],
                                [355, 500],
                                [375, 490],
                                [380, 455]],
                               arcade.color.GOLD)


def tree():
    # Log
    arcade.draw_lrtb_rectangle_filled(380, 420, 200, 60, arcade.color.DARK_BROWN)
    # Leaves
    leaves()
    # Christmas lightbulbs
    christmas_lightbulbs()
    # Star
    star()





class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """Draws a cloud"""
        arcade.draw_circle_filled(-60 + self.position_x, -35 + self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(10 + self.position_x, -65 + self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(0 + self.position_x, 0 + self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(40 + self.position_x, -5 + self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(80 + self.position_x, -45 + self.position_y, self.radius, self.color)

    def on_update(self):
        # Move the cloud
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.BLUE)

        self.set_mouse_visible(False)

        self.cloud = Cloud(50, 50, 0, 0, 50, arcade.color.LIGHT_GRAY)


        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None


    def on_draw(self):
        self.clear()
        grass()
        tree()
        self.cloud.draw()

    def on_update(self, delta_time):

        # GAME CONTROLLER
        # Update the position according to the game controller
        if self.joystick:
            print(self.joystick.x, self.joystick.y)

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.cloud.change_x = 0
            else:
                self.cloud.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.cloud.change_y = 0
            else:
                self.cloud.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.cloud.on_update()

    # MOUSE
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.cloud.position_x = x
        self.cloud.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)



    # KEYBOARD
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            print("Left key hit")
        elif key == arcade.key.RIGHT:
            print("Right key hit")

    def on_key_released(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.cloud.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.cloud.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0



def main():
    window = MyGame()
    arcade.run()


main()