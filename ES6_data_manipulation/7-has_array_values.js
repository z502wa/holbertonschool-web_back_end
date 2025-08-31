/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that checks if all elements of an array exist in a given Set
export default function hasValuesFromArray(set, array) {
  // Use every to ensure all array elements are present in the Set
  return array.every((element) => set.has(element));
}
