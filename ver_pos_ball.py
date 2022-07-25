intial_velocity = 5
acceleration_of_gravity = 9.81
Time = 0.6

VerticalPositionOfBall = intial_velocity*Time - 0.5*acceleration_of_gravity*Time**2

print(VerticalPositionOfBall)


v0 = 5 
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2

print(y)

yc = 0.2
import math

t1 = (v0 - math.sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + math.sqrt(v0**2 - 2*g*yc))/g
print("At t = ",t1, "and ",t2, "the height is ",yc)
