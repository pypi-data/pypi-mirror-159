import argparse
import sys

import pandas as pd

from tedana_regressors import __version__


def _get_parser():
    """
    Parse command line inputs for this function.

    Returns
    -------
    parser.parse_args() : argparse dict

    Notes
    -----
    # Argument parser follow template provided by RalphyZ.
    # https://stackoverflow.com/a/43456577
    """
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group("Required Arguments:")

    # Required arguments
    required.add_argument("-ctab", "--ctab", help="Component table", required=True, dest="ctab")
    required.add_argument("-mix", "--mix", help="Mixing matrix", required=True, dest="mix")
    required.add_argument(
        "-prefix", "--prefix", help="Prefix of output file", required=True, dest="prefix"
    )
    optional.add_argument("-v", "--version", action="version", version=("%(prog)s " + __version__))

    parser._action_groups.append(optional)

    return parser


def tedana_regressors(ctab, mix, prefix):

    # Load component table and mixing matrix into pandas dataframes
    ctab_df = pd.read_csv(ctab, sep="\t", index_col=0)
    mix_df = pd.read_csv(mix, sep="\t", index_col=0)

    # Extract the indices of the components that are "accepted" in ctab_df
    accepted_components = ctab_df[ctab_df["accepted"] == 1].index

    # Create matrix with the columns of the mixing matrix corresponding to the accepted components
    mix_accepted_df = mix_df.loc[:, accepted_components]

    # Save the mixing matrix with the accepted components to a file
    mix_accepted_df.to_csv(prefix + "_accepted.1D", sep=" ", index=False)


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    tedana_regressors(**vars(options))


if __name__ == "__main__":
    _main(sys.argv[1:])
