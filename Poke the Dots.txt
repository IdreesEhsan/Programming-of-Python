# Poke The Dots Version 5
# This is a graphical game where two dots move around
# the screen, bouncing off the edges. The user tries 
# to prevent the dots from colliding by pressing and 
# releasing the mouse button to teleport the dots to 
# a random location. The score is the number of seconds 
# from the start of the game until the dots collide.

from uagame import Window
from random import randint
from math import sqrt
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

# User-defined functions

def main():
    game = Game()
    game.play()
    
# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self):
        # Initialize a Game.
        # - self is the Game to initialize
        
        self._window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90  # larger is faster game
        self._close_selected = False
        self._clock = Clock()
        self._small_dot = Dot('red', [50,75], 30, [1,2], self._window)
        self._big_dot = Dot('blue', [200,100], 40, [2,1], self._window)
        self._small_dot.randomize()
        self._big_dot.randomize()
        self._score = 0
        self._continue_game = True
        
    def _adjust_window(self):
        # Adjust the window for the game.
        # - self is the Game to adjust the window for
        
        self._window.set_font_name('ariel')
        self._window.set_font_size(64)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')        
    
    def play(self):
        # Play the game until the player presses the close icon
        # and then close the window.
        # - self is the Game to play

        while not self._close_selected:
            # play frame
            self.handle_events()
            self.draw()
            self.update()
        self._window.close()
           
    def handle_events(self):
        # Handle the current game events by changing the game
        # state appropriately.
        # - self is the Game whose events will be handled

        event_list = get_events()
        for event in event_list:
            self.handle_one_event(event)
            
    def handle_one_event(self, event):
        # Handle one event by changing the game state
        # appropriately.
        # - self is the Game whose event will be handled
        # - event is the Event object to handle
            
        if event.type == QUIT:
            self._close_selected = True
        elif self._continue_game and event.type == MOUSEBUTTONUP:
            self.handle_mouse_up(event)

    def handle_mouse_up(self, event):
        # Respond to the player releasing the mouse button by
        # taking appropriate actions.
        # - self is the Game where the mouse up occurred
        # - event is the Event object to handle

        self._small_dot.randomize()
        self._big_dot.randomize()
 
    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self._window.clear()
        self.draw_score()
        self._small_dot.draw()
        self._big_dot.draw()
        if not self._continue_game:  # perform game over actions
            self.draw_game_over()
        self._window.update()
                        
    def update(self):
        # Update all game objects with state changes
        # that are not due to user events. Determine if
        # the game should continue.
        # - self is the Game to update

        if self._continue_game:
            # update during game
            self._small_dot.move()
            self._big_dot.move()
            self._score = get_ticks() // 1000 
        self._clock.tick(self._frame_rate)
        
        # decide continue
        if self._small_dot.intersects(self._big_dot):
            self._continue_game = False

    def draw_game_over(self):
        # Draw GAME OVER in the lower left corner of the
        # surface, using the small dot's color for the font
        # and the big dot's color as the background.
        # - self is the Game to draw for
        
        string = 'GAME OVER'
        font_color = self._small_dot.get_color()
        bg_color = self._big_dot.get_color()
        original_font_color = self._window.get_font_color()
        original_bg_color = self._window.get_bg_color()
        self._window.set_font_color(font_color)
        self._window.set_bg_color(bg_color)
        height = self._window.get_height() - self._window.get_font_height()
        self._window.draw_string(string, 0, height)
        self._window.set_font_color(original_font_color)
        self._window.set_bg_color(original_bg_color)
        
    def draw_score(self):
        # Draw the time since the game began as a score.
        # - self is the Game to draw for.
        
        string = 'Score: ' + str(self._score)
        self._window.draw_string(string, 0, 0)

class Dot:
    # An object in this class represents a colored circle
    # that can move.

    def __init__(self, color, center, radius, velocity, window):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the str color of the dot
        # - center is a list containing the x and y int
        # coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - window is the game's Window

        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = velocity
        self._window = window

    def move(self):
        # Change the location and the velocity of the Dot so it
        # remains on the surface by bouncing from its edges.
        # - self is the Dot

        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            # update center at index
            self._center[index] = self._center[index] + self._velocity[index]
            # dot perimeter outside window?
            if (self._center[index] < self._radius) or (self._center[index] + self._radius > size[index]):
                # change direction
                self._velocity[index] = - self._velocity[index]

    def draw(self):
        # Draw the dot on the surface.
        # - self is the Dot

        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)

    def intersects(self, dot):
        # Return True if the two dots intersect and False if
        # they do not.
        # - self is a Dot
        # - dot is the other Dot

        distance = sqrt((self._center[0] - dot._center[0])**2 + (self._center[1] - dot._center[1])**2)
        return distance <= self._radius + dot._radius

    def get_color(self):
        # Return a str that represents the color of the dot.
        # - self is the Dot
        
        return self._color
    
    def randomize(self):
        # Change the dot so that its center is at a random
        # point on the surface. Ensure that no part of a dot
        # extends beyond the surface boundary.
        # - self is the Dot

        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)

main()