'''Doc: solution <problemset 1>

Question : 4c

Author: divya.natarajan@accenture.com

Date:05/12/2017'''



t=6+52/60.0

slowpace=2*((8+(15/60.0))/60.0)

tempo=3*((7+(12/60.0))/60.0)

ttl=(t+slowpace+tempo)

minu=(ttl-int(ttl))*60

print "He reached at %d : %d" % (int(ttl),minu)



