#!/usr/bin/env python

# ROS
import rospy
from tf_static_aggregator.aggregator import TfAggregator


if __name__ == '__main__':
    rospy.init_node('Tf_static_aggregator')

    aggregator = TfAggregator()

    rospy.spin()
