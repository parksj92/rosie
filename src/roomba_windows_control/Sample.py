################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, sys, inspect, _thread, time, math, json
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/LeapSDK/lib/x64' if sys.maxsize > 2**32 else '../lib/LeapSDK/lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

lib_dir1 = os.path.abspath(os.path.join(src_dir, '../lib/LeapSDK/lib'))
lib_dir2 = os.path.abspath(os.path.join(src_dir, '../lib/pycreate'))
sys.path.insert(0, lib_dir1)
sys.path.insert(0, lib_dir2)
import Leap, create
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    robot = None

    def on_init(self, controller, serPort):
        print("Initialized")
        robot = create.Create(serPort)

    def on_connect(self, controller):
        print("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        frame_pointables = frame.pointables
        handType = ""
        data = {}
        for points in frame_pointables:
            if (points.is_finger and points.is_valid):
                finger = Leap.Finger(points)
                if finger.type() == 1:
                    hand = points.hand
                    if(hand.is_valid):
                        if(hand.is_right):
                            handType = "Right"
                        elif(hand.is_left):
                            handType = "Left"
                        #print handType
                    angle = points.direction.yaw*180.0/math.pi
                    sign = "Right" if angle >= 0 else "Left"
                    angle = math.fabs(angle)
                    angleEst = round(angle, -1)
                    if(angleEst == 0):
                        sign = "Straight"
                    #data["angle"]       = angleEst
                    data["direction"]   = sign
                    json_data = json.dumps(data)
                    print(json_data)
            else:
                data["direction"] = None

        DEFAULT_ANGULAR_VELOCITY = 5
        DEFAULT_LINEAR_VELOCITY = 15

        # the robot keeps moving left or right
        if sign == "Right" or sign == "Left":
            robot.go(0, DEFAULT_ANGULAR_VELOCITY)
        elif sign == "Straight":
            robot.go(DEFAULT_LINEAR_VELOCITY, 0)
        elif data["direction"] == None:
            robot.stop()


                 
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    if (len(sys.argv) != 2):
        print("Need more command line arguments")
        sys.exit(2)

    serPort = int(sys.argv[1])

    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller(serPort)

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
