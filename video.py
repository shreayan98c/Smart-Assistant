#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the OpenCV library
import cv2
import time
# Importing python text ot speech library
import pyttsx3


# In[2]:


# Initializing the engine
engine = pyttsx3.init()


# In[3]:


# Initializing video
video = cv2.VideoCapture('http://192.168.1.2:4747/video/mjpegfeed?640x480')


# In[4]:


# Creating a CascadeClassifier
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
# body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
# numberplate_cascade = cv2.CascadeClassifier("haarcascade_licence_plate_rus_16stages.xml")


# In[5]:


# Initialize the flag variable
flag = 1


# In[6]:


while True:
    flag+=1
    check, frame = video.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_found = 0
    # Search co-ordinates of face
    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)
    for x,y,w,h in faces:
        face_found = 1
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow('Capturing', frame)
    
    # Waiting for 1ms
    key = cv2.waitKey(1)
    # Break if user presses quit
    if(key==ord('q')):
        break


# In[7]:


if(face_found==1):
    engine.say("Careful, there is a person ahead!")
    engine.runAndWait()
else:
    engine.say("Your path is clear!")
    engine.runAndWait()


# In[8]:


print(flag)


# In[9]:


video.release()


# In[10]:


cv2.destroyAllWindows()

