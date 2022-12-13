import turtle
TK_SILENCE_DEPRECATION=1
min_branch_lenght = 5

wn = turtle.Screen()
wn.setup(width = 1200, height = 600)


def build_tree(t, branch_length, shorten_by, angle):
    if branch_length > min_branch_lenght:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)

        t.right(angle*2)
        build_tree(t, new_length, shorten_by, angle)

        t.left(angle)
        t.backwards(branch_length)
        print("bye")
def setUp():
    
    tree = turtle.Turtle()

    tree.setheading(90)
    tree.color('green')
    tree.speed(100)
    tree.goto(0,0)
    tree.pendown()
    tree.forward(100)
    print("hey")

    build_tree(tree, 50, 5, 30)

setUp()
while True:
    wn.update()