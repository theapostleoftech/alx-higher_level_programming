#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      theFunction();
    }
  }
};
