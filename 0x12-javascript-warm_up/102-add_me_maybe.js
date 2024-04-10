#!/usr/bin/node
exports.addMeMaybe = function (nb, theFunction) {
  const i = nb + 1;
  theFunction(i);
};
