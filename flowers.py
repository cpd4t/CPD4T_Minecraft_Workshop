import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, block.FLOWER_CYAN.id)
