import sim
import math
import flib
import time
from geometry_tools import *

rad = math.radians
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID != -1:
    print('Connected to remote API server')
err, QuadricopterT = sim.simxGetObjectHandle(
    clientID, 'Quadricopter_target', sim.simx_opmode_blocking)
if err == -1:
    print("No Quadricopter")
err, Quadricopter = sim.simxGetObjectHandle(
    clientID, 'Quadricopter', sim.simx_opmode_blocking)
if err == -1:
    print("No Quadricopter")

sim.simxStartSimulation(clientID, sim.simx_opmode_blocking)

r = 1.0
h = 1.0

speed = 0.8

l = 2*math.pi*r
circle_time = l/speed
angle = 360/circle_time
k = 0
print("is conneted!!!")

pos = flib.get_pos(clientID, QuadricopterT)
rot = flib.get_rot(clientID, QuadricopterT)
t = 0
old_timer = time.time()
while True:
    dt = time.time() - old_timer
    t += dt
    old_timer = time.time()
    if dt < 0.0001:
        continue

    pos = flib.get_pos(clientID, QuadricopterT)
    offset = rotate_vect(t*speed, 1)
    print("offset", offset)

    err = sim.simxSetObjectPosition(clientID, QuadricopterT, -1,
                                     (pos[0]+offset[0], pos[1]+offset[1], 1.),
                                     sim.simx_opmode_blocking)
    # err = sim.simxSetObjectOrientation(clientID, QuadricopterT, -1, (0, 0, rad(90)), sim.simx_opmode_blocking)

    time.sleep(0.01)

sim.simxFinish(clientID)
