/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

// Function that handles multiple promises and normalizes results to { status, value }
export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((res) => (
      res.status === 'fulfilled'
        ? { status: res.status, value: res.value }
        // Convert Error to the expected string "Error: <message>"
        : { status: res.status, value: String(res.reason) }
    )),
  );
}
