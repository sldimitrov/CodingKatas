const { iterativeBinarySearch } = require('./index.js');

test('finds 5 in sorted array', () => {
  expect(iterativeBinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)).toBe(true);
})

test('does not find 0 in sorted array', () => {
  expect(iterativeBinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)).toBe(false);
})

test('handles empty array', () => {
  expect(iterativeBinarySearch([], 1)).toBe(false);
});
