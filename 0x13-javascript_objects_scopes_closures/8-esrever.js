#!/usr/bin/node

exports.esrever = function (list) {
  const r = [];
  for (let x = list.length - 1; x >= 0; x--) {
    r.push(list[x]);
  }
  return r;
};
