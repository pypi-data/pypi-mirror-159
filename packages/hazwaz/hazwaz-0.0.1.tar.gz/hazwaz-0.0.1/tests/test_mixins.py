import unittest

import hazwaz


class testEditorMixin(unittest.TestCase):
    def test_open_with_cat_existing_file(self):
        subcmd = hazwaz.mixins.ExternalEditorMixin()
        subcmd.editors = [("cat", "cat")]
        # TODO: suppress this output in the tests (we can't use
        # contextlib.redirect_stdout because that doesn't redirect the
        # stdout used by subprocess.
        res = subcmd.edit_file_in_external_editor("/bin/fgrep")
        self.assertTrue(res)

    def test_open_with_cat_missing_file(self):
        subcmd = hazwaz.mixins.ExternalEditorMixin()
        subcmd.editors = [("cat", "cat")]
        # TODO: suppress this output in the tests (we can't use
        # contextlib.redirect_stderr because that doesn't redirect the
        # stderr used by subprocess.
        res = subcmd.edit_file_in_external_editor("no_such_file")
        self.assertFalse(res)

    def test_open_with_non_existing_editor(self):
        subcmd = hazwaz.mixins.ExternalEditorMixin()
        subcmd.editors = [("no_such_command", "no_such_command")]
        with self.assertLogs() as cm:
            subcmd.edit_file_in_external_editor("no_such_file")
        self.assertIn(
            "Could not open file no_such_file with no_such_command",
            cm.output[0]
        )


if __name__ == '__main__':
    unittest.main()
