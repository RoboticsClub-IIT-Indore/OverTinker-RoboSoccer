#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty
from gazebo_msgs.msg import ContactsState
from std_msgs.msg import String
import time
time.sleep(2)
reset_flag = False
goals = [0,0]                  #Team1-Team2
pub = rospy.Publisher('/goals', String, queue_size=10)

def callback(data):
    print(data)
    global goals
    global reset_flag
    j=0
    
    if not (data.states)==[]:
        ans = (data.states)[j].info[13:15]
        if (ans[1]==')'):
            noi = int(ans[0])
        
        else:
            noi = 10 * int(ans[0]) + int(ans[1])
      
        i=0
    
        for i in range(noi):
            if ((data.states[i]).collision2_name)[17]=='G' and not reset_flag:
                check = (data.states[i]).collision2_name[30]
                if (check == 'n'):
                    print(check,"_net")
                    goals[0] = goals[0] + 1
                    reset_flag = True
                    print("GOAL1","_net")
                    break
        
                else:
                    goals[1] = goals[1] + 1
                    reset_flag = True
                    print("GOAL2","_net")
                    break
            
            i = i + 1

def referee():
    global pub
    global goals
    global reset_flag
    rospy.init_node('reset_world')
    rate = rospy.Rate(100)
    
    rospy.wait_for_service('/gazebo/reset_world')
    reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
    print("TEST1")
    rospy.Subscriber("/goal_checker", ContactsState, callback)
    print("TEST2")
    print("TEST3")
    
    while not rospy.is_shutdown():
    
        if reset_flag:
            reset_world()
            reset_flag = False

        pub.publish(str(goals[0])+"-"+str(goals[1]))
        
    rospy.spin()
    
if __name__=='__main__':
    try:
        referee()
    except:
        pass
