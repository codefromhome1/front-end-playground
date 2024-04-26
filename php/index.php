<?php

// variable
$name = "John Doe";
$age  = 30;

echo "<h1>My name is $name and I am $age years old.</h1>"; // output: My name is John Doe and I am 30 years old.
// echo statement
echo "My name is $name and I am $age years old." . "<br>";

// concatenation operator (.)
echo "I live in New York City" . ", which is known for its skyscrapers." . "<br>" ;

// string interpolation / variable substitution
$city = "Los Angeles";
echo "I also live in $city, which is famous for its beaches." . "<br>";



// PHP Operators
/*
 * Arithmetic operators: +, -, /, * %
 */
$x = 5;
$y = 2;

echo "$x + $y = " . ($x + $y) . "<br>"; // prints 7
echo "$x - $y = " . ($x - $y) . "<br>"; // prints 3
echo "$x / $y = " . ($x / $y) . "<br>"; // prints 2.5
echo "$x * $y = " . ($x * $y) . "<br>"; // prints 10
echo "$x % $y = " . ($x % $y) . "<br>"; // prints 1
?>

