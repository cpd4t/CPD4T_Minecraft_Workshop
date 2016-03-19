# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create CONSTANTS for block and light colours
AIR = 0
STONE = 1

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.setBlocks(-60, -1, -60, 60, -1, 60, STONE)
mc.player.setPos(5, 0, 0)
