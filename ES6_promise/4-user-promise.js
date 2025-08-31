/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns a resolved Promise with user details
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
