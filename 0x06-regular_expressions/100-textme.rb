#!/usr/bin/env ruby
puts ARGV[0].scan(/([\d|\w|+][a-zA-Z0-9]+)\]\s\[to:([\d|\w|+]\d\w+)\]\s\[flags:([-:\d]+)/).join(",")
