__version__ = '1.0.0'

import argparse
import numpy as np
import pandas as pd
from .__main__ import topsis

def readInputFile(input):
    if input.endswith('.csv'):
        df = pd.read_csv(input)
    elif input.endswith('.xlsx') or input.endswith('.xls'):
        df = pd.read_excel(input)
    else:
        raise ValueError('Unsupported file format. Use CSV or XLSX.')
    
    data = df.iloc[:, 1:].values
    alternatives = df.iloc[:, 0].values if df.shape[1] > data.shape[1] else None
    return data, alternatives

def main():
    parser = argparse.ArgumentParser(description = 'Topsis') 
    parser.add_argument('input', help = 'Path to the input CSV file')
    parser.add_argument('weights', help = 'Weights - Comma separated')
    parser.add_argument('impacts', help = 'Impacts(+/-) - Comma Separated')
    parser.add_argument('output', help = 'Path to save the output CSV file')

    args = parser.parse_args()

    try:
        data, alternatives = readInputFile(args.input_file)
    except Exception as e:
        print(f'Error reading input file: {e}')
        return

    weights = np.array(list(map(float, args.weights.split(','))))

    impacts = args.impacts.split(',')

    try:

        score, rank = __main__(data, weights, impacts)

        outputData = np.column_stack((alternatives, data, score, rank)) if alternatives is not None else np.column_stack((data, score, rank))
        columns = ['Alternative'] + [f'Criterion{i+1}' for i in range(data.shape[1])] + ['Score', 'Rank']
        df = pd.DataFrame(outputData, columns=columns)

        if args.output.endswith('.csv'):
            df.to_csv(args.output, index=False)
        elif args.output.endswith('.xlsx'):
            df.to_excel(args.output, index=False)
        print(f'Result saved to {args.output}') 

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()