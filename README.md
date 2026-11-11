# Course kit

The plumbing shared by every notebook in the AI Agents course, so each notebook can show only the
idea it teaches.

- `course_kit/__init__.py`: connect to the model, the two model names, and a few small helpers.
- `course_kit/fintech.py`, `healthcare.py`, `recruiting.py`: one made-up company each, with its data,
  tools and test messages. All people and numbers are invented.

In a notebook:

```python
!pip install -q git+https://github.com/navdeepyadav19/ai-agents-course-kit
from course_kit import *            # connect(), ask(), MODEL, ...
from course_kit.fintech import *    # Acme Software's data, tools and test messages
```

Nothing here is hidden: every function was written out in full in the module that first taught it.
To read one in Colab, type its name followed by two question marks, for example `ask??`.
