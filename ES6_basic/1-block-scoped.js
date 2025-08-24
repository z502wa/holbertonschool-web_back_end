// Suhail Al-aboud - 10675@holbertonstudents.com

// Function demonstrating block scope using let and const
export default function taskBlock(trueOrFalse) {
  const task = false;   // Using const since this value should not change
  const task2 = true;   // Same here, remains constant

  if (trueOrFalse) {
    // Variables inside this block will not overwrite the outer variables
    const task = true;   // Scoped only inside the if block
    const task2 = false; // Scoped only inside the if block
  }

  // Returns the values defined in the outer scope (not affected by block variables)
  return [task, task2];
}
