/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: babel.config.js
 * Description: Babel config enabling ES6 on current Node.
 */

'use strict';

module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: { node: 'current' },
      },
    ],
  ],
};
