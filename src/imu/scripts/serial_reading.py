import serial


ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    imu_string = ser.readline()
    print imu_string

