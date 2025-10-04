Snake Game using Python Turtle
--
Description
--
This project is a classic Snake game implemented using Python's built-in Turtle graphics library. The player controls a snake using arrow keys to eat randomly appearing food on the screen. Each time the snake eats food, it grows longer and the score increases. The game ends if the snake hits the screen borders or collides with its own body.

Features
--
Graphical interface created with Turtle

Randomly shaped and colored food appearing at various locations

Snake controlled using arrow keys (Up, Down, Left, Right)

Score and High score displayed at the top of the window

Increasing speed as the snake grows

Game restarts automatically after collision with walls or self

How to Run
--
Ensure Python is installed on your system.

Save the snake_game.py file with the provided code.

Run the script using the command:

bash
python snake_game.py
Control the snake using your keyboard arrow keys.

Code Structure
--
Modules Used:
turtle: For creating the game window, snake, food, and score display.

random: To place food randomly on the screen.

time: To control the speed of the game.

Key Components:
--
Screen setup: A 600x600 blue screen with title "Snake Game".

Snake head: White square turtle starting at the center with an initial direction 'stop'.

Food: Randomly shaped and colored turtle placed at random positions.

Scoreboard: Displays current score and highest score.

Movement functions: Control the snake’s direction and move it accordingly.

Main game loop: Continuously updates game state, checks for collisions, moves snake segments, increases score, and updates speed.

How Movement Works:
--
Movement is based on changing x and y coordinates by fixed steps (20 pixels) in four directions.

The snake’s segments follow the head by updating their positions in reverse order.

Collision Handling:
--
Game resets if the snake hits the border.

Game resets if the snake collides with itself.

When food is eaten, the snake grows by adding a segment and speed increases slightly.

Customization Ideas
--
Change colors or shapes of snake and food.

Adjust screen size or speed increments.

Add sound effects on eating or collisions.

Implement levels or obstacles.
