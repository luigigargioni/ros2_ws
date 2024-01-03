
# ROS2

<https://www.youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy>

Lista di comandi nel file .bashrc:
source /opt/ros/humble/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /mnt/c/ros2_ws/install/setup.bash
cd /mnt/c
export LIBGL_ALWAYS_SOFTWARE=true
chmod 0700 /run/user/1000/

Il workspace di ros è semplicemente una cartella (ros_ws). Al suo interno deve esserci un'altra cartella chiamata src.
Lanciare "colcon build", muoversi poi nella cartella install e lanciare lo script setup.bash (lo stesso che poi viene lanciato all'apertura di ogni terminale).

Per compilare i nuovi file. Con l'opzione --symlink-install vede le modifiche sui file già presenti all'ultima build
colcon  build --symlink-install

Viene eseguito per sicurezza per impostare i source di ros2 (in teoria già eseguito all'apertura di ogni bash)
source ~/.bashrc

ex. ros2 run turtlesim turtlesim_node (turtlesim: package, turtlesim_node: run command)
ex. ros2 run my_robot_controller test_node (my_robot_controller: package, test_node: run command in setup.py)

Aggiungi i pacchetti che usi come tag depend nel file package.xml

Aggiungi il run command nel file setup.py quando finito
ex. "test_node = my_robot_controller.my_first_node:main"
test_node: run command, my_robot_controller: package, my_first_node: file name. All'interno del file my_first_node, al nodo viene dato il nome "first_node" che è un altro riferimento
usato all'interno di ros durante l'esecuzione

# GAZEBO

ign gazebo shapes.sdf per il render di test