/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that updates map items with quantity 1 to 100
export default function updateUniqueItems(map) {
  // Check if the argument is not a Map, throw an error
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate through map entries
  map.forEach((value, key) => {
    // If the quantity is 1, update it to 100
    if (value === 1) {
      map.set(key, 100);
    }
  });

  // Return the updated map
  return map;
}
