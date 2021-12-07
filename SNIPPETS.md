### enable autoreload in ipython (using deepreload)

```python
%load_ext autoreload
%autoreload 2

import builtins
from IPython.lib import deepreload
builtins.reload = deepreload.reload
```
