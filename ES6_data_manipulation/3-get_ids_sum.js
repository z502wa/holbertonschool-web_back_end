/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns the sum of all student IDs
export default function getStudentIdsSum(students) {
  // Use reduce to accumulate the sum of all IDs in the array
  return students.reduce((sum, student) => sum + student.id, 0);
}
