# pyrosetta_ghost

Sometimes movers in Rosetta move to new namespaces. Use this repository to know where they went! By examining the source code, you will be able to track down movers without needing to use slack!

This package should never be installed. 

Never type:  
```bash
git clone https://github.com/bcov77/pyrosetta_ghost.git  
pip install pyrosetta_ghost  
```

And then at the top of your old pyrosetta scripts that don't work anymore, never type:
```python
import pyrosetta_ghost
```
Even though performing these actions will seemlessly put the movers back to the namespaces where they used to live, this is wrong. Use this repository only to manually fix your old scripts by comparing source code after each "AttributeError: 'module' object has no attribute 'X'"
