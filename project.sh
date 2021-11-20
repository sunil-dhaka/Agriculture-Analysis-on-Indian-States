#!/bin/sh
python data.py

#!/bin/sh
python area.py

#!/bin/sh
python login.py

#!/bin/bash
jupyter nbconvert --to notebook --execute analysis.ipynb

#!/bin/bash
jupyter nbconvert --to notebook --execute state-geo-analysis.ipynb

#!/bin/bash
jupyter nbconvert --to notebook --execute district-geo-analysis.ipynb