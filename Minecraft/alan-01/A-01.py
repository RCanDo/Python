# andżomandżoukulele

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(10)
mc.player.setTilePos(50000)

time.sleep(2)
X=-10000
y=100
z=-10000
mc.player.setBlock(-10000, 200, -10000)

x = 10000
y = 70
z = 10000
typBloku = 124
mc.setBlock(x, y, z, typBloku)
