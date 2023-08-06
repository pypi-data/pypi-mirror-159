# Python Console Configuration

Python Console Configuration is a Python library for customization the output of terminal by color, style and highlight.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python Console Configuration.

```bash
pip install pythonConsoleConfig
```

## Usage

```python
from Font import Color, Style, Highlight

# prints magenta
print(f'{Color.MAGENTA}{"This is a test of Python Console Configuration Library"}')

# prints blink
print(f'{Style.BLINK}{"This is a test of Python Console Configuration Library"}')

# prints highlight blue
print(f'{Highlight.BLUE}{"This is a test of Python Console Configuration Library"}')

# Reset all configuration
Style().reset()

# And so many others ...
```

## Available Configurations
* Colors, Highlights (+ LIGHT)
  * BLACK 
  * RED 
  * GREEN 
  * YELLOW 
  * BLUE 
  * MAGENTA 
  * CYAN 
  * WHITE 
  * GREY
* Styles
  * BOLD 
  * ITALIC 
  * URL 
  * BLINK 
  * BLINK2 
  * SELECTED


## License
[Apache License 2.0](http://www.apache.org/licenses/)