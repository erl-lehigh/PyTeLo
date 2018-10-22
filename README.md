# Signal Temporal Logic

Setup
-----

```bash
git clone git@github.com:wasserfeder/python-stl.git
mkdir -p python-stl/lib
cd python-stl/lib
wget 'https://www.antlr.org/download/antlr-4.7.1-complete.jar'
pip install antlr4-python2-runtime==4.7.1
```

For permanent settings use:

```bash
echo "export CLASSPATH=\".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH\"" >> ~/.bashrc
echo "alias antlr4=\"java -jar $PWD/lib/antlr-4.7.1-complete.jar\"" >> ~/.bashrc
echo "alias grun=\"java org.antlr.v4.gui.TestRig\"" >> ~/.bashrc
```

Otherwise

```bash
export CLASSPATH=".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
alias antlr4="java -jar $PWD/lib/antlr-4.7.1-complete.jar"'
alias grun="java org.antlr.v4.gui.TestRig"
```

Install *Gurobi* with *gurobipy*.
