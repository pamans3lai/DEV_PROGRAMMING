<?php

$str = 'Ini adalah tes';
$pertama = $str[0];
echo '$pertama' . PHP_EOL;

$ketiga = $str[2];

$str = 'ini masih tes';
$akhir = $str[strlen($str) - 1];

$str = 'lihat ke laut';
$str[strlen($str) - 1];

$str = 'Look at the sea';
$str[strlen($str) - 1] = 'e';
