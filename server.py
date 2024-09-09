import Physics
import phylib

import cgi
import sys
import os

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl;

class MyHandler( BaseHTTPRequestHandler ):


    def do_GET(self):
        parsed  = urlparse( self.path );

        if parsed.path in [ '/webpage.html' ]:

            fp = open( '.'+self.path );
            content = fp.read();

            
            with open('webpage.html', 'r') as fp:
                content = fp.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))

            fp.close();

        elif parsed.path in [ '/animate.html' ]:

            fp = open( '.'+self.path );
            content = fp.read();

            
            with open('animate.html', 'r') as fp:
                content = fp.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))

            fp.close();

        elif parsed.path in [ '/animate.js' ]:

            fp = open( '.'+self.path );
            content = fp.read();

            
            with open('animate.js', 'r') as fp:
                content = fp.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))

            fp.close();

        elif parsed.path.startswith('/table-') and parsed.path.endswith('.svg'): 
            file_path = parsed.path.lstrip("/")

            fp = open( '.'+self.path );
            content = fp.read();

            split_table = parsed.path.split('-')
            table_number = split_table[1].split('.')[0]
            file_path = f'table-{table_number}.svg'

            if os.path.exists(file_path):
                fp = open( '.'+self.path );
                content = fp.read();
                self.send_response(200)
                self.send_header('Content-type', 'image/svg+xml')
                self.send_header("Content-length", len(content))
                self.end_headers();
                self.wfile.write(bytes(content, 'utf-8'))
                fp.close();

        elif self.path == '/firstTable.svg':
            file_path = 'firstTable.svg' 

            if os.path.exists(file_path):
                with open(file_path, 'rb') as fp:
                    content = fp.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'image/svg+xml')
                    self.send_header("Content-length", len(content))
                    self.end_headers()
                    self.wfile.write(content)
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("ERROR 404. File: %s not found\n404" % self.path, "utf-8"))

        else:
            self.send_response( 404 );
            self.end_headers();
            self.wfile.write( bytes( "404: %s not found" % self.path, "utf-8" ) );


    def do_POST(self):
        parsed  = urlparse( self.path );

        if parsed.path in [ '/animate.html' ]:

            form = cgi.FieldStorage( fp=self.rfile,
                                     headers=self.headers,
                                     environ = { 'REQUEST_METHOD': 'POST',
                                                 'CONTENT_TYPE': 
                                                   self.headers['Content-Type'],
                                               } 
                                    )

            # remove svg tables from prevoius plays
            serv_dir = './'
            for filename in os.listdir(serv_dir):
                if filename.startswith('table') and filename.endswith('.svg'):
                    file_path = os.path.join(serv_dir, filename)
                    os.remove(file_path) 

            # add balls to table
            sBall1Pos = Physics.Coordinate(675, 690)
            stillBall1 = Physics.StillBall(1,sBall1Pos)
            sBall2Pos = Physics.Coordinate(635, 630)
            stillBall2 = Physics.StillBall(2,sBall2Pos)
            sBall3Pos = Physics.Coordinate(730, 630)
            stillBall3 = Physics.StillBall(3,sBall3Pos)
            sBall4Pos = Physics.Coordinate(580, 590)
            stillBall4 = Physics.StillBall(4,sBall4Pos)
            sBall5Pos = Physics.Coordinate(676, 578)
            stillBall5 = Physics.StillBall(5,sBall5Pos)
            sBall6Pos = Physics.Coordinate(780, 574)
            stillBall6 = Physics.StillBall(6,sBall6Pos)
            sBall7Pos = Physics.Coordinate(550, 525)
            stillBall7 = Physics.StillBall(7,sBall7Pos)
            sBall8Pos = Physics.Coordinate(630, 512)
            stillBall8 = Physics.StillBall(8,sBall8Pos)
            sBall9Pos = Physics.Coordinate(710, 499)
            stillBall9 = Physics.StillBall(9,sBall9Pos)
            sBall10Pos = Physics.Coordinate(800, 512)
            stillBall10 = Physics.StillBall(10,sBall10Pos)
            sBall11Pos = Physics.Coordinate(500, 445)
            stillBall11 = Physics.StillBall(11,sBall11Pos)
            sBall12Pos = Physics.Coordinate(590, 420)
            stillBall12 = Physics.StillBall(12,sBall12Pos)
            sBall13Pos = Physics.Coordinate(675, 410)
            stillBall13 = Physics.StillBall(13,sBall13Pos)
            sBall14Pos = Physics.Coordinate(775, 425)
            stillBall14 = Physics.StillBall(14,sBall14Pos)
            sBall15Pos = Physics.Coordinate(845, 450)
            stillBall15 = Physics.StillBall(15,sBall15Pos)
            sBall0Pos = Physics.Coordinate(676, 2025)
            stillBall0 = Physics.StillBall(0, sBall0Pos)

            table = Physics.Table()
            table += stillBall0
            table += stillBall1
            table += stillBall2
            table += stillBall3
            table += stillBall4
            table += stillBall5
            table += stillBall6
            table += stillBall7
            table += stillBall8
            table += stillBall9
            table += stillBall10
            table += stillBall11
            table += stillBall12
            table += stillBall13
            table += stillBall14
            table += stillBall15

            velocityX = form.getvalue('velocityX')
            velocityX = float(velocityX)
            velocityY = form.getvalue('velocityY')
            velocityY = float(velocityY)

            # get player and game info
            gameName = form.getvalue('gameName')
            playerOne = form.getvalue('playerOne')
            playerTwo = form.getvalue('playerTwo')

            counter = form.getvalue('counter')

            velX = float(velocityX)
            velY = float(velocityY)
            print("Game Name is ", gameName)
            print("Player 1 name is ", playerOne)
            print("Player 2 name is ", playerTwo)
            gamePath = float(counter)

            checkGame = 0
            game = 0
            numFrames = 0
            htmlString = ""


            if gamePath == -1:
                htmlString = """<html><head><title>Displaying The Winner!</title><head>\n"""
                htmlString += "<h1>No Winner has been decided yet!</h1>\n"
                htmlString += '<a href="/webpage.html" style="display: none;">Continue Playing</a>\n';
            elif checkGame == 0:
                checkGame = 1
                game = Physics.Game( gameName=gameName, player1Name=playerOne, player2Name=playerTwo, table=table)
                numFrames = game.shoot(gameName, playerOne, table, velX, velY ) 
                print("Shot Complete! Go check Animation.", numFrames)

                for i in range(0, numFrames):
                    with open(f"table-{i}.svg", "w") as fp:
                        table = game.gameRead(table, i)
                        fp.write(table.svg())

                htmlString = "<!DOCTYPE html>\n"
                htmlString += '<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>SVG Animation</title>\n'
                htmlString += '<style>img {max-width: 20%;height: auto;}</style>\n'
                htmlString += '<style>\n';
                htmlString += 'img {max-width: 20%; height: auto;}\n';  # CSS for img tag
                htmlString += 'body {  padding: 0; margin: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; background-color: rgba(210, 192, 250); }\n';  # Additional CSS for body tag
                htmlString += '#lineLength{text-align: center;}\n';
                htmlString += '#cursorPos{ text-align: center;}\n';
                htmlString += 'h1 { margin-top: 20px; font-size: 150px; color: rgba(116, 12, 135); text-align: center;}\n';
                htmlString += '.title-container { margin-top: 20px;}\n';
                htmlString += '.container { margin-top: 100px; margin-left: auto; margin-right: 200px; z-index: 1;}\n';
                htmlString += '#svgContainer { position: absolute; top: 400px;left: 500px;}\n';
                htmlString += 'table {border-collapse: collapse; margin: 25px 0; font-size: 0.9em; font-family: sans-serif; min-width: 400px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); width: 650px; height: 350px; margin-top: 350px; margin-right: 150px;}\n';
                htmlString += 'th, td {background-color: rgba(125, 33, 237); color: #ffffff; text-align: left; padding: 12px 15px; font-size: 30px;}\n';
                htmlString += 'input[type="text"] { width: calc(100% - 60px); padding: 6px; border: 1px solid #ddd; border-radius: 4px; font-size: 90;}\n';
                htmlString += '#shootButton {background-color: #717171; color: rgb(255, 255, 255); padding: 20px 40px; border: none; border-radius: 50%; cursor: pointer; font-size: 24px; margin-top: 20px; margin-left: 250px;}\n';
                htmlString += '#shootButton:hover {background-color: #9d00ffb9;}\n';
                htmlString += '#winnerButton { display: none;}\n';
                htmlString += '#lineLength, #cursorPos { display: none;}\n';
                htmlString += '</style>\n';
                htmlString += '</head><body><button style="background-color: #717171; color: rgb(255, 255, 255); padding: 20px 40px; border: none; border-radius: 50%; cursor: pointer; font-size: 24px; margin-top: 20px; margin-left: 250px;" onclick="startAnimation()">Animate Shot</button>\n'
                htmlString += '<div id="imageContainer" style="width: 100%; height: 100%; position: relative; top: 160px; left: 873px;"></div>\n';
                htmlString += '<a href="winnerResult.html" style="color: #7200d5; font-weight: bold; text-decoration: none; margin-top: 0px; margin-left: 1000px; font-size: 30px; position: relative; z-index: 9999;">See The Winner</a>\n';
                htmlString += '<script>\nvar images = [\n'
                i = 0
                while os.path.exists(f"table-{i}.svg"):
                    if os.path.exists(f"table-{i+1}.svg"):
                        htmlString += f"'table-{i}.svg', "
                    else:
                        htmlString += f"'table-{i}.svg'\n"
                    i += 1

                htmlString += '];\n var currentIndex = 0;\nvar intervalId;\nvar loadedImages = [];\n'
                htmlString += 'function preloadImages() {\nfor (var i = 0; i < images.length; i++) {\nvar img = new Image();\nimg.src = images[i];\nloadedImages.push(img);\n}\n}\n'
                htmlString += 'function startAnimation() {\ncurrentIndex = 0;\nshowImage();\nintervalId = setInterval(nextImage, 40);\n}\n'
                htmlString += 'function stopAnimation() {\nclearInterval(intervalId); // Stop the animation\n}\n'
                htmlString += 'function nextImage() {\ncurrentIndex = (currentIndex + 1) % images.length; // Move to the next image, looping back to the beginning if necessary\nshowImage();\n}\n'
                htmlString += "function showImage() {\nvar imageContainer = document.getElementById('imageContainer');\nimageContainer.innerHTML = ''; // Clear previous image(s)\nvar img = loadedImages[currentIndex];\nimageContainer.appendChild(img)\n;}\n"
                htmlString += "window.onload = preloadImages;\n</script>\n</body>\n</html>\n"


                file_path = "animate.html" 
                
            else:
                numFrames = game.shoot(gameName, playerOne, table, velX, velY ) 
                print("NumFrames:", numFrames)

            file_path = "animate.html"

            with open(file_path, "w") as file:
                file.write(htmlString)
        
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(htmlString, "utf-8"))

        else:
            self.send_response( 404 );
            self.end_headers();
            self.wfile.write( bytes( "404: %s not found" % self.path, "utf-8" ) );

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', int(sys.argv[1])), MyHandler);
    print("Server listing in port:  ", int(sys.argv[1]));
    httpd.serve_forever();
