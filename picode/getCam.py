import socket
import subprocess
# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket=socket.socket()
server_socket.bind(('0.0.0.0',8004))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection=server_socket.accept()[0].makefile('rb')
try:
    cmdline=['/Applications/VLC.app/Contents/MacOS/VLC','--demux','h264','-']
    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
    player=subprocess.Popen(cmdline, stdin=subprocess.PIPE)
    while True:
        data=connection.read(1024)
        if not data:
            break
        player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    player.terminate()
