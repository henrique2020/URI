var input = require('fs').readFileSync('/dev/stdin', 'utf8');
console.log(input.split(' ').indexOf('1')+1);
