In a nutshell
=============
DCC_generate_stubs generates stubs for different DCC apis.

Supported DCC
=============
For now, only maya.cmds (2017 and 2018) is supported.

How is it possible?
===================
To get stubs, proper api documentation (probably on-line documentation) is parsed.


Usage
=====
Command:

    `dcc_generate_stubs.cmd maya cmds -v 2017 -s short_name -o "./../../stubs/test.pyi" -w`

will generate stubs for Maya 2017 cmds package and write the output into './../../stubs/test.pyi' file with forced 
file override (`-w` flag).


IDE-dependent tips  
==================

PyCharm
-------
PyCharm, by default, has set a file size limitation for file parsing. Files, which are bigger that 2500KB will not be
parsed. To make this limit higher, go to `Help -> Edit Custom Properties...` and put the text below into the properties
file.

```
#---------------------------------------------------------------------
# Maximum file size (kilobytes) IDE should provide code assistance for.
# The larger file is the slower its editor works and higher overall system memory requirements are
# if code assistance is enabled. Remove this property or set to very large number if you need
# code assistance for any files available regardless their size.
#---------------------------------------------------------------------
idea.max.intellisense.filesize=2500
```