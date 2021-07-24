
# suffuse_log

![Screenshot 2021-07-23 113324](https://user-images.githubusercontent.com/84053244/126813501-a5f428b8-cc96-4c75-9d8b-9735f30f583a.png)

### Overview
suffuse_log is a python library that specializes in ansi-formatting of log messages. It targets 
local scripts that want to output colored logs to a command line terminal. 

However, If you have CLI's that you want to make more engaging, pretty, or additionally communicate their meaning with color,
then this is the library for you. 

### Install

`pip install suffuse_log`

### Getting Started

```
from suffuse_log import suffuse_formatter

logger = suffuse_formatter.defaultConfig(log_level_no=10)

x.info('this is my message')
```


### Features

- Individually color logging attributes!
- Conditionally color multiple logging attributes based on glob patterns or user-defined callables
- Defaults to the popular colorama ansi library
- Allows users to supply their own ansi-style dictionary

### Details

This line in the defaultConfig function:
```
    format_ansi["%(levelname)s"] = AnsiConfig(
        {
            "DEBUG": ("green_fore", "dim_style"),
            "INFO": ("blue_fore",),
            "WARNING": ("yellow_fore",),
            "ERROR": (bright, "red_fore"),
            "CRITICAL": (bright, "red_fore"),
        },
        ("levelname", "message", "name", "module", "lineno"),
    )
```
tells us how to color the listed attributes when the levelname is one of the dictionary keys.


Additionally, this line:

```
    format_ansi["%(message)s"] = AnsiConfig(
        {
            "*error*": (bright,),
            "*important*": (bright,),
            "*critical*": (bright,),
            "*warn*": (bright,),
            "*alert*": (bright,),
        },
        case_sensitive_glob=False,
    )
```

says that when the listed glob patterns are matched, then additionally make the message bright.

**Together this functionality gives us some powerful abilities in how we conditionally color and style our messages.**