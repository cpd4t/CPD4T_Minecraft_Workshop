# import modules
import mcpi.minecraft as minecraft
from time import sleep
import pibrella

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create variables for block and light colours
air = 0
stone = 1
wool = 35
black = 15
red = 14
amber = 4
green = 5

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, air)
mc.setBlocks(-60, -1, -60, 60, -1, 60, stone)
mc.player.setPos(5, 0, 0)

# create initial light stack
for i in range(1, 7):
    mc.setBlock(10, 0 +i, 0, wool, 8)

mc.setBlock(9, 6, 0, wool, black)
mc.setBlock(9, 5, 0, wool, black)
mc.setBlock(9, 4, 0, wool, black)

# wait three seconds before starting sequence
sleep(3)

# traffic light sequence
while True:
    # turn on red
    mc.setBlock(9, 6, 0, wool, red)
    pibrella.light.red.on()
    # wait three seconds
    sleep(3)

    # turn on amber
    mc.setBlock(9, 5, 0, wool, amber)
    pibrella.light.yellow.on()
    # wait one second
    sleep(1)

    # turn off red & amber, turn on green
    mc.setBlock(9, 6, 0, wool, black)
    pibrella.light.red.off()
    mc.setBlock(9, 5, 0, wool, black)
    pibrella.light.yellow.off()
    mc.setBlock(9, 4, 0, wool, green)
    pibrella.light.green.on()
    # wait three seconds
    sleep(3)

    # turn off green
    mc.setBlock(9, 4, 0, wool, black)
    pibrella.light.green.off()
    # turn on amber
    mc.setBlock(9, 5, 0, wool, amber)
    pibrella.light.yellow.on()
    # wait one second
    sleep(1)

    # turn off amber
    mc.setBlock(9, 5, 0, wool, black)
    pibrella.light.yellow.off()
