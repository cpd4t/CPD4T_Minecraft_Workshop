# import modules
import mcpi.minecraft as minecraft
import random

# connect python to minecraft
mc = minecraft.Minecraft.create()

# define suitable block types
block_list = [1, 4, 20, 22, 24, 41, 42, 43, 48, 49, 57]

# start program here
# get players position
x, y, z = mc.player.getTilePos()

# set build point 10 blocks away from player
x = x + 10
z = z + 10

# set starting value for story
story = 0

# a 10 story building
while story < 10:
    # choose random block type
    block_id = random.choice(block_list)
    mc.setBlocks(x - 5, y + story, z - 5, x + 5, y + story, z + 5, block_id)
    story = story + 1
