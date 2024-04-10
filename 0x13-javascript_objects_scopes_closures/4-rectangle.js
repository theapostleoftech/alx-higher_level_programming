#!/usr/bin/node
class Rectangle {
    width;
    height;
    constructor(w, h) {
        if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            this.width = undefined;
            this.height = undefined;
        } else {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        if (this.width !== undefined && this.height !== undefined) {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }

    rotate() {
        if (this.width !== undefined && this.height !== undefined) {
            [this.width, this.height] = [this.height, this.width];
        }
    }

    double() {
        if (this.width !== undefined && this.height !== undefined) {
            this.width *= 2;
            this.height *= 2;
        }
    }
}

module.exports = Rectangle;
