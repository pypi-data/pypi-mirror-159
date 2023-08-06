# Regener - Resume Generator

Simple one page generator.

## System requirements:
 - Linux (I'm using Debian 11)
 - Python > 3.6
   - reportlab (3.6.5)


## Installation 

    pip install regener==22.7.17

## Usage

INPUT_PATH: Path to folder with files (json, images, fonts)

OUTPUT_PATH: Path to the pdf file or to directory where that pdf file will be generated

Usage:

    regener -p <INPUT_PATH>
    regener -p /home/${USER}/Desktop/My_CV/

Or:

    regener -p <INPUT_PATH> -o <OUTPUT_PATH>
    regener -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/
    regener -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/My_CV_2022.pdf

## Json file

Script will search for file `cv.json` in INPUT_PATH.

Example of simple CV json file can be found in `examples` directory. 
