<?php
$data = trim(fgets(STDIN));
$data = date_create_from_format("d/m/y", $data);
echo date_format($data, "m/d/y") . "\n";
echo date_format($data, "y/m/d") . "\n";
echo date_format($data, "d-m-y") . "\n";
?>