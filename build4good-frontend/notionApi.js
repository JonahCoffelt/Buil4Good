
const http = require('http');
const https = require('https');
const { URL } = require('url');

const NOTION_API_KEY = 'secret_cqvLNy1oJA7hy1A4yv3nx5u7yEROhpW3gmcQfeUab72';
const DATABASE_ID = '7a276b34a7914843a66ef1cec7cebecc';

http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*'); // Allow requests from any origin

  if (req.method === 'OPTIONS') {
    // Handle preflight request
    res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Authorization,Content-Type');
    res.writeHead(200);
    res.end();
    return;
  }

  if (req.url === '/fetchData') {
    fetchData(req, res);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
}).listen(3000, () => {
  console.log('CORS-enabled web server listening on port 3000');
});

function fetchData(req, res) {
  const url = new URL(`https://api.notion.com/v1/databases/${DATABASE_ID}/query`);
  const options = {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${NOTION_API_KEY}`,
      'Notion-Version': '2021-05-13',
      'Content-Type': 'application/json',
    },
  };

  const proxyReq = https.request(url, options, (proxyRes) => {
    let data = '';
    proxyRes.on('data', (chunk) => {
      data += chunk;
    });
    proxyRes.on('end', () => {
      res.setHeader('Content-Type', 'application/json');
      res.writeHead(proxyRes.statusCode);
      res.end(data);
    });
  });

  proxyReq.on('error', (error) => {
    console.error('Proxy request error:', error);
    res.writeHead(500);
    res.end(JSON.stringify({ error: 'Failed to fetch data' }));
  });

  proxyReq.end();
}