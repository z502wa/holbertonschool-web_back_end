const fs = require('fs').promises;

const listName = (list) => list.map((element) => element[0]).join(', ');

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
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
      return (
        `Number of students: ${nbStudent}\n`
        + `Number of students in CS: ${nbStudentCS.length}. List: ${listName(nbStudentCS)}\n`
        + `Number of students in SWE: ${nbStudentSWE.length}. List: ${listName(nbStudentSWE)}`
      );
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = listName;
module.exports = countStudents;
