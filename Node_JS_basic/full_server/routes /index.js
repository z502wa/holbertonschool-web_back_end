/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: full_server/routes/index.js
 * Description: Express router wiring App and Students controllers.
 */

'use strict';

import { Router } from 'express';
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const router = Router();

// Home
router.get('/', AppController.getHomepage);

// Students
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
