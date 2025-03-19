
# ROS2

<https://www.youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy>

List of commands in the .bashrc file:
source /opt/ros/humble/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /mnt/c/ros2_ws/install/setup.bash
cd /mnt/c
export LIBGL_ALWAYS_SOFTWARE=true
chmod 0700 /run/user/1000/

The ros workspace is simply a folder (ros_ws). Inside it there must be another folder called src.
Run "colcon build", then move to the install folder and run the setup.bash script (the same one that is run when opening each terminal).

To compile new files. With the --symlink-install option it sees changes to files already present at the last build:
colcon  build --symlink-install

It is run for safety to set up ros2 sources (in theory already executed when opening each bash):
source ~/.bashrc

ex. ros2 run turtlesim turtlesim_node (turtlesim: package, turtlesim_node: run command)
ex. ros2 run my_robot_controller test_node (my_robot_controller: package, test_node: run command in setup.py)

Add the packages you use as depend tags in the package.xml file

Add the run command in the setup.py file when finished:
ex. "test_node = my_robot_controller.my_first_node:main"
test_node: run command, my_robot_controller: package, my_first_node: file name. Inside the my_first_node file, the node is given the name "first_node" which is another reference used within ros during execution

# GAZEBO

ign gazebo shapes.sdf per il render di test
