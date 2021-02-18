## Simple Python Interpreter for bash
This package enable you to run bash commands and scripts from Python.

#### Installation
```bash
	python3 -m pip install sbash
```

#### Usage
* Import Bash `class` from `sbash.core` as follow:
```bash
	from sbash import Bash
```
`Bash` class have a static method `exec` that allow you to execute bash commands (in `string` or list of `strings` form).
```bash
	Bash.exec(BASH_CMD, where=WHERE_RUN_BASH_CMD, quiet=TRUE_FOR_RUN_QUIETLY)
```

In the next examples I show you how to use the syntaxis above.
```bash
	from sbash import Bash
	
	Bash.exec("date")				
    #output: 
    Thu Feb 18 12:50:07 AM -05 2021
	
    Bash.exec("Bash.exec("python --version")	
    #output: 
    Python 3.9.1

	Bash.exec("sensors")
	#output:
    coretemp-isa-0000
    Adapter: ISA adapter
    Package id 0:  +50.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 0:        +44.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:        +50.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 2:        +43.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 3:        +44.0°C  (high = +100.0°C, crit = +100.0°C)

    BAT0-acpi-0
    Adapter: ACPI interface
    in0:          15.56 V  
    curr1:            N/A  

    pch_skylake-virtual-0
    Adapter: Virtual device
    temp1:        +50.5°C  

    acpitz-acpi-0
    Adapter: ACPI interface
    temp1:        +45.0°C  
```
