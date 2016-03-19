# Build a 16 x 16 grid of all the available block types up to block ID 255

# import modules
import mcpi.minecraft as minecraft
from time import sleep

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create CONSTANTS and variables for blocks and counts
AIR = 0
STONE = 1
DIRT = 3
block_id = 0
z = 0

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.setBlocks(-60, -1, -60, 60, -1, 60, STONE)
mc.setBlocks(-60, -2, -60, 60, -2, 60, DIRT)
mc.player.setPos(-3, 0, 0)

print("Starting...")
mc.postToChat("Starting...")

while block_id < 256:
    for x in range(0, 16):
        print (x, -1, z, block_id)
        mc.setBlock(x, -1, z, block_id)
        block_id = block_id + 1
        sleep(0.1)
    z = z + 1

mc.postToChat("Finished")
print("Finished")
