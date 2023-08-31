<?php
$bits = explode(" ", trim(fgets(STDIN)));
if(in_array(9, $bits)){ printf("S\n"); }
else { printf("F\n"); }
?>
