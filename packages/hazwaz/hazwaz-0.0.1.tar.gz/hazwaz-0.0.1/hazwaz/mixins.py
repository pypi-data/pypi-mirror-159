import logging
import os
import subprocess


class ExternalEditorMixin:
    """
    Add facilities to open a file in an external editor to a Command.
    """
    editors = [
        (os.environ.get("EDITOR"), "$EDITOR (set to {editor})"),
        ("sensible-editor", "sensible-editor"),
        ("vi", "vi"),
    ]

    def edit_file_in_external_editor(self, filepath):
        """
        Open filepath in an external editor and wait for it to be closed.

        Return whether opening the file was succesful.
        This tries to cycle through all editors listed in self.editors.
        """
        for editor, e_name in self.editors:
            if editor:
                try:
                    res = subprocess.call([editor, filepath])
                except FileNotFoundError:
                    logging.info('Could not open file {} with {}'.format(
                        filepath, e_name
                    ))
                else:
                    if res == 0:
                        return True
                    else:
                        return False
        return False
