# import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

# connect python to minecraft
mc = minecraft.Minecraft.create()

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, block.AIR.id)
mc.player.setPos(5, 0, 0)

# build the trap
mc.setBlocks(20, 0, 20, 22, 3, 22, block.WOOL.id, 3)
mc.setBlocks(21, 0, 20, 21, 3, 21, block.AIR.id)

while True:
    x, y, z = mc.player.getTilePos()
    
    if x == 21 and y == 0 and z == 21:
        mc.setBlock(21, 0, 20, block.WOOL,id, 1)
        mc.setBlock(21, 1, 20, block.WOOL,id, 1)
        mc.setBlock(21, 2, 20, block.WOOL,id, 1)
        mc.setBlock(21, 3, 20, block.WOOL,id, 1)
        mc.postToChat("Trapped!")
        sleep(1)
        
 