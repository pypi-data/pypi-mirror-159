import sys
import csv
import os.path
import pickle


def show_saved_figure(path):
    """Unpickle and show a pickled matplotlib figure.

    Parameters
    ----------
    path: str | pathlib.Path
        The path where the figure is saved.

    Returns
    -------
    fig: matplotlib.figure.Figure
        The matplotlib figure instance.

    """
    fig = pickle.load(open(path, 'rb'))

    import matplotlib.pyplot as plt
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)

    plt.show()
    return fig


def save_figure(fig, path):
    """Pickle a matplotlib figure.

    Parameters
    ----------
    fig: matplotlib.figure.Figure
        The matplotlib figure instance to be saved.
    path: str | pathlib.Path
        The path where the figure is saved.

    """
    pickle.dump(fig, open(path, 'wb'))


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


class CsvLogger:
    """Logger that only open file for writing. Use pandas.read_csv to read csv files"""
    def __init__(self, filename: str, fieldnames: list, dialect='excel-tab', append=False):
        self.dialect = csv.get_dialect(dialect)
        self.filename = os.path.abspath(filename)
        self.fieldnames = fieldnames

        if os.path.exists(filename):
            if not append:
                raise FileExistsError

            # validate file has the correct header
            with open(filename, 'r') as file:
                reader = csv.DictReader(file, dialect=dialect)

                if reader.fieldnames != fieldnames:
                    raise RuntimeError("Existing file has differing fieldnames", reader.fieldnames, fieldnames)

        else:
            with open(self.filename, 'x') as file:
                csv.DictWriter(file, fieldnames=self.fieldnames, dialect=self.dialect).writeheader()

    def write(self, *args):
        with open(self.filename, 'a+') as file:
            csv.DictWriter(file, fieldnames=self.fieldnames, dialect=self.dialect).writerow(dict(zip(self.fieldnames, args)))
