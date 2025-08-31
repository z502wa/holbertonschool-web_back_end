/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns students located in a specific city
export default function getStudentsByLocation(students, city) {
  // Use filter to select only students whose location matches the given city
  return students.filter((student) => student.location === city);
}
