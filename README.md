# Mini-Projects
Projects' Description 

(1) Gambling Time
This is a simple game that allows two players - player A and B to roll a dice randomly. If Player A rolls a 1, the turn will pass over to the Player B. If is any other number, Player A can choose to hold it, in which case it will be added to the total score of Player A and the turn will pass over to Player B or Player A can choose to roll again and the next number will be added to the current score, without handing over the turn to Player B. However, if anytime the dice lands on a 1, the current score is reset and the turn hands over to Player B. The first player to reach a total score of 50 wins! In a sense this game brings out the real gambler in one. 

How to run:
Download all the contents in the folder and run the index.html file (open in browser) within the folder. 

(2) Map Maker
This is a python program that displays datasets (in csv) on a map using folium. The purpose of this program was simply to experiment with data structures using pandas and then visualise it, which happened to be using folium; as there were easily available geographical data on data.gov website for me to work with :D

How to run:
1. Install folium, pandas and branca modules 
2. Download all the contents of the folder and run the program from within the folder

(3) Motion Detector 
This was a fairly complicated program for me that required multiple references to online materials. This is a python program that detects using an individual's webcam, moving objects that are in range of the camera and draws a rectangle surrounding the moving object. Once the person exits the program, a bokeh graph will open in the browser showing the amount of time the moving object was in frame. For this project, the usage of the webcam is enabled by the builtin cv2 module in python and the data that is fed to the bokeh plot is gathered in a pandas dataframe. This is a project that I aim to further improve the results on as currently it is too easy to trigger false positives and the conditions required to replicate the intended outcome are rather intricate. 

How to run:
1. Start the program on a device with a webcam (if you have multiple webcams, specify in the code in the commented line). This will not work on devices without a webcam.
2. Quickly get out of frame of the webcam such that when the webcam turns on the intial state is motionless  
3. Get back into frame and the program will identify you as a moving object
4. For best results, run the program in an environment without many moving objects
5. To exit the program, press Q on the keyboard.

(4) Password Manager
This is a simple program that utilizes the tkinter module to create a GUI that generates and keeps track of passwords the user creates or assigns to various websites. It outputs a (.txt) file containing the passwords for each website.

How to Run:
Download all the contents in the folder and run the program within the folder

Credits
These projects are built with the help of online course materials. Here are the links of the various github profiles from where you can build these projects as well:

https://github.com/jonasschmedtmann
https://github.com/arditsulceteaching/thepythonmegacourse
https://github.com/angelabauer
