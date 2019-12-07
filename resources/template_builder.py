#!/usr/bin/env python
'''
Description: A resource file to provide the default dictionary
             values in the verilog2tikz Python script for use
             in providing a full template of the TeX file
'''
__author__ = "Victoria (Rice) Rodriguez"
__email__ = "rice.rodriguez@ttu.edu"
__status__ = "Prototype"

import os
from string import Template
# path_to_this = os.path.split(__file__)[0]
preamble = os.path.join(os.path.split(__file__)[0],'template.tex')

class TeXTemplate(Template):
    delimiter='#'

def build_template (args):
    """
    Uses the arguments from the argument parser in verilog2tikz
    to determine the values of the dictionary items
    """
    class_declaration = '\documentclass{article}' if not args['input_ready'] else ''
    package_header = '% In your main document, please include the following packages: \n' if args['input_ready'] else ''
    if (args['axis'] and not args['input_ready']):
        packages='\\usepackage[active,tightpage]{preview}\n\\usepackage{tikz-timing}\n\\usepackage{fp}\n\\usepackage{siunitx}\n'
    elif (args['axis'] and args['input_ready']):
        packages='% \\usepackage{tikz-timing}\n% \\usepackage{fp}\n% \\usepackage{siunitx}\n'
    elif (not args['axis'] and args['input_ready']):
        packages='% \\usepackage{tikz-timing}\n'
    # not args[axis] and not args[input_ready]
    else:
        packages='\\usepackage{tikz-timing}\n'

    extras_header = '% In your main document, uncomment the following code and place it in\nthe preamble of your document:\n' if args['axis'] and args['input_ready'] else ''
    extras = '''\providecommand\timeStart{0}
    \newcommand{\timingaxis}[1][1] {
      \\begin{scope}
        \draw [timing/table/axis] (0,-2*\nrows+1) -- (\twidth,-2*\nrows+1);
        \foreach \n in {0,#1,...,\twidth} {
          \draw [timing/table/axis ticks]
          (\n,-2*\nrows+1+.1) -- +(0,-.2)
          node [below,inner sep=2pt] {\scalebox{.75}{\tiny\FPeval\result{clip(\timeStart+\n)}\num{\result}}};
        }
      \end{scope}
    }
    \tikzset{timing/table/axis/.style={->,>=latex},
      timing/table/axis ticks/.style={},
    }
    ''' if args['axis'] and not args['input_ready'] else '''% \providecommand\timeStart{0}
    % \newcommand{\timingaxis}[1][1] {
    %   \\begin{scope}
    %     \draw [timing/table/axis] (0,-2*\nrows+1) -- (\twidth,-2*\nrows+1);
    %     \foreach \n in {0,#1,...,\twidth} {
    %       \draw [timing/table/axis ticks]
    %       (\n,-2*\nrows+1+.1) -- +(0,-.2)
    %       node [below,inner sep=2pt] {\scalebox{.75}{\tiny\FPeval\result{clip(\timeStart+\n)}\num{\result}}};
    %     }
    %   \end{scope}
    % }
    % \tikzset{timing/table/axis/.style={->,>=latex},
    %   timing/table/axis ticks/.style={},
    % }
    ''' if args['axis'] else ''

    outer_env = 'document' if not args['input_ready'] else 'tikztimingtable'

    # Making the options for the tikz timing table environment
    tikz_options_template = TeXTemplate('[xscale=#{xscale},font=#{font},timing/d/background/.style={fill=white}]\n')
    tikz_options = tikz_options_template.substitute(dict(xscale=1,font=args['font'],begin=args['begin']/args['scale'],end=args['end']/args['scale']))

    # If this is input ready then the outermost environment is tikztimingtable, so use those options
    outer_options = tikz_options if args['input_ready'] else '\n'
    inside_extras_template = TeXTemplate(
        '''
        \\begin{extracode}
          \providecommand\timeStart{0}\renewcommand\timeStart{#{begin}.0}
          \providecommand\timeEnd{0}\renewcommand\timeEnd{#{end}.0}
          \timingaxis[10]\relax
        \end{extracode}
        '''
    )
    
    inner_env = '''\\begin{preview}
      \\begin{tikztimingtable}#{tikz_options}
        #{data}
        #{inside_extras}
      \end{tikztimingtable}
    \end{preview}
    ''' if not args['input_ready'] else '''
    #{data}
    #{inside_extras}
    '''

    inner_env_template = TeXTemplate(inner_env)
    inside_extras = inside_extras_template.substitute(dict(begin=args['begin']/args['scale'],end=args['end']/args['scale'])) if args['axis'] else '\n'
    inner_env = inner_env_template.substitute(dict(data=args['tikz_timing'],inside_extras=inside_extras,tikz_options=tikz_options))
    texfile=None
    d=dict(
        class_declaration=class_declaration,
        package_header=package_header,
        packages=packages,
        extras_header=extras_header,
        extras=extras,
        outer_env=outer_env,
        outer_options=outer_options,
        inner_env=inner_env)
    with open(preamble,'r') as f:
        pre_template = f.read()
        template = TeXTemplate(pre_template)
        texfile = template.substitute(d)

    return texfile
