
```{python}

library(reticulate)
use_python("C:/Users/zawe1/AppData/Local/Continuum/anaconda3/pkgs/python-3.6.9-h5500b2f_0/python")
use_virtualenv("env")

py_run_file("ReadData.py")
py$df

```