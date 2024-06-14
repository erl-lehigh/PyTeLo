# Python Temporal Logic (PyTeLo)

Setup
-----

```bash
git clone git@github.com:erl-lehigh/PyTeLo.git pytelo
mkdir -p pytelo/lib
cd pytelo/lib
wget 'https://www.antlr.org/download/antlr-4.13.0-complete.jar'
pip install antlr4-python3-runtime==4.13.0
pip install scipy
```

For permanent settings use:

```bash
cd <clone-dir>
echo "export CLASSPATH=\".:$PWD/lib/antlr-4.13.0-complete.jar:$CLASSPATH\"" >> ~/.bashrc
echo "alias antlr4=\"java -jar $PWD/lib/antlr-4.13.0-complete.jar -visitor\"" >> ~/.bashrc
echo "alias grun=\"java org.antlr.v4.gui.TestRig\"" >> ~/.bashrc
```

Otherwise

```bash
cd <clone-dir>
export CLASSPATH=".:$PWD/lib/antlr-4.13.0-complete.jar:$CLASSPATH"
alias antlr4="java -jar $PWD/lib/antlr-4.13.0-complete.jar -visitor"
alias grun="java org.antlr.v4.gui.TestRig"
```

where `<clone-dir>` is the directory where you cloned the `pytelo` repository.

Install *Gurobi* with *gurobipy* for python3.

Run
---

```bash
cd <clone-dir>/src
antlr4 -Dlanguage=Python3 stl.g4
```

Install as Package
---
After running `antlr4` above, from one directory level above `pytelo/`

```bash
pip install pytelo/
```

This will let other packages import pytelo functions without including pytelo in their directory structure or referencing the associated files by location.


**NOTE:** At the moment the implementation only supports python2 and python3. However, you
can generate lexers, parsers, listners, and visitors for other target languages,
such as Java (default), C++, C#, Go, JavaScript, and Swift.
See http://www.antlr.org/download.html for more details.
