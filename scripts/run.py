import argparse
from ParseData import read_all_files, read_single_file
from DataAnalysis import plot_graph_xy, body_position_side
import json
import os

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a','--parse_all_file', 
        type=bool, 
        default=False,
        help='Parse all the files in folder'
    )
    
    parser.add_argument(
        'input_path', 
        type=str, 
        help='The input file or folder'
    )

    # parser.add_argument(
    #     'output_path', 
    #     type=str, 
    #     help='The output file to save results.'
    # )
    args = parser.parse_args()

    if args.parse_all_file:
        parsed_files = read_all_files(args.input_path)
    else:
        parsed_files = read_single_file(args.input_path)
        position_side = body_position_side(parsed_files)
        plot_graph_xy(position_side,parsed_files.file_name,"frame id", "body position")
        # plot_body_length_graph(parsed_files)


        

if __name__ == "__main__":
    main()