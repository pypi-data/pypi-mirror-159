from . import services


# -------------------
class ResultSummary(dict):
    # -------------------
    def __init__(self):
        super().__init__()
        self.result = 'PASS'
        self.actual = None
        self.actual_type = None
        self.expected = None
        self.expected_type = None
        self.reqids = None
        self.location = None
        self.formatter = None

    # -------------------
    def load(self, j):
        self.result = j['result']
        self.actual = j['actual']
        self.actual_type = j['actual_type']
        self.expected = j['expected']
        self.expected_type = j['expected_type']
        self.reqids = j['reqids']
        self.location = j['location']
        self.formatter = j['formatter']

    # -------------------
    def passed(self):
        self.result = 'PASS'

    # -------------------
    def failed(self):
        self.result = 'FAIL'

    # -------------------
    def set_reqids(self, reqids):
        if reqids is None:
            self.reqids = None
        elif isinstance(reqids, str):
            self.reqids = [reqids]
        elif isinstance(reqids, list):
            self.reqids = reqids

    # -------------------
    ## required for JSON to handle this class as a dictionary
    def __setattr__(self, key, value):
        self[key] = value

    # -------------------
    ## required for JSON to handle this class as a dictionary
    def __getattr__(self, key):
        return self[key]

    # -------------------
    def format_actual(self, val):
        self.actual_type = type(val).__name__
        self.actual = self._format('format_actual', val, self.actual_type)

    # -------------------
    def format_expected(self, val):
        self.expected_type = type(val).__name__
        self.expected = self._format('format_expected', val, self.expected_type)

    # -------------------
    def _format(self, tag, val, original_type):
        if self.formatter is None:
            # no formatter, so just convert to a simple string
            return str(val)

        if self.formatter.format is not None:
            # user gave a format, so format it with their request
            return self.formatter.format % val

        if self.formatter.as_hex:
            return self._format_as_hex(tag, val, original_type)

        services.logger.err(f'{tag}: unknown condition')
        return None

    # -------------------
    def _format_as_hex(self, tag, val, original_type):
        if original_type == 'int':
            return f'0x{val:08X}'

        if original_type == 'bytes' or original_type == 'bytearray':
            msg = ''
            count = 0
            for ch in val:
                count += 1
                if ch == val[-1]:
                    suffix = ''
                elif count == 8:
                    suffix = '\n'
                    count = 0
                else:
                    suffix = ' '
                msg += f'{ch:02X}{suffix}'
            return msg

        services.logger.err(f'{tag}: can not convert value with type {original_type} to hex')
        return None
