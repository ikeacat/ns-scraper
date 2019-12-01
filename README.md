# THE NationStates Scraper
A scraper for [NationStates](http://nationstates.net) using the NationStates Official API.

## Todo

For next release:
- [X] Switch to requests from urllib
- [X] Enable passworded info
- [ ] (maybe) Enable output to STDOUT
- [ ] Region info???

## Documentation

### List of Arguments

you can get to this using the argument -h or --help

```
usage: nscraperargs.(exe or pyc or py or py3) [-h] [-nation NATION] [-password PASSWORD]
                        [-saveToFile SAVETOFILE] [-category CATEGORY]
                        [-listCategories LISTCATEGORIES]

Process main commands

optional arguments:
  -h, --help            show this help message and exit
  -nation NATION        Define the Nation you would like to scrape from.
  -password PASSWORD    (Optional), Enter the password, if you would like to
                        get something that is private (Ex. Issues), Command
                        Ex: -password "insertpasshere"
  -saveToFile SAVETOFILE
                        (Optional), Save to a specific file. Is not compatible
                        with "--saveOutputToSTDOUT". (EX: -saveToFile
                        "downfile")
  -category CATEGORY    Choose the category, put in double quotes NOT SINGLE
                        QUOTES
  -listCategories LISTCATEGORIES
                        (Optional) List the categories avaliable. use public
                        or private after to view either public or private
                        categories
```

### Execute

Using the Compiled python file.
```bash
python3 nscraperargs-[insert version here].pyc [args here]
```

Using the EXE file in CMD.
```
nscraperargs-[insert version here].exe [args here]
```

### Examples
Example 1:

```bash
python3 nscraperargs-1-0.pyc -nation Entitize -category animal
```

```bash
nscraperargs-1-0.exe -nation Entitize -category animal
```

Returns:
(in nsdownload.xml)
```xml
<NATION id="entitize">
  <ANIMAL>Entity</ANIMAL>
</NATION>
```

Example 2:

if using pyc file:
```bash
python3 nscraperargs-1-0.pyc -nation Entitize -category capital
```

if using exe file:
```bash
nscraperargs-1-0.exe -nation Entitize -category capital
```

Returns:
(in nsdownload.xml)
```xml
<NATION id="entitize">
  <CAPITAL>Bark Forest Preserve</CAPITAL>
</NATION>
```

Example 3: (is version 1.1 because that is minimum version you can define 2 or more categories)
```bash
python3 nscraperargs-1-1.pyc -nation Entitize -category "capital animal"
```

```bash
nscraperargs-1-1.exe -nation Entitize -category "capital animal"
```

Returns:
(in nsdownload.xml)
```xml
<NATION id="entitize">
  <CAPITAL>Bark Forest Preserve</CAPITAL>
  <ANIMAL>Entity</ANIMAL>
</NATION>
```

Example 4: (Only compatible with 1.2 and up)

Using py file:
```bash
python3 nscraperargs-1-2.py -nation Entitize -password "thisisntmyrealpassword" -category "nextissuetime" 
```

Using exe file:
```bash
nscraperargs-1-2.exe -nation Entitize -password "thisisntmyrealpassword" -category "nextissuetime"
```

Returns: (in unix Epoch time) (taken at 2:32 PM CST)
(in nsdownload.xml)
```xml
<NATION id="entitize">
  <NEXTISSUETIME>1575250840</NEXTISSUETIME>
</NATION>
```
