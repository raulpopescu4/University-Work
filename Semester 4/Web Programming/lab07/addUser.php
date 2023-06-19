<?php
require_once "configuration.php";

$name = $_POST['name'];
$username = $_POST['username'];
$password = $_POST['password'];
$age = $_POST['age'];
$role = $_POST['role'];
$email = $_POST['email'];
$webpage = $_POST['webpage'];

$errors = [];
if (empty($name)) {
    $errors[] = "Name is required";
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = "Invalid email format";
}

if (strlen($password) < 3) {
    $errors[] = "The password must be at least 3 characters long";
}

if (!empty($errors)) {

    $errorString = implode(",", $errors);
    echo $errorString;
    exit;
}

$sql_query = "insert into user(name, username, password, age, role, email, webpage) values ('$name', '$username', '$password', $age, '$role', '$email', '$webpage')";
global $connection;
$result = mysqli_query($connection, $sql_query);
if ($result) {
    echo "Your user was added successfully!";
    header("Location: showUsers.html");
} else {
    echo "Oops!Something went wrong and your document cannot be added!Please try again later.";
}
mysqli_close($connection);