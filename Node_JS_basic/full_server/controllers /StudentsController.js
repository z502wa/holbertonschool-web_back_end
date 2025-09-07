/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: full_server/controllers/StudentsController.js
 * Description: Controller for students listing endpoints.
 */

'use strict';

import readDatabase from '../utils.js';

class StudentsController {
  /**
   * GET /students
   * - First line: "This is the list of our students"
   * - For each field (alphabetically, case-insensitive):
   *   "Number of students in FIELD: N. List: name1, name2, ..."
   */
  static async getAllStudents(_req, res) {
    try {
      // Retrieve DB path at execution time (not at require-time), as required by the checker
      const dbPath = process.argv[2];
      const map = await readDatabase(dbPath);

      const header = 'This is the list of our students';
      const fields = Object.keys(map).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      const lines = [header];
      for (const field of fields) {
        const list = map[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      res.status(200).send(lines.join('\n'));
    } catch (_err) {
      res.status(500).send('Cannot load the database');
    }
  }

  /**
   * GET /students/:major
   * - major must be "CS" or "SWE"
   * - Response: "List: name1, name2, ..."
   */
  static async getAllStudentsByMajor(req, res) {
    try {
      const { major } = req.params;
      if (major !== 'CS' && major !== 'SWE') {
        res.status(500).send('Major parameter must be CS or SWE');
        return;
      }

      const dbPath = process.argv[2];
      const map = await readDatabase(dbPath);
      const list = map[major] || [];

      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (_err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
