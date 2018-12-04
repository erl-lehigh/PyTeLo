# Signal Temporal Logic

Setup
-----

```bash
git clone git@github.com:wasserfeder/python-stl.git
mkdir -p python-stl/lib
cd python-stl/lib
wget 'https://www.antlr.org/download/antlr-4.7.1-complete.jar'
pip install antlr4-python2-runtime==4.7.1
pip install scipy
```

For permanent settings use:

```bash
cd <clone-dir>
echo "export CLASSPATH=\".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH\"" >> ~/.bashrc
echo "alias antlr4=\"java -jar $PWD/lib/antlr-4.7.1-complete.jar -visitor\"" >> ~/.bashrc
echo "alias grun=\"java org.antlr.v4.gui.TestRig\"" >> ~/.bashrc
```

Otherwise

```bash
cd <clone-dir>
export CLASSPATH=".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
alias antlr4="java -jar $PWD/lib/antlr-4.7.1-complete.jar -visitor"'
alias grun="java org.antlr.v4.gui.TestRig"
```

where `<clone-dir>` is the directory where you cloned the `python-stl` repository.

Install *Gurobi* with *gurobipy* for python2, and optionally for python3.


Run
---

```bash
cd <clone-dir>
antlr4 -Dlanguage=Python2 stl.g4
```

**NOTE:** At the moment the implementation only supports python2. However, you
can generate lexers, parsers, listners, and visitors for other target languages,
such as Java (default), C++, Python3, C#, Go, JavaScript, and Swift.
See http://www.antlr.org/download.html for more details.
