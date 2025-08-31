/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns a string of set values starting with a specific string
export default function cleanSet(set, startString) {
  // If startString is not a string or empty, return an empty string
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  // Filter set values that start with startString and remove that prefix
  const filtered = [...set]
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  // Join the resulting substrings with '-'
  return filtered.join('-');
}
