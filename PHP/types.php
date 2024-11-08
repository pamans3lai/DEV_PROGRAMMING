<?php

$a_bool = true;
$a_str = "foo";
$_str2 = 'foo';
$an_int = 12;

echo get_debug_type($a_bool), "\n";
echo get_debug_type($a_str), "\n";

if (is_int($an_int)) {
    $an_int += 4;
}

var_dump($an_int);

if (is_bool($a_bool)) {
    echo "String: $a_bool";
}
