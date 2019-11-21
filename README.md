# THE NationStates Scraper
A scraper for [NationStates](http://nationstates.net) using the NationStates Official API.

## Documentation

### List of Arguments

you can get to this using the argument -h or --help

```
-nation [NATION NAME] | Define the nation to scrape from
-category "[CATEGORIES]" | Categories to get.
-password [PASSWORD FOR NATION] | Password to get private information. (Doesnt do anything, that will be in the next release)
-saveToFile [File to save to] | File to save to. No spaces in the file name.
--listCategories [True / False] | If true, will list categories then terminate. Use alone. If used, other args wont matter.
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
python3 nscraperargs-1-0.exe -nation Entitize -category animal
```

Returns:
(in nsdownload.html)
```xml
<NATION id="entitize">
  <ANIMAL>Entity</ANIMAL>
</NATION>
```

Example 2:
```bash
python3 nscraperargs-1-0.pyc -nation Entitize -category capital
```

Returns:
(in nsdownload.html)
```xml
<NATION id="entitize">
  <CAPITAL>Bark Forest Preserve</CAPITAL>
</NATION>
```
