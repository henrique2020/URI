<?php
$d = trim(fgets(STDIN));
if ($d <= 800) { printf("%d\n", 1); } 
else if ($d <= 1400) { printf("%d\n", 2); } 
else { printf("%d\n", 3); }
?>
