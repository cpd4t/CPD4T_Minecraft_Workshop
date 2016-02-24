# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# start program here
# get players position
x, y, z = mc.player.getTilePos()

# set build point 10 blocks away from player
x = x + 10
z = z + 10

# set starting values for story and block type
story = 0
block_id = 10

# a 10 story building
while story < 10:
    mc.setBlocks(x - 5, y + story, z - 5, x + 5, y + story, z + 5, block_id)
    story = story + 1
    block_id = block_id + 1
