import express from 'express';

const HOST = '0.0.0.0';
const PORT = 80;

const app = express();

app.get('/', (_req, res) => {
  res.send('Hello World');
});

console.log(`Starting dev server on http://${HOST}:${PORT}`);
app.listen(PORT, HOST);
