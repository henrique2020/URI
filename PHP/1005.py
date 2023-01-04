<?php
$a = trim(fgets(STDIN));
$a *= 3.5;
$b = trim(fgets(STDIN));
$b *= 7.5;

$media = ($a+$b)/11;
printf("MEDIA = %.5f\n", $media);
?>
