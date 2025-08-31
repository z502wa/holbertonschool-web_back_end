/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that creates an Int8 typed array and sets a value at a specific position
export default function createInt8TypedArray(length, position, value) {
  // Check if the position is outside the allowed range
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer with the given length
  const buffer = new ArrayBuffer(length);

  // Create a DataView to manipulate the buffer
  const view = new DataView(buffer);

  // Set the Int8 value at the given position
  view.setInt8(position, value);

  // Return the DataView
  return view;
}
