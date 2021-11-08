var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        
        var upTimeInSeconds=process.uptime();
        var upTimeInMinutes = upTimeInSeconds / 60;
        var upTimeInHours = upTimeInMinutes / 60;
        var upTimeInDays = upTimeInHours / 24;
        upTimeInSeconds = Math.floor(upTimeInSeconds);
        upTimeInMinutes = Math.floor(upTimeInMinutes);
        upTimeInHours = Math.floor(upTimeInHours);
        upTimeInDays = Math.floor(upTimeInDays);

        totalMem = os.totalmem();
        totalMemInMB = totalMem / 10000;

        freeMem=os.freemem();
        freeMemInMB = freeMem / 10000;

        cpuNum = os.cpus().length;

        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${upTimeInDays}, Hours: ${upTimeInHours}, Minutes: ${upTimeInMinutes}, Seconds: ${upTimeInSeconds}</p>
            <p>Total Memory: ${totalMemInMB} MB</p>
            <p>Free Memory: ${freeMemInMB} MB</p>
            <p>Number of CPUs: ${cpuNum}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
