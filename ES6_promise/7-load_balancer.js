/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns the value of the promise that resolves first
export default function loadBalancer(chinaDownload, USDownload) {
  // Promise.race returns the first settled promise (resolved or rejected)
  return Promise.race([chinaDownload, USDownload]);
}
