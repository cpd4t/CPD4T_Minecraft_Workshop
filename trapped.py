# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create variables for block and light colours
air = 0
stone = 1
wool = 35

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, air)
mc.setBlocks(-60, -1, -60, 60, -1, 60, stone)
mc.player.setPos(5, 0, 0)

# build the trap
mc.setBlocks(20, 0, 20, 22, 3, 22, wool, 3)
mc.setBlocks(21, 0, 20, 21, 3, 21, air)
mc.setBlock(21, -1, 21, wool, 14)

while True:
    x, y, z = mc.player.getTilePos()

    # check if player is trapped and block them in with orange wool
    # print "Trapped!" to the chat
    if x == 21 and y == 0 and z == 21:
        mc.setBlocks(21, 0, 20, 21, 3, 20, wool, 1)
        mc.setBlock(21, 3, 21, wool, 1)
        mc.postToChat("Trapped!")

        #quit program
        break
