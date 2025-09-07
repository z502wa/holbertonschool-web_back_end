const http = require('http');
const app = require('express')();

http.createServer(app).listen(1245);
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

module.exports = app;
