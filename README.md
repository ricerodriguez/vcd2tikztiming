<!-- # vcd2tikztiming -->

<!-- converts ValueChangeDump-Files to tikz-timing-diagrams ( see https://bitbucket.org/martin_scharrer/tikz-timing for the latex-package) -->

<!-- needs: -->
<!--  + python3 -->
<!--  + Verilog_VCD ( see https://pypi.org/project/Verilog_VCD/#files ) -->
<!--  + (optional) latexpand - if you want to use the tex-template (see later!) -->
<!--  + a vcd-file (currently only digital signals will have a chance of working) -->
<!--  + either a copy of vcd2tikztiming.py or a symlink named the same as your vcd-file in the same directory (extension .py) -->
<!--  + (optional) a tex-template (again, same name, same directory, extension .tmp this time) -->
<!--  + run the python file (for the example-directory: python siggen_tb.py) -->

<!-- creates: -->
<!--  + a .dmp-file for every signal (basically a single line of tikz-timing-diagram data) -->
<!--  + if a template was given the signals will be imported into the template (for me using input sadly did not work within tikztiming...) and the output will be saved as a .tex-file -->

<!-- parameters: -->
<!--  + you can set starttime, stoptime and scale-factor from the symlink filename (see example directory) -->
<!--    parameters will not be included in output-filename  -->
<!--    you might want to use additional symlinks and directories in more compliacted cases -->

<!-- example: -->
<!-- ![example time signal](https://github.com/ernstblecha/vcd2tikztiming/raw/master/example/siggen_tb.png) -->
# VCD to Tikz Timing

This repo is a fork of the [vcd2tikztiming.py](https://github.com/ernstblecha/vcd2tikztiming "See their repository here."). This script converts a [Value Change Dump (VCD)](https://en.wikipedia.org/wiki/Value_change_dump "Read more about VCD here.") file into a timing diagram using the [tikz-timing](https://ctan.org/pkg/tikz-timing?lang=en "Package description here.") package for LaTeX. This fork was created to provide more precautionary programming through error handling and to change the interface to be more user friendly by requiring less management and providing more documentation. It also does not require a Perl installation or the `latexpand` script, and provides much more options for the generated TeX file.

## Installation

This script uses [Python 3](https://www.python.org/downloads/ "Download the latest version of Python here."), so be sure you have the latest Python version installed on your computer. You'll also need to install the following package:

* **Verilog_VCD** is used to parse the VCD file so it can be converted to the tikz-timing notation. While a copy of the script is included in this repository, you will still need to install it for the script to work.
        
        pip install Verilog_VCD
        
    or, if it gives you permission denied errors:
    
        sudo pip install Verilog_VCD
        
<!-- Once you have installed both packages, add the latexpand script and vcd2tikztiming script to your PATH. -->
To install the verilog2tikz script, download the repository and add it to your PATH.
Of course, don't forget to mark the script as executables with `cd /path/to/script & chmod u+x [script]` for the script:

    cd /path/to/verilog2tikz & chmod u+x verilog2tikz

You should then be able to call it from any location.

## Usage

<!-- **The following instructions don't apply anymore. Documentation will be updated soon.** -->

Navigate to a directory with the VCD file you want to convert to a tikz-timing diagram.

    cd /path/to/vcd/

Then call the script on the file you want to convert and the name of the output TeX file.

    verilog2tikz example.vcd example.tex
    

The script comes with a useful for help command that describes all of the options you can specify
for the generated TeX output:
    
    verilog2tikz --help
    
    usage: verilog2tikz [-h] [-v [LOG LEVEL]] [-b TIME] [-e TIME] [-s SCALE] [-i]
                    [-a] [--font FONTFAMILY] [--upper] [--prefix]
                    [--settings SETTINGS]
                    vcd_file latex_file

    Converts VCD files to tikz-timing compatible files

    positional arguments:
      vcd_file              vcd file to draw diagram from
      latex_file            tex file to write diagram to

    optional arguments:
      -h, --help            show this help message and exit
      -v [LOG LEVEL], --verbose [LOG LEVEL]
                            outputs logging to console
      -b TIME, --begin TIME
                            beginning time of diagram
      -e TIME, --end TIME   end time of diagram
      -s SCALE, --scale SCALE
                            scale of diagram
      -i, --input_ready     diagram ready to use with the \input LaTeX command,
                            usually inside a figure environment
      -a, --axis            include a timing axis in diagram
      --font FONTFAMILY     specify font family (defaults to no specification if
                            not used)
      --upper               capitalize the letters of hex signals
      --prefix              include the '0x' in hex signals
      --settings SETTINGS   store something to settings for future uses

The `settings` option is not currently implemented but is a planned future addition.
<!-- You can also set the start and end times of the diagram. -->



<!-- And you can also set the scale. If you set the scale, make sure the argument for scale comes before the start/end arguments. Otherwise it will not work properly. -->

<!--     vcd2tikztiming example.vcd scale=1000 start=1000 end=1200 -->

<!-- The script creates a `.dmp` file for every reg/wire that has a change with the tikz-timing notation for it. It then uses latexpand to put the contents of the file into the LaTeX file generated. Afterwards, it cleans up and deletes all of the files that it generated except for the `.tex` file with the tikz-timing table. Compile the LaTeX document however way you wish. -->


