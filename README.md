# Course kit

The plumbing shared by every notebook in the AI Agents course, so each notebook can show only the
idea it teaches.

- `course_kit/__init__.py`: connect to the model, the model names, and a few small helpers such as `ask()`.
- `course_kit/fintech/`, `healthcare/`, `recruiting/`: one made-up company each. `company.py` holds its rules,
  data and tools; `moduleN.py` holds the practice material one module uses. All people and numbers are invented.

In a notebook:

```python
!pip install -q git+https://github.com/navdeepyadav19/ai-agents-course-kit
from course_kit import *            # connect(), ask(), MODEL, ...
from course_kit.fintech import *            # Acme Software: rules, data and tools
from course_kit.fintech.module2 import *    # the practice material Module 2 uses
```

Nothing here is hidden: every function was written out in full in the module that first taught it.
To read one in Colab, type its name followed by two question marks, for example `ask??`.
