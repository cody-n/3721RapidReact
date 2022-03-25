import wpilib
from wpilib import SmartDashboard
from commandbased import CommandBasedRobot
from commands2 import CommandScheduler
from commands2 import RunCommand
import commands2
from robotMap import RobotMap
from helper import Creator
from commands.teleop import TeleOp
from subsytems.drive import Drive
from oi import OI


class compRobot(CommandBasedRobot):
    def robotInit(self):
        super().__init__()

        self.Creator = Creator
        self.botMap = RobotMap(self)
        self.oi = OI(self)
        self.drive = Drive(self)
        self.s = CommandScheduler
        self.teleop = TeleOp(self)

    def robotPeriodic(self):
        self.s.getInstance().run()

    def log(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.teleop.execute()

    def teleopPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(compRobot)

