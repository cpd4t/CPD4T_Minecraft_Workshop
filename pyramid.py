# import modules
import mcpi.minecraft as minecraft
import time

# connect python to minecraft
mc = minecraft.Minecraft.create()

# declare CONSTANTS and variables
GOLD = 41
AIR = 0
STONE = 1
layers = 10

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.setBlocks(-60, -1, -60, 60, -1, 60, STONE)
mc.player.setPos(layers + 5, 0, 0)

# set width and height
width = layers
height = 0

# create pyramid
for i in range(layers):
    print(width, height)  # debug output
    mc.setBlocks(-width, height, -width, width, height, width, GOLD)
    width = width -1
    height = height + 1
    time.sleep(0.2)
