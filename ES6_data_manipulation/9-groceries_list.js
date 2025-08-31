/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns a Map of groceries with their quantities
export default function groceriesList() {
  // Create a new Map and set grocery items with their quantities
  const groceries = new Map();
  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);

  // Return the Map
  return groceries;
}
