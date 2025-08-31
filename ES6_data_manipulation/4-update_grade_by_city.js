/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that returns students from a specific city with updated grades
export default function updateStudentGradeByCity(students, city, newGrades) {
  // Filter students based on the given city
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      // Find grade object for the current student
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);

      // Return a new object with student data and updated grade (or 'N/A' if not found)
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
