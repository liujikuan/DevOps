const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Home</title>
            </head>
            <body>
                <a href="/signin">Sign In</a>
            </body>
            </html>
        `);
        res.end();
    } else if (req.url === '/signin') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Sign In Page</title>
            </head>
            <body>
                <h1>Welcome to the Sign In Page</h1>
            </body>
            </html>
        `);
        res.end();
    } else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.write('404 Not Found');
        res.end();
    }
});

server.listen(8080, () => {
    console.log('Server is running on http://localhost:8080');
});