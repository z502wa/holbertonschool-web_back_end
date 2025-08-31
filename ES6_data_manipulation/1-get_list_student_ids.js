/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns an array of student IDs from a list of student objects
export default function getListStudentIds(students) {
  // Check if the argument is not an array, return an empty array
  if (!Array.isArray(students)) {
    return [];
  }

  // Use map to extract the id from each student object
  return students.map((student) => student.id);
}
