#!/usr/bin/env python3

import os

from launch import LaunchDescription
from launch_ros.actions import Node

# this is the function launch  system will look for
def generate_launch_description():

    return LaunchDescription([
        Node(package='qos_test', executable="qos_pub", output={'both': 'log'}),
        Node(package='qos_test', executable="qos_sub", output='screen')
    ])
