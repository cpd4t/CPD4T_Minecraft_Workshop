import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x + 1, y, z, 41)
