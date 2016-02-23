# import modules
import mcpi.minecraft as minecraft
import time

# connect python to minecraft
mc = minecraft.Minecraft.create()

# declare variables
gold = 41
air = 0
layers = 10

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, air)
mc.player.setPos(layers + 5, 0, 0)

# set width and height
width = layers
height = 0

# create pyramid
for i in range(layers):
    print(width, height)  # debug output
    mc.setBlocks(-width, height, -width, width, height, width, gold)
    width = width -1
    height = height + 1