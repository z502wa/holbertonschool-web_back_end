/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that handles a response from a Promise
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' })) // On resolve
    .catch(() => new Error()) // On reject
    .finally(() => {
      // This block always executes
      console.log('Got a response from the API');
    });
}
