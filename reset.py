# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create variables for block and light colours
air = 0
stone = 1

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, air)
mc.setBlocks(-60, -1, -60, 60, -1, 60, stone)
mc.player.setPos(5, 0, 0)
