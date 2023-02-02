## Smart Home
Smart Home is a project that has the goal to develop an intelligent system to manage a smart room in a house. First of all, an infrared distance sensor is placed on the ceiling of the room and is used to determine whether the user is inside the room or not.
Based on the occupancy of the room and on the light measurements obtained by a photoresistor, the smart home system turns on/off a smart light bulb.
Furthermore, the room has a window on one side, equipped with a servo motor to open/close it based on the delta between the temperatures measured by two temperature sensors, one indoor and one outdoor (i.e., inside and outside the room).
Finally, the smart home system also monitors the gas level in the air inside the room through an air quality sensor and then triggers an active buzzer when too many gas particles are detected.

## Sensors and Actuators 
To recap, the following sensors and actuators are present:
- An infrared distance sensor located on the ceiling to the room.
- A smart light bulb.
- A photoresistor sensor to measure the light level inside the room.
- A servo motor to open/close the window.
- Two temperature sensors, one indoor and one outdoor, used in
combination with the servo motor to open/close the window.
- An air quality sensor, used to measure the gas level inside the room.
- An active buzzer that is triggered when a certain level of gas particles in
the air is detected.

The communication between the main board and the other components happens with GPIO pins configured in BCM mode. 

## User Stories 
1. User detection: to verify whether the room has someone inside of it by using the infrared distance sensor.
2. Manage smart light bulb based on occupancy: to control the behavior of the smart light bulb.
3. Manage smart light bulb based on light level: to handle the additional constraint of the photoresistor measurements with the function to measure the amount of lux in the room.
4. Open/close window based on temperature: to control the behavior of the window based on the temperature values. 
The servo motor can be controlled by the Duty Cycle DC that is implemented according to this formula DC = (angle/18) + 2.
5. Gas leak detection: to control the behavior of the air quality sensor and the buzzer.
