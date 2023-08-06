#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""For information of MolDrug:
    Docs: https://moldrug.readthedocs.io/en/latest/
    Source Code: https://github.com/ale94mleon/moldrug
"""
from moldrug._version import __version__, __version_tuple__
import yaml, argparse, os, inspect, importlib

def run():
    from moldrug import utils

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        help='The configuration yaml file',
        dest='yaml_file',
        type=str)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-f', '--fitness',
                        help="The path to the user-custom fitness module; inside of which the given custom cost function must be implemented. "\
                            "See the docs for how to do it properly. E.g. my/awesome/fitness_module.py."\
                            "By default will look in the moldrug.fitness module.",
                        dest='fitness',
                        default=None,
                        type=str)
    args = parser.parse_args()
    
    with open(args.yaml_file, 'r') as c:
        Config = yaml.safe_load(c)
    if args.fitness:
        spec=importlib.util.spec_from_file_location('fitness', args.fitness)
        fitness = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fitness)
        Cost = dict(inspect.getmembers(fitness))[Config['costfunc']]
    else:
        from moldrug import fitness
        Cost = dict(inspect.getmembers(fitness))[Config['costfunc']]
    
    if Config['type'].lower() == 'ga':
        TypeOfRun = utils.GA
    elif Config['type'].lower() == 'local':
        TypeOfRun = utils.Local
    else:
        raise RuntimeError(f"\"{Config['type']}\" it is not a possible type. Select from: GA or Local")
    InitArgs = Config.copy()

    # Modifying InitArgs
    [InitArgs.pop(key, None) for key in ['type', 'njobs']]
    InitArgs['costfunc'] = Cost
    
    # Initialize the class
    Results = TypeOfRun(**InitArgs)
    # Call the class
    Results(Config['njobs'])
    # Save final data
    Results.pickle(f"{InitArgs['deffnm']}_result", compress=True)
    # Saving final sdf file
    utils.make_sdf(Results.pop, sdf = f"{InitArgs['deffnm']}_pop.sdf")
    print(Results.to_dataframe())
 