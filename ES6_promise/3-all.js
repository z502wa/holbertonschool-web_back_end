/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

import { uploadPhoto, createUser } from './utils';

// Function that handles profile signup by resolving multiple promises
export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const [photo, user] = results;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
