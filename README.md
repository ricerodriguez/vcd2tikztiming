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

This repo is a fork of the [vcd2tikztiming.py](https://github.com/ernstblecha/vcd2tikztiming "See their repository here."). This script converts a [Value Change Dump (VCD)](https://en.wikipedia.org/wiki/Value_change_dump "Read more about VCD here.") file into a timing diagram using the [tikz-timing](https://ctan.org/pkg/tikz-timing?lang=en "Package description here.") package for LaTeX. This fork was created to provide more precautionary programming through error handling and to change the interface to be more user friendly by requiring less management and providing more documentation. It also cleans up after it's finished and removes the unnecessary files it generated in the intermediary process.

## Installation

This script uses [Python 3](https://www.python.org/downloads/ "Download the latest version of Python here."), so be sure you have the latest Python version installed on your computer. You'll also need to install the following other packages:

* **Verilog_VCD** is used to parse the VCD file so it can be converted to the tikz-timing notation. While a copy of the script is included in this repository, you will still need to install it for the script to work.
        
        pip install Verilog_VCD
        
    or, if it gives you permission denied errors:
    
        sudo pip install Verilog_VCD
        
* **latexpand** is a Perl script used to expand the `\input` commands that are generated in the intermediary steps of this script. This allows the script to dump the contents of the temporary files generated into the final LaTeX file without needing to keep the temporary files. 

    You will need to make sure you have [Perl](https://www.perl.org/ "Official website for Perl") installed on your computer.
  
        perl -v
        
    This should output something like:
    
        This is perl 5, version 28, subversion 2 (v5.28.2) built for x86_64-linux-thread-multi

        Copyright 1987-2019, Larry Wall

        Perl may be copied only under the terms of either the Artistic License or the
        GNU General Public License, which may be found in the Perl 5 source kit.

        Complete documentation for Perl, including FAQ lists, should be found on
        this system using "man perl" or "perldoc perl".  If you have access to the
        Internet, point your browser at http://www.perl.org/, the Perl Home Page.
        
    with your version and build. If it doesn't, [download and install Perl from here](https://www.perl.org/get.html "Download Perl here."). Once that's finished, check your installation with the same `perl -v` command. If you have issues installing Perl, refer to the [Perl](https://www.perl.org/ "Official website for Perl") website for guidance. Once Perl is installed, [download the latexpand script here](https://gitlab.com/latexpand/latexpand "GitLab repository for latexpand"). Put it in a safe location on your computer and [add that location to your PATH](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path "StackExchange answer on how to add to PATH in Linux"). You should be able to do this in any OS, so if you aren't aware how, look up how to do so for your OS.
    
Once you have installed both packages, add the latexpand script and vcd2tikztiming script to your PATH.

Of course, don't forget to mark the scripts as executables with `cd /path/to/script & chmod u+x [script]` for both scripts:

    cd /path/to/latexpand & chmod u+x latexpand

    cd /path/to/vcd2tikztiming & chmod u+x vcd2tikztiming


You should then be able to call it from any location.

## Usage

Navigate to a directory with the VCD file you want to convert to a tikz-timing diagram.

    cd /path/to/vcd/

Then call the script on the file you want to convert.

    vcd2tikztiming example.vcd

You can also set the start and end times of the diagram.

    vcd2tikztiming example.vcd start=1000 end=1200

And you can also set the scale. If you set the scale, make sure the argument for scale comes before the start/end arguments. Otherwise it will not work properly.

    vcd2tikztiming example.vcd scale=1000 start=1000 end=1200

The script creates a `.dmp` file for every reg/wire that has a change with the tikz-timing notation for it. It then uses latexpand to put the contents of the file into the LaTeX file generated. Afterwards, it cleans up and deletes all of the files that it generated except for the `.tex` file with the tikz-timing table. Compile the LaTeX document however way you wish.


