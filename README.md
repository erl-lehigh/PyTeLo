# Python Temporal Logic (PyTeLo)

## Paper description [PDF](https://arxiv.org/pdf/2310.08714)

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

where `<clone-dir>` is the directory where you cloned the `PyTeLo` repository.

Install *Gurobi* with *gurobipy* for python3.


Run
---

```bash
cd <clone-dir>/stl
antlr4 -Dlanguage=Python3 stl.g4
cd <clone-dir>/mtl
antlr4 -Dlanguage=Python3 mtl.g4
```
## How To Cite
Cardona, G.A., Leahy, K., Mann, M. and Vasile, C.I., 2023. A Flexible and Efficient Temporal Logic Tool for Python: PyTeLo. arXiv preprint arXiv:2310.08714.

BibTeX:
```
@article{cardona2023flexible,
  title={A Flexible and Efficient Temporal Logic Tool for Python: PyTeLo},
  author={Cardona, Gustavo A and Leahy, Kevin and Mann, Makai and Vasile, Cristian-Ioan},
  journal={arXiv preprint arXiv:2310.08714},
  year={2023}
}
```

**NOTE:** At the moment the implementation only supports python2 and python3. However, you
can generate lexers, parsers, listners, and visitors for other target languages,
such as Java (default), C++, C#, Go, JavaScript, and Swift.
See http://www.antlr.org/download.html for more details.
