# -------------------
class ResultFormatter(dict):
    # -------------------
    def __init__(self):
        super().__init__()
        self.actual_tag = None
        self.as_hex = False
        self.format = None

    # TODO use json content in cfg.json to create a default formatter

    # -------------------
    ## required for JSON to handle this class as a dictionary
    def __setattr__(self, key, value):
        self[key] = value

    # -------------------
    ## required for JSON to handle this class as a dictionary
    def __getattr__(self, key):
        return self[key]
