#!/usr/bin/env/python3

#Import libraries

import os
from time import sleep 


#Sudo check

#if os.geteuid() != 0:
 #   exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

#Welcome

print("Welcome to the pyducky script, please choose a program: \n")

#Get the required instructions

print("1) Reverse Shell\t 2) Turn off Anti-Virus")
print("3) Wifi Extractor\t 4) Rickroll (Mac Functionality)")
print("5) Hacked Message (Mac Functionality)\t 6) Custom\n")

file = int(input("Please type a number and press enter: "))

print("")

#Preparing the pico

input("Please hold the boot select button and connect the pico. (Make sure you are in the Downloads/pyducky-main folder) Press enter when it shows up...")

sleep(5)

print("Formatting pico...")
os.system("cp src/format.uf2 /Volumes/RPI-RP2/ ")

sleep(20)

print("Flashing circuit python...")
os.system("cp src/circuit_python.uf2 /Volumes/RPI-RP2/ ")

sleep(20)

print("Copying libraries...")
os.system("cp -r src/lib/adafruit_hid /Volumes/CIRCUITPY/lib/")

sleep(10)

print("Copying main program...")
os.system("cp src/code.py /Volumes/CIRCUITPY/code.py")

sleep(2)

print("Preparation done!\n")

#Flashing the right program

if file == 1:
    input("Please modify the file src/scripts/reverse.dd to your needs the press enter...")
    os.system("cp src/scripts/reverse.dd /Volumes/CIRCUITPY/payload.dd")
    print("Transfered Reverse Shell")
elif file == 2:
    os.system("cp src/scripts/antivaitusoff.dd /Volumes/CIRCUITPY/payload.dd")
    print("Transfered Turn off Antivirus")
elif file == 3:
    input("Please modify src/scripts/extractor.dd to your needs then press enter...")
    os.system("cp src/scripts/extractor.dd /Volumes/CIRCUITPY/payload.dd")
    print("Transfered Wifi Extractor\n")
elif file == 4:
    oneortwo = int(input("Please select 1 for complicated or 2 for simple: (Note: Only option 2 has MacOS Terminal Functionality)"))
    if oneortwo == 1:
        os.system("cp src/scripts/rickrollcomp.dd /Volumes/CIRCUITPY/payload.dd")
    elif oneortwo == 2:
        os.system("cp src/scripts/macrickrollsimple.dd /Volumes/CIRCUITPY/payload.dd")
    print("Tranfered Rickroll\n")
elif file == 5:
    os.system("cp src/scripts/machacked.dd /Volumes/CIRCUITPY/payload.dd")
    print("Transfered Hacked Message\n")
elif file == 6:
    input("Create your custom file src/scripts/custom.dd and press enter...")
    os.system("cp src/scripts/custom.dd /Volumes/CIRCUITPY/payload.dd")
    print("Transferred custom file.\n")
else:
    exit("Wrong number please rerun the script...")


print("Your pico is ready to go! Please do not use this for mailicious purposes...")
sleep(0.5)
exit("Bye!")

    
