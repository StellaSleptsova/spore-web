from decimal import Decimal

from .models import Result

def parse(filename):
    try:
        result = {}
        i = 0
        with open("C:\Users\Stella\Documents\SPORE\mainSPORE\spore-web\logs\{0}".format(filename), mode='r') as file:
            for line in file:
                if line != '#[spec][snr][schedule][N][K][R][stddev][fer]':
                    parameters = line.split(' ')
                    try:
                        res = Result(spec=str(parameters[0]),
                                     snr=float(parameters[1]),
                                     schedule=int(parameters[2]),
                                     n=int(parameters[3]),
                                     k=int(parameters[4]),
                                     r=float(parameters[5]),
                                     stddev=float(parameters[6]),
                                     fer=float(parameters[7]))
                        i+=1
                        result.update({i:res})
                    except IndexError:
                        print 'An unexpected format in line'
        return result
    except IOError as e:
        print 'Could not read file {0}, {1}, {2}'.format(filename, e.errno, e.strerror)