from vpython import *
#Web VPython 3.2
from vpython import *

# Display an object undergoing basic projectile motion

# Define the parameters for the coordinate axes
a_length = 12         # Each axis will range from - to + of this value
a_color = color.white # Set the color for the coordinate axes here
a_radius = 0.1        # Set the radius of the axes here
 
# Display a set of coordinate axes using narrow cylinders
xaxis=cylinder(color=a_color, pos=vector(-a_length,0,0), axis=vector(2*a_length,0,0), radius=a_radius)
yaxis=cylinder(color=a_color, pos=vector(0,-a_length,0), axis=vector(0,2*a_length,0), radius=a_radius)
zaxis=cylinder(color=a_color, pos=vector(0,0,-a_length), axis=vector(0,0,2*a_length), radius=a_radius)

# Define Constants
m = 0.1  # Mass of object (kg)
g = 9.8  # Gravity Constant (N/kg)

# Define Initial Conditions
r0 = vector(0,3,0)  # Initial Position (m)

v0 = 10              # Magnitude of Initial Velocity (m/s)
theta0 = 30                # Launch Angle in Degrees


# Create the object at the initial position
ball=sphere(pos=r0, radius=1000, color=color.red, make_trail=True)
# Compute an Inital Velocity and Momentum
#  remember to convert angle from degrees to radians
ball.v = vector(v0*cos(radians(theta0)), v0*cos(radians(90-theta0)),0) 
ball.m = 0.1   # Mass of the ball in kg
ball.p = ball.m * ball.v

pi = 3.141592653589793
b = 6 * pi * (1.81 * 10**(-5)) * ball.radius

# Create a Position vs Time Graph
g1 = graph(title='Position vs Time', xtitle='Time (s)', ytitle='Position (m)', fast=True, width=800)
f1 = gcurve(color=color.blue, width=2, markers=True, marker_color=color.blue, label='Horizontal, x')
f2 = gcurve(color=color.red , width=2, markers=True, marker_color=color.red,  label='Vertical, y')

# Create a Velocity vs Time Graph
g2 = graph(title='Velocity vs Time', xtitle='Time (s)', ytitle='Velocity (m/s)', fast=False, width=800)
f3 = gcurve(color=color.blue, width=2, markers=True, marker_color=color.blue, label='Horizontal, Vx')
f4 = gcurve(color=color.red , width=2, markers=True, marker_color=color.red,  label='Vertical, Vy')

# Initialize the Time Variables
t=0      # Actual Time (s)
dt=0.2  # Time Step (s)

# Loop until the ball hits the ground
while ball.pos.y>=0:
    rate(100)
    
    # Compute the force on the ball
    Fdrag = vector((ball.p.x/ball.m) * b * -1, (ball.p.y/ball.m) * b * -1, 0)
    
    Fnet = vector(Fdrag.x, Fdrag.y + -m*g, 0)
    
    # Update the momentum of the ball
    ball.p = ball.p + Fnet*dt
    
    # Update the position of the ball
    ball.pos = ball.pos + ball.p/ball.m*dt

    
    # Increment time for the plot
    t=t+dt
        
    # Update the position vs time plots
    f1.plot(t, ball.pos.x)
    f2.plot(t, ball.pos.y)
    
    # Update the velocity vs time plots
    f3.plot(t, ball.p.x/m)
    f4.plot(t, ball.p.y/m)

# Range
print("Range is " + round(ball.pos.x, 2))

# Final Velocity 
vF = vector(ball.p.x/ball.m, ball.p.y/ball.m , 0)
print("X-Component of final velocity is " + round(vF.x, 2))
print("Y-Component of final velocity is " + round(vF.y, 2))
print("Magnitude is " + round((vF.x**2 + vF.y**2)**.5, 2))