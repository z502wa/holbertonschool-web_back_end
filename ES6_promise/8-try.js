/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that divides two numbers and throws an error if denominator is 0
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
