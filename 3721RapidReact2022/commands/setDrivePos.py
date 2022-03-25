import wpilib
from commands2 import Command


class SetDrivePos(Command):
    def __init__(self, robot, speed, dist, turnDeg):
        Command().__init__()
        self.robot = robot

        self.speed = speed
        self.distance = dist
        self.speed = speed
        self.angle = turnDeg
        self.i = 0
        self.s = 0

    def initialize(self):
        self.robot.drive.resetHeading()
        self.robot.drive.resetEnc()
        self.robot.drive.DrivePID.setPt(0)
        self.robot.drive.DrivePID.limitVal(self.speed)

    def execute(self):
        turn = self.Drive.DrivePID.outVal(self.Drive.getHeading())
        forward = self.Drive.DrivePID.outVal(self.Drive.getEnc())

    def isFinished(self):
        return False

    def end(self):
        self.i = 0
        self.robot.Drive.stop()
        self.robot.Drive.resetEnc()
