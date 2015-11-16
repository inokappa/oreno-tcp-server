#!/usr/bin/env python
#-*- coding: utf-8 -*-

import SocketServer
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='log.txt',
    format="%(asctime)s %(levelname)s %(message)s")

class TCPHandler(SocketServer.StreamRequestHandler):
  def handle(self):
    self.data = self.rfile.readline().strip()
    # print self.data
    logging.info('Python TCP Server Test Input:' + self.data.strip())

if __name__ == "__main__":
  HOST, PORT = '127.0.0.1', 18181
  server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
  server.serve_forever()
