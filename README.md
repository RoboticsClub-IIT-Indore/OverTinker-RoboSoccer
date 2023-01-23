# RoboSoccer
Installation for RoboSoccer '23 - Overtinker Software PS

```
cd ~/catkin_ws
git clone https://github.com/AkshitRaizada/RoboSoccer.git
```
```
sudo cp ~/catkin_ws/models/* ~/.gazebo/models/
sudo cp ~/catkin_ws/robocup_final.world /usr/share/gazebo-11/worlds/
```
```
cd src
git clone https://github.com/chvmp/champ.git
cd ~/catkin_ws
rosdep install -y -r -q --from-paths src --ignore-src --rosdistro noetic
catkin_make
```

After this you can simply run the world_launcher.launch file to get the desired world. Check the rostopics(there should ideally be 6 /robot_name/cmd_vel) and write scripts in ~/catkin_ws/src/gz_launcher/scripts/Team_1 for the first set of robots and in the same directory /scripts/Team_2 for the second team.
