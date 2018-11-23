from __future__ import print_function
from tmdbwrapper import TV

#popular=TV.popular()

#for number, show in enumerate(popular['results'],start=1):
#    print("{0}. {1} - {2}".format(number, show['name'], show['popularity']))


info = TV.info(TV(1234))
for key in info:
    print("{} - {}".format(key, info[key]))
#    print("{} -> {}".format(key, val))


#API Key: 5eb51ab1040e271fa7b1b5d9ac5cc3ab
