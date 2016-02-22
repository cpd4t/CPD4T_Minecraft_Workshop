import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y + 30, z)
