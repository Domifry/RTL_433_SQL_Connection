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

# Troubleshooting

* If you do not find your Sensors try:
* proc = subprocess.Popen(['rtl_433','-R', '73', '-F', 'json','-f', '433.9M'], stdout=subprocess.PIPE)
* You can change the 433.9 to 433.8 and many more to find out your sensors
* or try it in the console directly: sudo rtl_433 -F json -f 433.9M

# Sensors ahd Hardware
I use this sensors and they work fine!
* Temperature: <a href="https://amzn.to/3oPndbq">TFA Dostmann Thermo-Hygro-Sender, 30.3221.02</a>
* Rain: <ahref ="https://amzn.to/3Dqihh4">TFA Dostmann 30.3222.02</a>
* Wind: <a href="https://amzn.to/30eydor">TFA Dostmann 30.3161 </a> (I will test this sensor until 15.10.21 and give an Update)
* Stick: <a href="https://amzn.to/3anco7Z"> RTL-SDR Stick </a>
* Antenna: <href="https://amzn.to/3aExHlH"> Delock 88877 ISM SMA Omni Star  </a>
* Active USB HUB (Energy): <a href="https://amzn.to/3arlGj8"> CSL USB HUB </a>
