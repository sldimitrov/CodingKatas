// Binary Search Algorithm Implementation #1
// const targetValue = 10;
// const sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//
// let leftIdx = 0;
// let rightIdx = sortedArray.length;
//
// for (let i = 0; i <= sortedArray.length; i++) {
//   let midIndex = Math.floor((leftIdx + rightIdx) / 2);
//
//   const currentValue = sortedArray[midIndex];
//
//   if (currentValue === targetValue) {
//     break;
//   } else if (currentValue < targetValue) {
//     leftIdx = midIndex;
//   } else if (currentValue > targetValue) {
//     rightIdx = midIndex;
//   }
//
//   if (midIndex === 0 || midIndex === sortedArray.length - 1) {
//     break;
//   }
// }

// Binary Search Algorithm Implementation #2
const target = 9;
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let left = 0;
let right = arr.length - 1;
let found = false;

while (left <= right) {
  let midIdx = Math.floor((left + right) / 2);
  let currentValue = arr[midIdx];

  if (currentValue < target) {
    left = midIdx + 1;
  } else if (currentValue > target) {
    right = midIdx - 1;
  } else {
    console.log(`You have found the target value ${target} on index ${midIdx}`);
    found = true;
    break;
  }

  if (midIdx === 0 || midIdx === arr.length - 1) {
    break;
  }
}

if (!found) {
  console.log('Number was not found in the array')
}

// Binary Search Algorithm Implementation #3
const target = 9;
