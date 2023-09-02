# Instructions
# Initial game starts, and you have 3 seconds to choose a choice between block, sneak, attack, and defend
# For the red player the controls are wasd(w=attack, s= sneak hit, a = defend, and d = block)
# For the blue player the controls are the arrow keys(up arrow = attack, down arrow= sneak hit, and left arrow = defend,
# and right arrow = block)
# For the controls: defend beats attack, attack beats sneak hit, sneak hit beats defend, and block negates all damage from
# the user. But each user only gets one block. When a user uses block after they have already used it or fails to pick an action
# altogether they lose the round unless the other user also used an illegal block or failed to pick an action.
# The user can continually change choices before the round ends. After the round ends, the user that picked the losing choice
# will lose 50 health. Once the round ends, another round will start in 4 seconds with 3 seconds for users to pick a choice.
# Once a user loses all 200 of their health, the game ends and the winner is displayed on the screen
# The user has the option to start the game again by pressing space bar.

# Game Description ***THIS IS NOT THE INSTRUCTIONS NEARLY A QUICK DESCRIPTION
# The players control two knights in a duel.
# The players have 4 seconds each turn to pick between attack, defend, sneaky hit or defend.
# Attack beats sneaky hit, sneaky hit beats defend, and defend beats attack.
# If the players pick the same choice they cancel out, the players only get 1 defend and it protects them that turn
# Each knight can take four hits before they lose
# When a knight loses all of their health the winner pops up on the screen

# User Input
# One user controls the blue Knight using "wasd", while the other user controls the red Knight using the arrow keys.

# Game Over
# When one of the players gets hit 4 times the winning Knight pops up on the screen

# Graphics
# The Knights will be graphic images
# The background will also *HAVE A* graphic image
# ADDED** The knights image changes based on what action you choose with a total of 5 unique sprites per a knight
# depending on the action


# Additional Features

# Timer: There is a timer set in each turn that tells the players how long they have to pick a choice. If they
# do not pick in time they do not move

# Two Players Simultaneously: Two players control the user input for the Knights

# Restart from game over: When a knight runs out of health and a winner is declared you can press space bar
# to restart ********REPLACED ANIMATION WITH THIS SINCE FIRST SUBMISSION

# Health Bar: The Knights have a health bar that goes down when they are hit


import uvage
camera = uvage.Camera(800,600)

# Creating initial variables and assigning them their values
game_on = True
round_on = True
timer = 0
time = 3
ticker = 0
health1 = 4
health2 = 4
knight1_block = 1
knight2_block = 1
knight1_choice1 = " "
knight2_choice2 = " "

# Creating background for the game
walls = [
    uvage.from_color(25, 300, "grey", 50, 600),
    uvage.from_color(775, 300, "grey", 50, 600),
]
health_bar_background = [
    uvage.from_color(180, 300, "grey", 200, 25),
    uvage.from_color(600, 300, "grey", 200, 25),
]
floor = uvage.from_color(400, 575, "white", 800, 50)
chandelier = uvage.from_image(400, 50, "https://www.realm667.com/images/content/repository/propstop/Chandelier%20Pack.png")
# Creating knights
knight1 = uvage.from_image(250, 472, "https://i.postimg.cc/KzH6yh5M/knight-red-6.png")
knight2 = uvage.from_image(650, 515, "https://i.postimg.cc/bNmpmW71/Knight-Blue.png")
knight2.flip()



