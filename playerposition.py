import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
position = str(x) + ", " + str(y) + ", " + str(z)
mc.postToChat(position)
