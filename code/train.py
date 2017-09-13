import numpy
import os
import sys

from nmt import train

def main(job_id, params):
    print params
    validerr = train(**params)
    return validerr

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print '%s config.py' % sys.argv[0]
        sys.exit(1)

    options = eval(open(sys.argv[-1]).read())
    numpy.random.seed(options['seed'])

    main(0, options)
