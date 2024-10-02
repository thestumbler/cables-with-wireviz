# Cable Diagram Tool

Based on the `WireViz` project: [https://github.com/formatc1702/WireViz](https://github.com/formatc1702/WireViz)

1. Input files defining the cables are in the `yaml` directory
2. Templates common to all the project's cables are in `common.yml`
3. Pictures are in the `images` directory (mostly showing connectors)
4. Output files go into the `out` directory

Even though this project is just a bash script, it uses the Python tool
WireViz. And also, experiments for further automation on the dev branch
are using some Python tools to parse the KiCad schematic netlist.
Therefore, it is best to run this in a virtual environment:

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt`
```

It may be desirable to bypass bash and make diagrams entirely within
Python. See this issue on GitHub where it seems to be possible.

[https://github.com/wireviz/WireViz/issues/231](https://github.com/wireviz/WireViz/issues/231)

Note the use of `common.yml` file and templates. This saves a lot 
of extra and often duplicate entries in the cables' yaml definition 
files.

## Prepare the Input Files

Generate the WireViz input yaml files for each cable of interest.
Keep them in the `yaml` directory.

## Generate a Cable Drawing

Use the `doit.sh` script as follows, for example W1:

```bash
$ doit.sh w1 [yamldir]
```
The name of the yaml directory can be specified as an optional second
argument, and defaults to `yaml`.

The output will be generated and put into the `out` folder. For example:
```bash
$ ls -l out
total 3016
-rw-r--r--  1 rclott  staff     868 May 26 12:55 w1.bom.tsv
-rw-r--r--  1 rclott  staff   19929 May 26 12:55 w1.gv
-rw-r--r--  1 rclott  staff  782172 May 26 12:55 w1.gv.png
-rw-r--r--  1 rclott  staff   57270 May 26 12:55 w1.gv.svg
-rw-r--r--  1 rclott  staff   64582 May 26 12:55 w1.html
-rw-r--r--  1 rclott  staff  555472 May 26 12:55 w1.png
-rw-r--r--  1 rclott  staff   56569 May 26 12:55 w1.svg
```

Description of the files:

* `w1.bom.tsv` BOM file, tab separated fields
* `w1.gv.png` -- PNG image of cable diagram
* `w1.gv.svg` -- SVG image of cable diagram
* `w1.html` -- HTML of cable diagram (images not linking?)
* `w1.gv` -- intermediate file, ignore
* `w1.png` -- intermediate file, ignore
* `w1.svg` -- intermediate file, ignore

## Generate all Cable Drawings

Use the `doall.sh` script as follows, for example W1:

```bash
$ doall.sh [yamldir]
```

The name of the yaml directory can be specified as an optional second
argument, and defaults to `yaml`. You can generate all of the
example files, for example:

```bash
$ doall.sh examples
```


