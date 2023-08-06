import os
import sys
import types

from . import services
from .result_formatter import ResultFormatter
from .result_summary import ResultSummary


# -------------------
class Verifier:
    # -------------------
    ## returns a copy of the default formatter
    def get_formatter(self):
        # TODO return a copy of the default formatter
        return ResultFormatter()

    # -------------------
    def iuv_verify(self, expected, actual, reqid):
        if not services.iuvmode:
            services.logger.err(f'ver.iuv_verify() can only be used in --iuvmode')
            services.harness.abort()

        expected_type = type(expected).__name__
        actual_type = type(actual).__name__

        if expected == actual:
            msg = f'\nIUV Verify: Reqid: "{reqid}"' \
                  f'\n   Expected ({expected_type: <5}): {expected}' \
                  f'\n   Actual   ({actual_type: <5}): {actual}'
            # TODO write to iuv_report file
            services.logger.line(msg)
            return

        # get a full stackframe
        try:
            raise AssertionError
        except AssertionError:
            tb = sys.exc_info()[2]

        # go one caller back
        frame = tb.tb_frame
        frame = frame.f_back

        tb = types.TracebackType(tb_next=None,
                                 tb_frame=frame,
                                 tb_lasti=frame.f_lasti,
                                 tb_lineno=frame.f_lineno)

        msg = f'\nIUV Verify: Reqid: "{reqid}"' \
              f'\n   Expected ({expected_type: <5}): {expected}' \
              f'\n   Actual   ({actual_type: <5}): {actual}'

        raise AssertionError(msg).with_traceback(tb)

    # -------------------
    def verify(self, actual, reqids=None, formatter=None):
        rs, tb = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(True, rs)

        if actual:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs, tb)

    # -------------------
    def verify_equal(self, expected, actual, reqids=None, formatter=None):
        rs, tb = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(expected, rs)

        if actual == expected:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs, tb)

    # TODO add other verifys

    # -------------------
    def _handle_pass(self, rs):
        self._save_result_pass(rs)

    # -------------------
    def _handle_fail(self, rs, tb):
        self._save_result_fail(rs)

        msg = self._format_fail_msg(rs)

        # Throw an assertion so the pyunit stops and shows a stack trace
        # starting from the verify_x() command in the caller
        # TODO should only report, currently aborts current test case
        raise AssertionError(msg).with_traceback(tb)

    # -------------------
    def _save_result_pass(self, rs):
        # override actual value with the tag the user requested
        if rs.formatter is not None and rs.formatter.actual_tag is not None:
            rs.actual = rs.formatter.actual_tag

        rs.passed()
        services.proto.add_result(rs)

    # -------------------
    def _save_result_fail(self, rs):
        rs.failed()
        services.proto.add_result(rs)

    # -------------------
    def _create_result_summary(self, reqids, formatter):
        # get a full stackframe
        try:
            raise AssertionError
        except AssertionError:
            tb = sys.exc_info()[2]

        # go two callers back
        frame = tb.tb_frame
        frame = frame.f_back
        frame = frame.f_back

        tb = types.TracebackType(tb_next=None,
                                 tb_frame=frame,
                                 tb_lasti=frame.f_lasti,
                                 tb_lineno=frame.f_lineno)

        # uncomment to debug
        # print(f"\nDBG: {frame.f_code.co_name}")
        # print(f"DBG: {frame.f_code.co_filename}")
        # print(f"DBG: {frame.f_lineno}")

        fname = os.path.basename(frame.f_code.co_filename)
        location = f'{fname}({frame.f_lineno})'

        # create a results summary and pre-populate it
        rs = ResultSummary()
        rs.location = location
        rs.set_reqids(reqids)
        rs.formatter = formatter

        return rs, tb

    # -------------------
    def _set_actual(self, actual, rs):
        rs.format_actual(actual)

    # -------------------
    def _set_expected(self, expected, rs):
        rs.format_expected(expected)

    # -------------------
    def _format_fail_msg(self, rs):
        msg = f'\n   Expected ({rs.expected_type: <5}): {rs.expected}' \
              f'\n   Actual   ({rs.actual_type: <5}): {rs.actual}'

        return msg
