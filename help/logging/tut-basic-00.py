import logging
import argparse

# %%
def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--loglevel", type=str, help="passing loglevel at the script call")
    parser.add_argument("--filter", type=int, default=None)
    return parser


args = get_parser().parse_args()

# logger = logging.getLogger(__name__)  # "__main__"
logger = logging.getLogger('tut-basic')

# %%
# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
print("args.loglevel: ", args.loglevel)
print("filter: ", args.filter)

numeric_loglevel = getattr(logging, args.loglevel.upper(), None)        # !!!
print("loglevel: ", numeric_loglevel)

if numeric_loglevel is None:
    raise ValueError('Invalid log level: %s' % args.loglevel)

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p',
    # The format of the datefmt argument is the same as supported by time.strftime().
    filename='example.log',
    level=numeric_loglevel,     # notice that logging.DEBUG, ... are numeric values
    # filemode='w',             # this overwrites earlier logs; default is 'a'ppend;  passed to open();
)

# %%
logger.debug('This message should go to the log file')
logger.info('So should this')

from datetime import datetime as dt
logger.info(f'{dt.now()}')      # f-strings work

from module import fun
fun()
fun('qq!')

logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

# %%
