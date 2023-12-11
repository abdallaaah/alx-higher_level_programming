#!/usr/bin/node

function factorialize (num) {
  if (num < 0) { return -1; } else if (num === 0) { return 1; } else {
    return (num * factorialize(num - 1));
  }
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const x = factorialize(parseInt(process.argv[2]));
  console.log(x);
}
