#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let sq = '';
      for (let j = 0; j < this.width; j++) {
        sq += 'X';
      }
      console.log(sq);
    }
  }
}

module.exports = Rectangle;
