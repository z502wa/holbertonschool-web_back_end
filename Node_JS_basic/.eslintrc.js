/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: .eslintrc.js
 * Description: ESLint config aligned with AirBnB Base for Node projects.
 */

'use strict';

module.exports = {
  env: {
    browser: false,
    es2021: true,
    node: true,
    jest: true,
  },
  extends: ['airbnb-base'],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {
    'no-console': 'off',
    'import/extensions': ['error', 'ignorePackages', { js: 'always' }],
  },
};
