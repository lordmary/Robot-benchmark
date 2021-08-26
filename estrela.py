# desafio da estrela 
# tentei usar a mesma logica do triangulo e quadrado

from controller import Robot

robot = Robot()

leftWheel = robot.getMotor('left wheel')
rightWheel = robot.getMotor('right wheel')

for i in range(0, 12):
    
    leftWheel.setPosition(1000)
    rightWheel.setPosition(1000)
    
    robot.step(2000)
    
    leftWheel.setPosition(-500)
    rightWheel.setPosition(500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
    leftWheel.setPosition(500)
    rightWheel.setPosition(-500)
    
    robot.step(480)
    
# parar o robo

leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
