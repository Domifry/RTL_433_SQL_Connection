#!/usr/bin/env python3

#Autor https://github.com/Domifry
#with help of https://github.com/mrkwenzel
#usage of the rtl_433 of https://github.com/merbanan/rtl_433

import mysql.connector
import time
import subprocess
import os
import sys

proc = subprocess.Popen(['rtl_433', '-F', 'json'], stdout=subprocess.PIPE)
sensor1 = False
sensor2 = False
json1 = line.rstrip()
#sorry for this but the string makes some lines that it is bad for SQL
json = str(json1)
json = json.lstrip("'")
json = json.lstrip("b")
json = json.lstrip("'")
json = json.rstrip("'")
connected = False
counter = 0

while True:
  line = proc.stdout.readline()
  json1 = line.rstrip()
  json = str(json1)
  counter+=1
  #if not line:
  #  break
  if connected == False:  
   connection = mysql.connector.connect(host="IP", user="USER", passwd="PASS", db="DB")
   cursor = connection.cursor()
   connected = True
  if "Sensor1-ID" in json and sensor1 == False:
    statement = "SQL Statement'"+json+"'statement"
    cursor.execute(statement)
    sensor1 = True
   if "Sensor2-ID" in json and sensor2 == False:
     statement = "SQL Statement'"+json+"'statement"
     cursor.execute(statement)
     sensor2 = True
   if counter == 100:
     proc = subprocess.Popen(['rtl_433', '-F', 'json'], stdout=subprocess.PIPE)
   if counter == 150:
     break
     #here you can send yourself a Mail or a push
   if sensor1 == True and sensor2 == True:
      sensor1 = False
      sensor2 = False
      connected = False
      connection.commit()
      cursor.close()
      counter = 0
      time.sleep(900)
