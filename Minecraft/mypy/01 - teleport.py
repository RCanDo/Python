# ForSpigot, Minecraft Python Server 1.11.2

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(10)

x=10 ; y=110 ; z=10
mc.player.setTilePos(x, y, z)    ## uses only integers


## x=10. ; y=70.8 ; z=10.
## mc.player.setPos(x, y, z)        ## uses float numbers

time.sleep(5)

x=0 ; y=100 ; z=0
mc.player.setTilePos(x, y, z)    ## uses only integers


time.sleep(6)

x=-50; y=100 ; z=-50
mc.player.setTilePos(x, y, z)    ## uses only integers
