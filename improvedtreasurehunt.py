# import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import pibrella
from math import sqrt
from time import sleep

# connect python to minecraft
mc = minecraft.Minecraft.create()

# start program here
# hide the treasure
treas_x = 100
treas_y = 5
treas_z = 20

# main loop
while True:
    # get player position
    x, y, z = mc.player.getTilePos()

    # calculate distance to treasure
    dist_x = x - treas_x
    dist_y = y - treas_y
    dist_z = z - treas_z
    dist = sqrt(dist_x * dist_x + dist_y * dist_y + dist_z * dist_z)

    print(dist)  # debug output
    if int(dist) > 20:
        pibrella.light.red.on()
        sleep(.5)
        pibrella.light.red.off()
        sleep(.5)
    elif int(dist) < 20 and int(dist) > 2:
        pibrella.light.yellow.on()
        sleep(.3)
        pibrella.light.yellow.off()
        sleep(.3)
    elif int(dist) < 2 and int(dist) > 0:
        pibrella.light.green.on()
        sleep(.1)
        pibrella.light.green.off()
        sleep(.1)
    else:
        mc.postToChat("Success, you have found the treasure")
        break  # quit loop