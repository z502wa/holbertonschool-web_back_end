/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: full_server/utils.js
 * Description: Asynchronously read a CSV database and return an object mapping fields to arrays of first names.
 */

'use strict';

import { promises as fs } from 'fs';

/**
 * readDatabase
 * @param {string} filePath - Path to CSV file
 * @returns {Promise<Record<string, string[]>>} - { CS: ['Johann', ...], SWE: ['Guillaume', ...] }
 * - Reads the database asynchronously
 * - Resolves with an object of arrays of first names per field (order preserved by file appearance)
 * - Rejects with the original error if file is not accessible
 */
async function readDatabase(filePath) {
  if (!filePath) {
    throw new Error('Cannot load the database');
  }

  try {
    const content = await fs.readFile(filePath, { encoding: 'utf8' });
    const lines = content
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    // Expect header: firstname,lastname,age,field
    const dataLines = lines.slice(1);
    const map = {};

    for (const line of dataLines) {
      const parts = line.split(',');
      if (parts.length >= 4) {
        const firstname = parts[0].trim();
        const field = parts[3].trim();
        if (firstname && field) {
          if (!Object.prototype.hasOwnProperty.call(map, field)) {
            map[field] = [];
          }
          map[field].push(firstname);
        }
      }
    }

    return map;
  } catch (err) {
    // Per spec: reject with the error; controllers map this to the required message
    throw new Error('Cannot load the database');
  }
}

export default readDatabase;
