#!/usr/bin/env ruby
data = ARGV[0].scan(/from:(.[a-zA-Z0-9_]+)|to:(.[a-zA-Z0-9_]+)|flags:([0-9:-]+)/)
array = [data[0].compact, data[1].compact, data[2].compact]
puts array.join(',')
