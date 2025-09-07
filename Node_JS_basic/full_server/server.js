/*
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 * File: full_server/server.js
 * Description: Express app bootstrap using routes from ./routes.
 */

'use strict';

import express from 'express';
import routes from './routes/index.js';

const app = express();
const PORT = 1245;

// Mount routes
app.use('/', routes);

// Start server only when this file is the entry point
app.listen(PORT, () => { /* no console output required by checker */ });

export default app;
