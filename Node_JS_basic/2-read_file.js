const fs = require('fs');

const listName = (list) => list.map((element) => element[0]).join(', ');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path).toLocaleString();
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  let start = true;
  let nbStudent = 0;
  const nbStudentCS = [];
  const nbStudentSWE = [];
  const rows = data.split('\n');

  rows.forEach((row) => {
    const columns = row.split(',');
    if (!start && columns[0] !== '') {
      if (columns[3] === 'CS') {
        nbStudentCS.push(columns);
      } else {
        nbStudentSWE.push(columns);
      }
      nbStudent += 1;
    }
    start = false;
  });
  console.log(`Number of students: ${nbStudent}`);
  console.log(`Number of students in CS: ${nbStudentCS.length}. List: ${listName(nbStudentCS)}`);
  console.log(`Number of students in SWE: ${nbStudentSWE.length}. List: ${listName(nbStudentSWE)}`);
}

module.exports = listName;
module.exports = countStudents;
