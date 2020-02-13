#! python3

import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)


guess = ''

while guess not in ('heads', 'tails'):
    logging.debug("guess = %s" % guess)
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
logging.debug("guess = %s" % guess)

    
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 0:
    toss = "heads"
else:
    toss = "tails"
    
logging.debug("toss = %s" % toss)


if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug("guess = %s" % guess)
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
