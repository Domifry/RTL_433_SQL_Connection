This Script use the Code of <a href="https://github.com/merbanan/rtl_433">rtl_433</a>
This Script helps you to push every 15 Minutes the current Data of Sensors to a SQL Database.
The Script starts the Stick and reads out for a certain time until it receives one value of every sensor. If it successfull it puts the JSON Data in a SQL Table and sleeps for 15 Minutes. 
If it fails for 100 times it restart the script and after 150 Times it ends the script and you can implement via Pushhover a notication or somehting that you have to restart it. This is just a monitoring notification that maybe one of your sensors is broken.

# Requirements
* You need a RTL-SDR Stick and connect it via USB
* pip install mysql-connector-python
* pip install python3
* <b>Install RTL_SDR first </b>
* git clone git://git.osmocom.org/rtl-sdr.git
* cd rtl-sdr
* mkdir build
* cd build
* cmake -DDETACH_KERNEL_DRIVER=ON ../
* make
* sudo make install
* sudo ldconfig
* <b>Install RTL_433 with this codes </b>
* git clone git://github.com/merbanan/rtl_433
* cd rtl_433
* mkdir build
* cd build
* cmake ../
* make
* sudo make install

# Doing

* Line23: Put your SQL Data in
* Line31 and 28: Put your SQL Statement in
* Start the file SQL_RTL_433.service
* Put the Service file to the right place
* sudo mv SQL_RTL_433.service /etc/systemd/system
* sudo systemctl enable SQL_RTL_433.service
* sudo systemctl start SQL_RTL_433.service
* Check it : sudo systemctl status SQL_RTL_433.service

# PHP File
* I included for you a PHP File how to extract the Data
* Just out in your data and read the comments in the file

# Troubleshooting

* If you do not find your Sensors try:
* proc = subprocess.Popen(['rtl_433','-R', '73', '-F', 'json','-f', '433.9M'], stdout=subprocess.PIPE)
* You can change the 433.9 to 433.8 or 433.95 or 433.85 and many more to find out your sensors
* or try it in the console directly: sudo rtl_433 -f 433.9M
* If you dont find it out just try sudo rtl_433 -M level (you see the frequency of the sensors)
* My perfect frequency for this sensors is 433.95M

# Sensors and Hardware
I use this sensors and they work fine!
* Temperature: <a href="https://amzn.to/3oPndbq">TFA Dostmann Thermo-Hygro-Sender, 30.3221.02</a>
* Rain: <a href ="https://amzn.to/3Dqihh4">TFA Dostmann 30.3222.02</a>
* Wind: <a href="https://amzn.to/30eydor">TFA Dostmann 30.3161 </a>
* Stick: <a href="https://amzn.to/3anco7Z"> RTL-SDR Stick </a>
* Antenna: <a href="https://amzn.to/3mDJS7I">BINGFU Funkgerät Antenne </a>
* Active USB HUB (Energy): <a href="https://amzn.to/3arlGj8"> CSL USB HUB </a>

# Find out your Sensors ID
* sudo rtl_433 -F json
* Check your sensors and write down the ID's
* Put it in your file and what you want like:
* if "12345" in json and sensor3 == False and "wind_avg_km_h" in json: (for the Wind Sensor)
* Other wise you normally use: if "12345" in json and sensor2 == False (for temperature and humandity)
