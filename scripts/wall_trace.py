#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, copy, math
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from pimouse_ros.msg import LightSensorValues

class WallTrace():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sensor_values = LightSensorValues()
        rospy.Subscriber('/lightsensors', LightSensorValues, self.callback)

    def callback(self, messages):
        self.sensor_values = messages

    def run(self):
        rate = rospy.Rate(20)
        data = Twist()

        accel = 0.01
        min_speed = 0.2
        max_speed = 0.4
        while not rospy.is_shutdown():
            s = self.sensor_values
            data.linear.x += accel

            if s.sum_forward >= 100:          data.linear.x = 0.0 # 前方に物があるときは停止
            elif data.linear.x <= min_speed: data.linear.x = min_speed
            elif data.linear.x >= max_speed: data.linear.x = max_speed

            if data.linear.x < min_speed:    data.angular.z = 0.0 # 停止しているときは回転しない
            elif s.left_side <= 5:           data.angular.z = 0.0 # 左に物がないときは直進
            else:
                target = 50
                error = (target - s.left_side) / 50.0
                data.angular.z = error * 3 * math.pi / 180.0

            self.cmd_vel.publish(data)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('wall_trace')
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    WallTrace().run()
