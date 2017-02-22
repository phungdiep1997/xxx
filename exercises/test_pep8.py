import subprocess as spr


def test_code_comply_to_pep8_flake8():
    try:
        p = spr.Popen(["flake8", "."], stdout=spr.PIPE, stderr=spr.PIPE)
    except OSError:
        assert False, "flake8 is not installed"
    out, err = p.communicate()
    if err:
        raise Exception("Failed to run flake8")
    if out:
        assert False, ("Code does not comply to "
                       "PEP8 https://www.python.org/dev/peps/pep-0008 \n"
                       + "\n".join(out.splitlines()))
