#!/usr/bin/env python
#-*- coding: utf-8 -*-

import SocketServer
import logging

HOST = '127.0.0.1'
PORT = 18181

logging.basicConfig(
    level=logging.INFO,
    filename='log.txt',
    format="%(asctime)s %(levelname)s %(message)s")

class Handler(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            # logging.debug(data)
            if len(data) == 0:
                break
            self.request.send('Python TCP Server Test Input:' + data)
            logging.info('Python TCP Server Test Input:' + data.strip())
        self.request.close()

server = SocketServer.TCPServer((HOST, PORT), Handler)
server.serve_forever()
