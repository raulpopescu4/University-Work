<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET,POST,PUT");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$HOST = 'localhost';
$USERNAME = 'root';
$PASSWORD = ''; 
$DBNAME = 'examprep';

// Here we connect to the database and find the table name and the columns that we need 
$con = mysqli_connect($HOST, $USERNAME, $PASSWORD, $DBNAME);
if ($con != null && !$con ) {
    die('Could not connect: ' . mysqli_error($con));
}
?>