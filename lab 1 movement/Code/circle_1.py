import sim
import math
import flib

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

speed = 0.1

l = 2*math.pi*r
circle_time = l/speed
angle = 360/circle_time
k = 0
print("is conneted!!!")
pos = flib.get_pos(clientID, QuadricopterT)

flib.navigate_map(pos[0], pos[1], h, speed, clientID, QuadricopterT)

while True:
    flib.navigate_local(speed, 0, 0, speed, clientID, QuadricopterT)
    err = sim.simxSetObjectOrientation(clientID, QuadricopterT, -1, (0, 0, rad(k)), sim.simx_opmode_blocking)
    k += angle
    if k >= 360:
        break

sim.simxFinish(clientID)
