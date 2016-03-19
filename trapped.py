# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create variables for block and light colours
AIR = 0
STONE = 1
WOOL = 35

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.setBlocks(-60, -1, -60, 60, -1, 60, STONE)
mc.player.setPos(5, 0, 0)

# build the trap
mc.setBlocks(20, 0, 20, 22, 3, 22, WOOL, 3)
mc.setBlocks(21, 0, 20, 21, 3, 21, AIR)
mc.setBlock(21, -1, 21, WOOL, 14)

while True:
    x, y, z = mc.player.getTilePos()

    # check if player is trapped and block them in with orange wool
    # print "Trapped!" to the chat
    if x == 21 and y == 0 and z == 21:
        mc.setBlocks(21, 0, 20, 21, 3, 20, WOOL, 1)
        mc.setBlock(21, 3, 21, WOOL, 1)
        mc.postToChat("Trapped!")

        #quit program
        break
mc.postToChat("Program has finished")
print("Program has finished")
