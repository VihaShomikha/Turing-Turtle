# TuringTurtle: Geometric Shapes with Loops

This Python code creates a visually appealing drawing using the Turtle graphics library. It combines loops and shape manipulation to produce a geometric pattern.

**Features:**

* Creates a red turtle object with a larger size.
* Creates a complex geometric pattern with alternating forward movements and turns.

**Instructions:**

1. **Prerequisites:** Ensure you have Python 3 and the `turtle` library installed.
   - To install `turtle`, run `pip install turtle` in your terminal.
2. **Running the Code:**
   - Save this code as a Python file (e.g., `turing_turtle.py`).
   - Open a terminal, navigate to the directory where you saved the file, and run:
      python turtle.py

**Explanation:**

The code utilizes the `turtle` library to create a drawing on the screen. Here's a breakdown of the key parts:

* **Import:** The `import turtle` line imports the `turtle` library, providing functions for drawing shapes and controlling the turtle.
* **Turtle Creation:** `my_turtle = turtle.Turtle()` creates a turtle object named `my_turtle` that we'll use for drawing.
* **Turtle Customization:**
   - `my_turtle.forward(80)` moves the turtle forward 80 units.
   - `my_turtle.shapesize(3)` increases the turtle's size to make it more visible.
   - `my_turtle.shape('turtle')` changes the turtle's shape to a turtle icon.
   - `my_turtle.color('red')` sets the turtle's color to red.
* **Drawing with Loop:**
   - The first `for` loop iterates 4 times (0 to 3).
   - Inside the loop:
      - `my_turtle.forward(100)` moves the turtle forward 100 units, drawing a line.
      - `my_turtle.right(90)` turns the turtle 90 degrees to the right, ready for the next side of the square.
* **Complex Geometric Pattern:**
   - The second `for` loop iterates 60 times (0 to 59).
   - Inside the loop:
      - `if i % 2 == 0` (even numbers):
         - `my_turtle.forward(100)` moves the turtle forward 100 units for shorter lines.
         - `my_turtle.right(60)` turns the turtle 60 degrees to the right.
      - `else` (odd numbers):
         - `my_turtle.forward(150)` moves the turtle forward 150 units for longer lines.
         - `my_turtle.right(80)` turns the turtle 80 degrees to the right.

This combination of loops and turns creates the intricate geometric pattern.

**I hope you find this code and explanation helpful!**
