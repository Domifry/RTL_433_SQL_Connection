<?php
$Datenbank = "put in";
$Passwort = "put in";

global $Datenbank, $Passwort;
	// Create connection
$con=mysqli_connect("localhost",$Datenbank,$Passwort,$Datenbank);

// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
//I show you how to give out the last Data
$sql = "SELECT * FROM `Tablename` ORDER BY `ID` DESC LIMIT 0 , 20";

//insert tablename
$result = mysqli_query($con, "SELECT COUNT(ID) as anzahl FROM `Tablename`");
$data=mysqli_fetch_assoc($result);
$total = $data['anzahl'];

//give me last value
$result = mysqli_query($con, 'SELECT * FROM `Wind` WHERE ID='.$total);
$row = $result->fetch_array();

//put in how your row name is e.g. wind
$json = $row['rownameinsert'];
$json1 = json_decode($json,true);

//put in the value you need
$wind = $json1["wind_avg_km_h"];
$emperature = $json1

//print out the value
echo($value);
?>
