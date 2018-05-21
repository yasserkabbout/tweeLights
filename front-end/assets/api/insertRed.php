<html>

<head> </head>

<?php
$servername = "yasserkabboutcom.ipagemysql.com";
$username = "yasser";
$password = "yasser";
$dbname = "twee_lights";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO winners_colors (store_id, winner_color)
VALUES (1, 'RED')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
</body>

</html>