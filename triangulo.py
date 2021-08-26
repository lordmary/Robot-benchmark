# desafio do triangulo, estou fazendo um triangulo equilatero e acutangulo

from controller import Robot


robot = Robot()


leftWheel = robot.getMotor('left wheel')
rightWheel = robot.getMotor('right wheel')


for i in range(0, 3):
    
    leftWheel.setPosition(3000)
    rightWheel.setPosition(3000)
    # vai andar o mesmo tanto pra cada lado
    robot.step(3900)
    
    leftWheel.setPosition(3000)
    # virar pra direita
    rightWheel.setPosition(-3000)
    # vai virar 60 graus pra ser acutangulo
    robot.step(640)

# parar o robo
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
