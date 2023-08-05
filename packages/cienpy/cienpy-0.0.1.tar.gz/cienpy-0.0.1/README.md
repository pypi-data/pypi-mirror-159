# cienpy

The name cienpy stands for CIvil ENgineering PYthon and the package contains supporting tools for the computation of parameters and the management of interactive widgets and glyph from the library Bokeh.
At the moment, the package is focused on Structural Mechanics beacause it supports Jupyter Notebooks with interactive tools, but in the future it could be enriched with more Civil Engineering analysis and theories.

- [MIT License](https://choosealicense.com/licenses/mit/)
- [RESSLab](https://github.com/AlbanoCastroSousa/RESSPyLab)
- [Author Github Page](https://github.com/DonCammne)
- Author: Carmine Schipani


## Requirements

- [Bokeh>=2.4.2](https://pypi.org/project/bokeh/2.4.2/) (safer with version 2.4.2)
- [numpy](https://pypi.org/project/numpy/)

## Features

### Structural Mechanics
- Static system: simply supported beam
- Cross section: filled and hollow rectangular section
- Free-body diagram (FBD) with state machine
- NVM diagrams
- Deflection (only due to bending)
- Elastic and plastic analysis
- Stress and strain analysis
- Stress state element and stresses
- Torsion (uniform)
- Mohr Circle
- Buckling

### Interactive Tools (Bokeh)
- Nested-string structure and explicit function implementation for easy and quick management of Javascript codes in Python 
- Curved and double arrows
- Linspace and parabola Javascript functions
- Roller and pinned boundary condition (draws)
- Supporting tools for quick definition and modification of various glyph and widgets

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cienpy using the following prompt command.

```bash
pip install cienpy
```

## Usage

The package is normally imported with this lines:

```python
# import the desired static system
from cienpy import simplebeam as static_sys
# import the desired cross-section
from cienpy import rectangular_section as beam_section
# import supporting modules for the visualisation implementation
from cienpy import models
from cienpy import javascriptcodes as js
```

A dictionary should be created with a specific format of arrays with one entry each and keynames that depend on the functions needed. This dictionary will be used as the main source (ColumnDataSource) for the manipulation of variables bewtween widgets and glyphs in the Javascript codes.

The figures, widgets and glyphs should be initialised. 

The Javascript logics for different widgets and events should be declared.

Finally the layout is declared and executed.

Note that the functions have exhaustive description to help the user.


## Examples

Applications of the library are available in the NOTO EPFL server under the DRIL project for Structural Mechanics or in the [RESSLab](https://github.com/AlbanoCastroSousa/RESSPyLab) Github page.

## Library Status

The library is currently finished for its intended use (support for Structural Mechanics interactive tools). Future implementations are possible to extend the usage and the power of the package. 
