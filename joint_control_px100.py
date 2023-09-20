# Copyright 2022 Trossen Robotics

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():
    joint1 = (np.pi/180)*90  # the limit is 180
    joint2 = (np.pi/180)*-60  # the limit is 107
    joint3 = (np.pi/180)*12  # the limit is 92
    joint4 = (np.pi/180)*83  # the limit is 123


    # TODO: Define the joint angles in radians considering the joint limits
    joint_positions = [joint1, joint2, joint3, joint4]

    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    bot.arm.go_to_home_pose()
    bot.arm.set_joint_positions(joint_positions)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

    bot.shutdown()


if __name__ == '__main__':
    main()