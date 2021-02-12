# 2020 FORCE Machine Learning competition: Lithology prediction
The purpose of this competition was first to release high quality well log data for use in research, and second to gather models that predict lithology based on well log measurements. It ran from August to October 2020.


# Context
All rocks have defining properties that can be measured with, in the case of subsurface rocks, sophisticated apparatuses. When a well is drilled these measurements are collected, but the corresponding type of rock or lithology is not known.  These data are evaluated by geologists and petrophysicists to assign a rock type (a.k.a. lithology class) to a set of measurements based on physical models and experience.

The lithology classification process is laborious and not scalable. It can take 2-3 days for an experienced petrophysicists to evaluate a single well depending on the quantity and quality of the available data. In addition, most of the time the evaluation process is carried on a well by well or one well at a time basis, which forfeits the use of the spatial information in the analysis.

As a result, there is an increased need to perform this process in an automated fashion, to assist in the lithology classification when done by hand, by building a starting best guess, and to process volumes of wells at once, e.g., on basin-scale studies with hundreds or thousands of wells.


# Environmnet set up
I'm using conda for managing packages and environments. Once you have [cloned this repo](https://github.com/RafaelPinto/force_2020_lith.git) you'll need to create a conda environment with:

`conda create --name lith_pred -c conda-forge python=3.8 invoke`

where lith_pred is the name of the newly created environment. Then, you must activate it with:

`conda activate lith_pred`

With the environment activated, you will be able to run the `invoke` commands present in the [task.py file](tasks.py). First, run `invoke env-update` to install the rest of the dependencies. Next, I recommend running `invoke env-set-jupyter` to enable jupyter notebook extensions. The other `env_` tasks are for when you install new packages. The suggested steps for intalling or removing packages are:

1. Add your package to the [environment.yml file](environment.yml). 
2. `invoke env-update`: Updates the `hcad_pred` environment with the packages in the environment.yml file.
3. `invoke env-freeze`: Updates the environment_to_freeze.yml file. This file contains all of the environment dependencies.
4. [Optional] `invoke env-remove`: If you need to start from scratch. This will remove the `hcad_env`.


# Downloading the data
`invoke download-data`

> **_NOTE:_**  Although the actual function name is `download_data`, to run in the terminal, we must replace the underscore (`_`) with a dash (`-`). This applies to all invoke functions.

This command will run script `src/data/download_lith_data.py`, which will fecth the competition CSV files available on the [shared Google Drive](https://drive.google.com/drive/folders/1GIkjq4fwgwbiqVQxYwoJnOJWVobZ91pL). It will also download the wells meta data (coordinates, KB, WB...) for the [Norwegian Petroleum Directorate (NPD)](https://factpages.npd.no/en/wellbore/tableview/exploration/all).


# References
Bormann P., Aursand P., Dilib F., Dischington P., Manral S. 2020. FORCE Machine Learning Competition. https://github.com/bolgebrygg/Force-2020-Machine-Learning-competition