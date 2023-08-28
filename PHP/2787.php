<?php
$n1 = trim(fgets(STDIN));
$n2 = trim(fgets(STDIN));

if($n1%2 == 0 && $n2%2 == 0){
    printf("%d\n", 1);
} elseif ($n1%2 != 0 && $n2%2 != 0) {
    printf("%d\n", 1);
} else {
    printf("%d\n", 0);
}
?>