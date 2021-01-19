import pandas as pd

import gdown

from src.definitions import ROOT_DIR


OUTPUT_ROOT = ROOT_DIR / 'data/external'

if not OUTPUT_ROOT.is_dir():
    OUTPUT_ROOT.mkdir(parents=True)


def download_from_google_drive(file_ids, output_root=None, redownload=False):
    """
    Download the seleced files from Google Drive using their Google Drive IDs.

    Parameters
    ----------
    file_ids : dict
        Dictionary with file name with extension as key and file's Google
        drive ID as value.
    output_root: path like
        Directory to store the downloaded data.
    redownload: bool
        Download the file even if it already exists.

    """
    if output_root is None:
        output_root = OUTPUT_ROOT

    url_root = "https://drive.google.com/uc?id="

    for file_name, file_id in file_ids.items():
        output = output_root / file_name

        # Skip file if already downloaded
        if output.exists():
            if not redownload:
                continue

        url = url_root + file_id

        gdown.download(url, str(output))

    return


def download_competition_files():
    """
    Download the competition files from Google Drive using their Google
    Drive IDs.

    """
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
        "olawale_hidden_test_pred.csv": "16w0E1QPIdCDdoJRgAXQzqSPJ5eywQyMl",
    }

    download_from_google_drive(file_ids)

    return


def download_well_meta():
    """
    Download well meta data from Norwegian Petroleum Directorate (NPD).

    """
    well_meta_url = 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/wellbore_exploration_all&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en'

    well_meta = pd.read_csv(well_meta_url)

    well_meta_path = OUTPUT_ROOT / 'well_meta_npd.csv'
    well_meta.to_csv(well_meta_path, index=False)


def download_open_test_labels():
    """
    Download the open test set true labels.

    """
    url = 'https://github.com/bolgebrygg/Force-2020-Machine-Learning-competition/raw/master/lithology_competition/data/leaderboard_test_target.csv'

    test_y_true = pd.read_csv(url, sep=';')

    test_y_true_path = OUTPUT_ROOT / 'open_test_y_true.csv'
    test_y_true.to_csv(test_y_true_path, index=False)


if __name__ == "__main__":
    download_competition_files()

    download_well_meta()

    download_open_test_labels()
