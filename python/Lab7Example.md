For this lab, I'm using a plugin called turtle. Turtle graphics draws lines on a screen with the right commands. it's a popular way for introducing programming to kids.

To run the Python script, you need to create a Virtual Env called turtle (or whatever you want to call it):

    virtualev ~/env/turtle

then you'll need to activate the Virtual Env:

    Windows: .\~/venv/turtle/Scripts/activate.ps1
    Linux: source ~/venv/turtle/Scripts/activate

Now, in Python, run the following command:

    import turtle

The above code will import turtle module

Next, run the following command to init turtle as well as show the drawings on the screen:

    myTurtle = turtle.Turtle()

turte got many functions to help you draw whatever you like on a screen. For example, here is a small list of fucntions you can use to draw:

1- forward(dictance (number)) -> Move the turtle forward by the spicified disctance. 
2- backword(distcance (number)) -> Move the turtle backwards by the spicified disctance
3- color(color name (string)) -> Set the color of the line of the trutle
4- circle(circle (number)) -> Draw a circle with a given radius

Let's test it! Run the following commands to draw two circles in different colors:

    myTurtle.forward(100)
    myTurtle.circle(50)
    myTurtle.color("red")

    myTurtle.backward(50)
    myTurtle.circle(50)
    myTurtle.color("blue")

Glad you liked it! finally, run the following commands to exit python and the Virtual Env

    exit()
    deactivate