def convert_dollar_sign_to_latex_counterpart(latex_code_filepath, saving_path=None):
    """ """

    import re

    match_cond0 = r"(^|[^\$])\$([^\$]+)\$([^\$]|$)"
    rpl0 = r"\1\\(\2\\)\3"

    match_cond1 = r"(^|[^\$])\${2}([^\$]+)\${2}([^\$]|$)"
    rpl1 = r"\1\\[\2\\]\3"

    fp = latex_code_filepath
    if saving_path is None:
        sfp = fp
    else:
        sfp = saving_path

    with open(fp, "r") as fi:
        txc = fi.read()

    txc1 = re.sub(match_cond0, rpl0, txc)
    txc1 = re.sub(match_cond1, rpl1, txc1)

    with open(sfp, "w") as fi:
        fi.write(txc1)

    print(f"saved as {sfp}")
