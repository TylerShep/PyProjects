import turtle
import pattern

def main():
    pattern.setUp()
    playAgain = True

# Main Menu
    while playAgain:
        pattern.setUp()
        print("Choose a Pattern Mode:")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Choose a mode to play: 1, 2, or 3? "))

# Draw Rectangle Pattern
        if mode == 1:
            xPos, yPos = eval(input("Enter a center position (x, y):"))
            width = eval(input("Width?:"))
            height = eval(input("Height?:"))
            offset = eval(input("Offset?:"))
            count = eval(input("Count?:"))
            rotation = eval(input("Rotation?:"))

            pattern.drawRectanglePattern(xPos, yPos, height, width, offset, count, rotation)

# Draw Circle Pattern
        elif mode == 2:
            xPos, yPos = eval(input("Enter a center position (x, y):"))
            radius = eval(input("Radius?:"))
            offset = eval(input("Offset?:"))
            count = eval(input("Count?:"))

            pattern.drawCirclePattern(xPos, yPos, radius, offset, count)

# Draw Super Pattern
        elif mode == 3:
            number = eval(input("Number?:"))

            pattern.drawSuperPattern(number)

        else:
            print("Invalid input.")

# Exit Menu
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear all drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

# Keep Playing
        playAgain = response == 1 or response == 2

# Rest Drawings
        if response == 2:
            pattern.reset()
            playAgain = response
# Done Drawing
        elif response == 3:
            print("Thanks for playing!")
            pattern.done()

main()
