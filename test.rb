#!/usr/bin/env ruby

require 'socket'
require 'logger'

log = Logger.new("log.txt")
server = TCPServer.new('0.0.0.0', 18282)
loop do
  Thread.start(server.accept){|s|
    while buffer = s.gets
      # puts buffer
      log.info("Ruby TCP Server Test Input: #{buffer.strip}")
    end
    s.close
  }
end
