const http = require("http");
const fs = require("fs");
const path = require("path");

const port = 3000;
const filePath = path.join(__dirname, "index.html");

http.createServer((request, response) => {
  // 브라우저가 접속하면 index.html 파일을 읽어서 보여줍니다.
  fs.readFile(filePath, "utf8", (error, data) => {
    if (error) {
      response.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
      response.end("파일을 불러오는 중 오류가 발생했습니다.");
      return;
    }

    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    response.end(data);
  });
}).listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
