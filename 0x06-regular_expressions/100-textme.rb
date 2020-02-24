#!/usr/bin/env ruby

from = ARGV[0].scan(/\[(from.*?)\]/).join
to = ARGV[0].scan(/\[(to.*?)\]/).join
flags = ARGV[0].scan(/\[(flags.*?)\]/).join

arr = [from.scan(/(?<=:).*$/), to.scan(/(?<=:).*$/), flags.scan(/(?<=:).*/)]

puts arr.join(",")
