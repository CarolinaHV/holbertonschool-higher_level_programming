#!/usr/bin/node
/*
  Write a class Rectangle that defines a rectangle:
  - The constructor must take 2 arguments w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0 or not a positive integer, create an empty object
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // This instance method prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // This instance method multiples the width and the height of the rectangle by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  // This instance method exchanges the width and the height of the rectangle
  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }
}

module.exports = Rectangle;
