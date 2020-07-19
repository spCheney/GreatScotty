import tkinter as tk
from PIL import ImageTk,Image
import RPi.GPIO as GPIO
import time
import threading

eighth_oz = 2.5
sixteenth_oz = 1.25

class Bartender():
    def __init__(self):
        
        #set up display
        window = tk.Tk()
        window.attributes('-fullscreen', True)

        #set up GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
        
        #this needs to be changed to be the full path of wherever you store the pictures
        pic_dir = "/home/pi/Desktop/GreatScotty/GreatScottyPics/"

        #creating images to be displayed
        watermelon = Bartender.createImage(pic_dir + "watermelon_text.png")
        mango = Bartender.createImage(pic_dir + "mango_text.png")
        cherry = Bartender.createImage(pic_dir + "cherry_text.png")
        kiwi = Bartender.createImage(pic_dir + "kiwi_text.png")
        grape = Bartender.createImage(pic_dir + "grape_text.png")
        peach = Bartender.createImage(pic_dir + "peach_text.png")
        strawberry = Bartender.createImage(pic_dir + "strawberry_text.png")
        coconut = Bartender.createImage(pic_dir + "coconut_text.png")
        raspberry = Bartender.createImage(pic_dir + "raspberry_text.png")
        tangerine = Bartender.createImage(pic_dir + "tangerine_text.png")
        thot_i_am_not = Bartender.createImage(pic_dir + "thot_I_am_not.png")
        bahama_blast = Bartender.createImage(pic_dir + "bahama_blast.png")
        cool_tool = Bartender.createImage(pic_dir + "cool_tool.png")
        kylorenzo = Bartender.createImage(pic_dir + "kyLo-renzo.png")
        eye_of_the_tiger = Bartender.createImage(pic_dir + "eye_of_the_tiger.png")
        get_er_dunn = Bartender.createImage(pic_dir + "get_er_dunn.png")
        
        #creating buttons
        watermelon_btn = tk.Button(window, image=watermelon, command=lambda:
                              Bartender.pour(27,eighth_oz * 4))
        watermelon_btn.grid(row=0, column=0)

        mango_btn = tk.Button(window, image=mango, command=lambda:
                              Bartender.pour(17,eighth_oz * 4))
        mango_btn.grid(row=0, column=1)

        cherry_btn = tk.Button(window, image=cherry, command=lambda:
                              Bartender.pour(22,eighth_oz * 4))
        cherry_btn.grid(row=0, column=2)

        kiwi_btn = tk.Button(window, image=kiwi, command=lambda:
                              Bartender.pour(23,eighth_oz * 4))
        kiwi_btn.grid(row=0, column=3)
        
        grape_btn = tk.Button(window, image=grape, command=lambda:
                              Bartender.pour(27,eighth_oz))
        grape_btn.grid(row=0, column=4)

        peach_btn = tk.Button(window, image=peach, command=lambda:
                              Bartender.pour(17,eighth_oz))
        peach_btn.grid(row=1, column=0)

        strawberry_btn = tk.Button(window, image=strawberry, command=lambda:
                              Bartender.pour(22,eighth_oz))
        strawberry_btn.grid(row=1, column=1)

        coconut_btn = tk.Button(window, image=coconut, command=lambda:
                              Bartender.pour(23,eighth_oz))
        coconut_btn.grid(row=1, column=2)
        
        raspberry_btn = tk.Button(window, image=raspberry, command=lambda:
                              Bartender.pour(27,eighth_oz))
        raspberry_btn.grid(row=1, column=3)

        tangerine_btn = tk.Button(window, image=tangerine, command=lambda:
                              Bartender.pour(17,eighth_oz))
        tangerine_btn.grid(row=1, column=4)
        
        get_er_dunn_btn = tk.Button(window, image=get_er_dunn, command=lambda:
                              Bartender.getErDunn())
        get_er_dunn_btn.grid(row=2, column=0)
        
        kylorenzo_btn = tk.Button(window, image=kylorenzo, command=lambda:
                              Bartender.kylorenzo())
        kylorenzo_btn.grid(row=2, column=1)

        cool_tool_btn = tk.Button(window, image=cool_tool, command=lambda:
                              Bartender.coolTool())
        cool_tool_btn.grid(row=2, column=2)
        
        eye_of_the_tiger_btn = tk.Button(window, image=eye_of_the_tiger, command=lambda:
                              Bartender.eyeOfTheTiger())
        eye_of_the_tiger_btn.grid(row=2, column=3)

        thot_i_am_not_btn = tk.Button(window, image=thot_i_am_not, command=lambda:
                              Bartender.thotIAmNot())
        thot_i_am_not_btn.grid(row=2, column=4)

        
        window.mainloop()
        
    def getErDunn(self):
        threads = []
        thread1 = threading.Thread(target=Bartender.pour, args=(27, eighth_oz * 10))
        thread2 = threading.Thread(target=Bartender.pour, args=(17, eighth_oz * 10))
        thread3 = threading.Thread(target=Bartender.pour, args=(22, eighth_oz * 10))
        thread4 = threading.Thread(target=Bartender.pour, args=(23, eighth_oz * 6))
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        threads.append(thread4)
        for thread in threads:
            thread.start()
      
    def coolTool(self):
        threads = []
        thread1 = threading.Thread(target=Bartender.pour, args=(22, eighth_oz * 6))
        thread2 = threading.Thread(target=Bartender.pour, args=(23, eighth_oz * 6))
        threads.append(thread1)
        threads.append(thread2)
        for thread in threads:
            thread.start()
      
    def eyeOfTheTiger(self):
        threads = []
        thread1 = threading.Thread(target=Bartender.pour, args=(22, eighth_oz * 6))
        thread2 = threading.Thread(target=Bartender.pour, args=(23, eighth_oz * 12))
        threads.append(thread1)
        threads.append(thread2)
        for thread in threads:
            thread.start()
      
    def thotIAmNot(self):
        threads = []
        thread1 = threading.Thread(target=Bartender.pour, args=(17, eighth_oz * 6))
        thread2 = threading.Thread(target=Bartender.pour, args=(22, eighth_oz * 6))
        thread3 = threading.Thread(target=Bartender.pour, args=(23, eighth_oz * 6))
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        for thread in threads:
            thread.start()
            
    def kylorenzo(self):
        threads = []
        thread1 = threading.Thread(target=Bartender.pour, args=(27, eighth_oz * 4))
        thread2 = threading.Thread(target=Bartender.pour, args=(17, eighth_oz * 4))
        thread3 = threading.Thread(target=Bartender.pour, args=(22, eighth_oz * 4))
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        for thread in threads:
            thread.start()

    def createImage(self, img_path): 
       image = Image.open(img_path)
       size = (200, 200)
       resized = image.resize(size)
       return ImageTk.PhotoImage(resized)

    def pour(self, pin, waitTime):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(waitTime)
        GPIO.output(pin, GPIO.LOW)


bartender = Bartender()
