var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var bits = input.split(' ');
var error = false;
for (let i = 0; i < bits.length; i++) {
    if(bits[i] == 9){
        error = true;
        break;
    }
}
if(error){
    console.log("F");
} else {
    console.log("S");
}