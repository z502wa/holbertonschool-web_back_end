// Suhail Al-aboud - 10675@holbertonstudents.com

// Function that uses const to declare a variable (cannot be reassigned)
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

// Function that returns a static string
export function getLast() {
  return ' is okay';
}

// Function that uses let to declare a variable (can be reassigned or modified)
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast(); // Append the result of getLast()

  return combination;
}
