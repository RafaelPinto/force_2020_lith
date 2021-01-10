import gdown

from src.definitions import ROOT_DIR


output_root = ROOT_DIR / 'data/external'

if not output_root.is_dir():
    output_root.mkdir(parents=True)

url_root = "https://drive.google.com/uc?id="

file_ids = {
    # "Well log competion rules and description": "1Q_Z7xDREeTGqXvdmFuZ89e6PXN4I1miPLq1I17MTkds",
    "Confusion matrix all submitters.xlsx": "1f4DZPmwJFPG7hScEX_S2RbLdOF4IOH_U",
    "CSV_hidden_test.csv": "1PLWXrUQKmwMchAmcoJos0lmAm9MLEFnW",
    "CSV_test.csv": "17W3I_XfI0JlJ4mLJVtz4rGa0eZKWZ6Xv",
    "CSV_train.csv": "1hwDi05hwICWf95SOlofdKKYZUH79ReOa",
    "lithology scoring matrix cost function.xlsx": "11Hx1KBCy3vMWzzyqdVumZxIP37qi6kEZ",
    "NPD_Casing_depth_most_wells.xlsx": "10HjgB3f1_VpGjTiFPjJs37r6QYLX5T9T",
    "NPD_Lithostratigraphy_groups_all_wells.xlsx": "19oTHTNg5jXsss8sElbXQZtjJrJRaffku",
    "NPD_Lithostratigraphy_member_formations_all_wells.xlsx": "1X57eNXWW0_ilNO_ISvC6uz1o2OsPDZRP",
    "penalty_matrix.npy": "1eCH2LBFywpgopOcHG0RLGXEtBKb7LHhM",
    "starter_notebook.ipynb": "1uYG70pz2hh2nmgo6f3Hdg_IxQmyRGWEb",
    "Well logs abbreviation description.xlsx": "1EOxhQicZC5X-tbPwojvWxsHjst7IcIsy",
}

for file_name, file_id in file_ids.items():
    url = url_root + file_id

    output = output_root / file_name

    gdown.download(url, str(output))
