# import modules
import mcpi.minecraft as minecraft
import pibrella
import random

# connect python to minecraft
mc = minecraft.Minecraft.create()

# start program here
while True:
    # check if button pressed
    if pibrella.button.read() == 1:
        # generate random co-ordinates
        x = random.randint(-100, 100)
        y = random.randint(0, 100) # no going underground
        z = random.randint(-100, 100)
        
        # move player to new co-ordinates
        mc.postToChat("Teleport!")
        mc.player.setPos(x, y, z)