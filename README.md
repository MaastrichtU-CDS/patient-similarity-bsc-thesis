# Patient Similarity BSc thesis archive

This repository contains the code developed by [Daniël Slob](https://www.linkedin.com/in/daniël-slob-83001a153/) for his BSc thesis on simple patient similarity vs prediction models.

The main code can be found in [Similarity.ipynb](Similarity.ipynb). This uses the model commissioning library code (in the [mcl](mcl) folder) with a small modification to load prediction models locally. This is based on the fairmodels.org work, with an example jupyter notebook to execute a prediction model loaded from the internet (see [example_original_model.ipynb](example_original_model.ipynb)).

## how to run?
1. Download/clone this repository
2. Download/clone the repository [https://github.com/MaastrichtU-CDS/Model-Commissioning-Library.git](https://github.com/MaastrichtU-CDS/Model-Commissioning-Library.git) into the subfolder named "mcl"
3. Execute the [Similarity.ipynb](Similarity.ipynb) notebook