#!/usr/bin/env python

# ROS
import rospy
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage

class TfAggregator(object):
    def __init__(self):
        self.pub_static_tf_aggregated = rospy.Publisher('/tf_static_aggregated',
                                         TFMessage , queue_size=20)
        self.sub_statiic_tf = rospy.Subscriber("/tf_static", TFMessage, self.cb_tf)
        self.transform_aggregated = []
	self.timer = rospy.Timer(rospy.Duration(1), self.tf_pub_cb)

    def cb_tf(self, data):
        for transform in data.transforms:
            # check if the transform as already been defined
            id = next((id for id, existing in
                       enumerate(self.transform_aggregated)
                       if existing.header.frame_id == transform.header.frame_id
                       and existing.child_frame_id == transform.child_frame_id)
                       , -1)

            if id < 0: self.transform_aggregated.append(TransformStamped())
            to_fill = self.transform_aggregated[id]
            to_fill.header.stamp.secs = transform.header.stamp.secs
            to_fill.header.frame_id = transform.header.frame_id
            to_fill.child_frame_id = transform.child_frame_id
            to_fill.transform = transform.transform

    def tf_pub_cb(self, event):
	self.pub_static_tf_aggregated.publish(self.transform_aggregated)
