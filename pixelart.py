# import modules
import mcpi.minecraft as minecraft

# connect python to minecraft
mc = minecraft.Minecraft.create()

# start program here
# define block types
AIR = 0
WOOL = 35

# define pixel art data
pixels = [
    [ 15, 13, 1, 14 ],
    [ 1, 3, 1, 14 ],
    [ 1, 13, 11, 14 ],
    [ 1, 13, 1, 15 ],
    ]

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.player.setPos(5, 0, 0)

# create pixel art
x=0
y=0
z=0
for row in pixels:
    y = y + 1
    z = 0
    for pixel in row:
        print(x, y, pixel)
        mc.setBlock(x, y, z, WOOL, pixel)
        z = z + 1
