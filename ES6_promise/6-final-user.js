/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

// Function that handles multiple promises and returns their settled results
export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);
}
