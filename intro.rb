# https://try.ruby-lang.org/

"Jimmy".reverse
40.to_s.reverse

ticket = [20, 12, 56]

ticket.sort!

puts ticket[0]
puts ticket[1]
puts ticket[2]


poems = "My toast has flown from my hand
And my toast has gone to the moon.
But when I saw it on television,
Planting our flag on Halley's comet,
More still did I want to eat it.


Does it rhyme?
"

puts poems

poem.gsub("toast", "honeydew")

poem.reverse

poem.lines.reverse

puts poem.lines.reverse.join


ratings = Hash.new {0}

books.values.each { |rate|
  ratings[rate] += 1
}

puts ratings

5.times { print "Odelay! " }

5.times { |time|
  puts time
}
