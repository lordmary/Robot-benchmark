#Desafio do quadrado

from controller import Robot

robot = Robot()

leftWheel = robot.getMotor('left wheel')
rightWheel = robot.getMotor('right wheel')

for i in range(0, 2):
   
    leftWheel.setPosition(1000)
    rightWheel.setPosition(1000)
    
    robot.step(3910)
   
    leftWheel.setPosition(1000)
    rightWheel.setPosition(-1000)
   
    robot.step(480)
for i in range(0, 2):
    
    leftWheel.setPosition(1000)
    rightWheel.setPosition(1000)
   
    robot.step(3905)
   
    leftWheel.setPosition(1000)
    rightWheel.setPosition(-1000)
   
    robot.step(455)

leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
