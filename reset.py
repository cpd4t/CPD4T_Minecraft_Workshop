# import modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# connect python to minecraft
mc = minecraft.Minecraft.create()

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, block.AIR.id)
mc.player.setPos(5, 0, 0)
