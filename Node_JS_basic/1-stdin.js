/* 
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: 1-stdin.js
 * Description: Read a user's name from STDIN and print it. On program end, print a closing message.
 */

'use strict';

// Print welcome prompt
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Ensure UTF-8 input
process.stdin.setEncoding('utf8');

// Handle user input (first line is enough per task description)
process.stdin.on('data', (chunk) => {
  const name = String(chunk).trim();
  // Echo the user's name in the required format
  process.stdout.write(`Your name is: ${name}\n`);
});

// When input stream ends (e.g., piped input or Ctrl+D), print closing message
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

// Also handle Ctrl+C gracefully to print the closing message before exit
process.on('SIGINT', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});
