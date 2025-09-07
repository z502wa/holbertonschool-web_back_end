/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: full_server/controllers/AppController.js
 * Description: Basic controller for the home route.
 */

'use strict';

class AppController {
  /**
   * GET /
   * @param {import('express').Request} _req
   * @param {import('express').Response} res
   */
  static getHomepage(_req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
