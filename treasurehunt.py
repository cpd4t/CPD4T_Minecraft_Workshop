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
