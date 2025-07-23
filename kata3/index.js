// TASK: 1
// Finding the number of binary digits needed for representation of big numbers
function bitsRequired(n) {
  return Math.floor(Math.log2(n) + 1);
}

console.log("Task #1");
console.log(`Bits required for 1,000 - ${bitsRequired(1000)}`);
console.log(`Bits required for 1,000,000 - ${bitsRequired(1000000)}`);
console.log(`Bits required for 1,000,000,000 - ${bitsRequired(1000000000)}`);
console.log(`Bits required for 1,000,000,000 - ${bitsRequired(1000000000000)}`);
console.log(`Bits required for 8,000,000,000 - ${bitsRequired(8000000000000)}`);
console.log("");

// TASK: 2
// Calculate the space for storing the data for number of residences
const resicences = 20000;

// Rough Representation of average characters
let residenceName = 20;
let residenceAdresses = 15;
let residenceNumber = 10;
const averageCharsPerRes = residenceName + residenceAdresses + residenceNumber;

// Character uses 8 nimary digits (bits) also known as a byte to represent in computer memory
const averageDigitsPerRes = averageCharsPerRes * 8;

const townResidencesInBits = resicences * averageCharsPerRes;
const townResidencesInBytes = townResidencesInBits / 8;
const townResidencesInMegaBytes = townResidencesInBytes / 1000000;

console.log("Task #2");
console.log(`Bits Representation = ${townResidencesInBits}`);
console.log(`Bytes Representation = ${townResidencesInBytes}`);
console.log(`Megabytes Representation = ${townResidencesInMegaBytes}`);

// TASK: 3
// Storing 1,000,000 integers in a binary tree.
const integers = 1000000;

console.log("Task #3");
// TODO: Calculate how many noded and levels the tree will have.