def tick():
    # All variables globalized
    global game_on
    global round_on
    global timer
    global time
    global health1
    global health2
    global knight1_block
    global knight2_block
    global knight1_choice
    global knight2_choice
    global result
    global count

    # Game over condition with the ability to restart
    if (health1 == 0) or (health2 == 0):
        game_on = False
        if health1 == 0:
            game_result = "The Blue Knight Wins!"
        if health2 == 0:
            game_result = "The Red Knight Wins!"
        timer += 1
        if timer >= 140:
            knight1_choice = " "
            knight2_choice = " "
            # Restarts game and assigns variables their initial values
            if uvage.is_pressing("space"):
                game_on = True
                round_on = True
                timer = 0
                time = 3
                health1 = 4
                health2 = 4
                knight1_block = 1
                knight2_block = 1

    # Draws the knights in case of no change
    knight1 = uvage.from_image(125, 502, "https://i.postimg.cc/BvkxhZxV/KnightR.png")
    knight2 = uvage.from_image(650, 501, "https://i.postimg.cc/bNmpmW71/Knight-Blue.png")
    knight2.flip()

    if game_on == True:

        if round_on == True:
            # count is used later to manage variable change
            count = 1
            # Where the two users make their choice of action
            if uvage.is_pressing("right arrow"):
                knight2_choice = "Block!"
            elif uvage.is_pressing("left arrow"):
                knight2_choice = "Defend!"
            elif uvage.is_pressing("down arrow"):
                knight2_choice = "Sneak Hit!"
            elif uvage.is_pressing("up arrow"):
                knight2_choice = "Attack!"
            else:
                knight2_choice = " "

            if uvage.is_pressing("d"):
                knight1_choice = "Block!"
            elif uvage.is_pressing("a"):
                knight1_choice = "Defend!"
            elif uvage.is_pressing("s"):
                knight1_choice = "Sneak Hit!"
            elif uvage.is_pressing("w"):
                knight1_choice = "Attack!"
            else:
                knight1_choice = " "

            # Manages the time in each active round, including changing the time on screen
            if (timer % 30) == 0:
                time -= 1
            if (timer == 90) and (round_on == True):
                round_on = False
                timer = 0



        timer += 1
        if round_on == False:
            # These if, elif statements determine what happens after user input round is over. They are ordered in a way to
            # make sure that the outcome is as we intended
            if ((knight1_choice == "Block!") and (knight1_block == 1) and (knight2_choice == "Block!") and (knight2_block == 1)):
                result = "Both Knights Used Their Block, No One is Hit"
                # This appears multiple times and is just to make sure the block variables only change on the last tick so
                # that the if, elif statement does not change until the next user input is made
                if timer == 120:
                    knight1_block = 0
                    knight2_block = 0
            elif (((knight1_choice == " ") or (knight1_choice == "Block!") and (knight1_block == 0)) and (knight2_choice == "Block!") and (knight2_block == 1)):
                result = "The Red Knight Failed to Pick a Usable Action, the Blue Knight Makes Contact!"
                if timer == 120:
                    knight2_block = 0
                # The count variable works to only subtract from a user's health once a round not every time a tick occurs
                if count == 1:
                    health1 -= 1
                    count = 0
            elif (((knight2_choice == " ") or (knight2_choice == "Block!") and (knight2_block == 0)) and (knight1_choice == "Block!") and (knight1_block == 1)):
                result = "The Blue Knight Failed to Pick a Usable Action, the Red Knight Makes Contact!"
                if timer == 120:
                    knight1_block = 0
                if count == 1:
                    health2 -= 1
                    count = 0
            elif (knight1_choice == " ") and (knight2_choice == " "):
                result = "The Knights Failed to Pick Usable Actions, No One is Hit!"
            elif ((knight2_choice == "Block!") and (knight2_block == 0)) and ((knight1_choice == "Block!") and (knight1_block == 0)):
                result = "The Knights Failed to Pick Usable Actions, No One is Hit!"
            elif ((knight1_choice == " ") and (knight2_choice == "Block!") and (knight2_block == 0)) or ((knight2_choice == " ") and (knight1_choice == "Block!") and (knight1_block == 0)):
                result = "Both Knights Failed to Pick Usable Actions, No One is Hit!"
            elif ((knight2_choice == "Block!") and (knight2_block == 0)):
                result = "The Blue Knight Failed to Pick a Usable Action, the Red Knight Makes Contact!"
                if count == 1:
                    health2 -= 1
                    count = 0
            elif ((knight1_choice == "Block!") and (knight1_block == 0)):
                result = "The Red Knight Failed to Pick a Usable Action, the Blue Knight Makes Contact!"
                if count == 1:
                    health1 -= 1
                    count = 0
            elif (knight1_choice == knight2_choice):
                result = "The Knights Picked the Same Action, No One is Hit!"
            elif knight1_choice == " ":
                result = "The Red Knight Failed to Pick a Usable Action, the Blue Knight Makes Contact!"
                if count == 1:
                    health1 -= 1
                    count = 0
            elif knight2_choice == " ":
                result = "The Blue Knight Failed to Pick a Usable Action, the Red Knight Makes Contact!"
                if count == 1:
                    health2 -= 1
                    count = 0
            elif (knight1_choice == "Block!") and (knight1_block == 1):
                result = "The Red Knight Used his One Block, No One is Hit!"
                if timer == 120:
                    knight1_block = 0
            elif (knight2_choice == "Block!") and (knight2_block == 1):
                result = "The Red Knight Used his One Block, No One is Hit!"
                if timer == 120:
                    knight2_block = 0
            elif (knight1_choice == "Attack!" and knight2_choice == "Defend!") or (knight1_choice == "Defend!" and knight2_choice == "Sneak Hit!") or (knight1_choice == "Sneak Hit!" and knight2_choice == "Attack!"):
                result = "The Blue Knight Makes Contact!"
                if count == 1:
                    health1 -= 1
                    count = 0
            elif (knight1_choice == "Defend!" and knight2_choice == "Attack!") or (knight1_choice == "Sneak Hit!" and knight2_choice == "Defend!") or (knight1_choice == "Attack!" and knight2_choice == "Sneak Hit!"):
                result = "The Red Knight Makes Contact!"
                if count == 1:
                    health2 -= 1
                    count = 0
            # After 120 ticks this if statement makes the next user choice round start
            if timer == 120:
                round_on = True
                time = 3
                timer = 0
        # These if, elif statements change the knights sprite depending on the action current being used by either user
        if knight1_choice == "Attack!":
            knight1 = uvage.from_image(125, 522, "https://i.postimg.cc/Dz9XrjhV/Knight-R-Attack.png")
        elif knight1_choice == "Defend!":
            knight1 = uvage.from_image(125, 502, "https://i.postimg.cc/QdV9RGxG/Knight-R-Defend.png")
        elif knight1_choice == "Sneak Hit!":
            knight1 = uvage.from_image(125, 512, "https://i.postimg.cc/tTdYh9DP/Knight-Red-crouch.png")
        elif knight1_choice == "Block!":
            knight1 = uvage.from_image(175, 542, "https://i.postimg.cc/jS9wTgLW/Knight-R-Block.png")
        elif knight1_choice == " ":
            knight1 = uvage.from_image(125, 502, "https://i.postimg.cc/BvkxhZxV/KnightR.png")
        if knight2_choice == "Attack!":
            knight2 = uvage.from_image(650, 521, "https://i.postimg.cc/8PYPfFD9/Knight-Blue-Attack.png")
            knight2.flip()
        elif knight2_choice == "Defend!":
            knight2 = uvage.from_image(650, 501, "https://i.postimg.cc/3RhwrP7w/Knight-B-Defend.png")
            knight2.flip()
        elif knight2_choice == "Sneak Hit!":
            knight2 = uvage.from_image(650, 511, "https://i.postimg.cc/y6PDxYDC/Knight-Blue-crouch.png")
            knight2.flip()
        elif knight2_choice == "Block!":
            knight2 = uvage.from_image(600, 541, "https://i.postimg.cc/zfKBrqsM/Knight-B-Block.png")
            knight2.flip()
        elif knight2_choice == " ":
            knight2 = uvage.from_image(650, 501, "https://i.postimg.cc/bNmpmW71/Knight-Blue.png")
            knight2.flip()



    # This reassigns the health bar so that it changes depending on the health of the knights
    health_bar = [
        uvage.from_color(180, 300, "red", health1 * 50, 25),
        uvage.from_color(600, 300, "blue", health2 * 50, 25),
    ]

    camera.clear("black")

    # Draws the background and the knights
    for wall in walls:
        camera.draw(wall)
    camera.draw(floor)
    camera.draw(chandelier)
    camera.draw(knight1)
    camera.draw(knight2)
    for background in health_bar_background:
        camera.draw(background)
    for bar in health_bar:
        camera.draw(bar)

    # Draws the total health on the health bar
    camera.draw("Health: " + str(health1*50) + "/200", 25, "white", 180, 300)
    camera.draw("Health: " + str(health2*50) + "/200", 25, "white", 600, 300)

    # These statements print the knights final choice on the screen after a knight has lost all their health and
    # the game is over
    if (game_on == False) and timer <= 120:
        if knight1_choice == " ":
            camera.draw("Red Knight Chose to Do Nothing", 25, "red", 190, 350)
        else:
            camera.draw("Red Knight Chose to " + knight1_choice, 25, "red", 180, 350)
        if knight2_choice == " ":
            camera.draw("Blue Knight Chose to Do Nothing", 25, "blue", 590, 350)
        else:
            camera.draw("Blue Knight Chose to " + knight2_choice, 25, "blue", 600, 350)
        camera.draw(result, 25, "white", 400, 200)

    # These statements print the users current action during the user choice round
    if round_on == True and game_on == True and timer >= 1:
        camera.draw(knight1_choice, 30, "red", 180, 350)
        camera.draw(knight2_choice, 30, "blue", 600, 350)
        camera.draw("Time Left in Round: " + str(time), 40, "white", 400, 200)

    # These statements print the users final choice after each user choice round is over
    if round_on == False and game_on == True:
        if knight1_choice == " ":
            camera.draw("Red Knight Chose to Do Nothing", 25, "red", 195, 350)
        else:
            camera.draw("Red Knight Chose to " + knight1_choice, 25, "red", 195, 350)
        if knight2_choice == " ":
            camera.draw("Blue Knight Chose to Do Nothing", 25, "blue", 590, 350)
        else:
            camera.draw("Blue Knight Chose to " + knight2_choice, 25, "blue", 600, 350)
        camera.draw(result, 25, "white", 400, 200)

    # This is the game over screen and also prints the option for the user to play again using spacebar
    if (game_on == False) and timer >= 140:
        camera.draw(game_result, 40, "white", 400, 200)
        if timer >= 90:
            camera.draw("Press Space to Restart", 30, "white", 400, 425)







    # displays everything
    camera.display()


# This means there are 30 ticks per a second and is the basis of many of our condition statements involving tick count and
# the functionality of the time printed on the screen
ticks_per_second = 30


uvage.timer_loop(ticks_per_second, tick)
