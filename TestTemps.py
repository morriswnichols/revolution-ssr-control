import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

tankTemp= []
headTemp=[]
arduinoData = serial.Serial('/dev/ttyACM0', 115200) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(60,200)                                 #Set y min and max values
    plt.title('Revolution Rum Temp Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp F')                            #Set ylabels
    plt.plot(tankTemp, 'ro-', label='Tank Temp')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(60,200)                                 #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(headTemp, 'b^-', label='Head Temp') #plot pressure data
    plt2.set_ylabel('Temp F')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    

while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    tank = float( dataArray[0])            #Convert first element to floating number and put in temp
    head = float( dataArray[1])            #Convert second element to floating number and put in P
    tankTemp.append(tank)                     #Build our tempF array by appending temp readings
    headTemp.append(head)                     #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>500):                            #If you have 500 or more points, delete the first one from the array
        tankTemp.pop(0)                       #This allows us to just see the last 50 data points
        headTemp.pop(0)
