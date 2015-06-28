
/**
* Module dependencies.
*/

var fs = require('fs');
var Canvas = require('..');

var canvas = new Canvas(0, 0, "fbdev")
var ctx = canvas.getContext('2d')

console.log("Width: " + canvas.width + ", Height: " + canvas.height);

ctx.fillStyle = "#00FF00";
ctx.fillRect(50, 50, 100, 100);

var outPath = __dirname + '/rectangle.png';

canvas.createPNGStream().pipe(fs.createWriteStream(outPath));