cmake_minimum_required(VERSION 2.8.3)
project(tf_static_aggregator)

find_package(catkin REQUIRED COMPONENTS
  rospy
  tf2_msgs
  geometry_msgs
)

catkin_package()

catkin_python_setup()

#############
## Install ##
#############
 install(PROGRAMS
   scripts/TfStaticAggregator.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
