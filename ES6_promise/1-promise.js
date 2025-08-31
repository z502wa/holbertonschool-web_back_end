/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns a Promise based on the success parameter
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      // Resolve with status and body when success is true
      resolve({ status: 200, body: 'Success' });
    } else {
      // Reject with an error when success is false
      reject(new Error('The fake API is not working currently'));
    }
  });
}
