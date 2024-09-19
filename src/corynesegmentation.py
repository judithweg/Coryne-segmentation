import proginit as pi


def project_entry():
    pi.logger.info("Starting cryneSegementation program!")
    if pi.pargs.input:
        pi.logger.debug("Our input file is: " + pi.pargs.input)
    else:
        pi.logger.warn("No input file given!")
