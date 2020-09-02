<?php
require_once 'Car.php';
require_once 'Account.php';
$car = new Car("AMS457", new Account("Andres Herrera", "AND123"));
print_r($car);
print_r($car->driver);
?>