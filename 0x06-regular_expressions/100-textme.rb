#!/usr/bin/env ruby
sender = ARGV[0].scan(/from:([a-zA-Z0-9_]+)/).join
reciber = ARGV[0].scan(/to:([a-zA-Z0-9_]+)/).join
flags = ARGV[0].scan(/flags:(\S[^\]]+)/).join
puts "#{sender}, #{reciber}, #{flags}"
