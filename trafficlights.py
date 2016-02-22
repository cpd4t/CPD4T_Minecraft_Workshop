# import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create variables for light colours
black = 15
red = 14
amber = 4
green = 5

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, block.AIR.id)
mc.player.setPos(5, 0, 0)

# create initial light stack 
for i in range(1, 7):
    mc.setBlock(10, 0 +i, 0, block.WOOL.id, 8)
    
mc.setBlock(9, 6, 0, block.WOOL.id, black)
mc.setBlock(9, 5, 0, block.WOOL.id, black)
mc.setBlock(9, 4, 0, block.WOOL.id, black)
    