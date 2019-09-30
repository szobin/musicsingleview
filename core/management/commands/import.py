from django.core.management.base import BaseCommand
import pandas as pd
from core.tools import exec_import


class Command(BaseCommand):
    help = 'Import musical records in csv format'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Name of the file that will be imported')
        parser.add_argument('-vb', type=int, help='Report level', default=0)

    def handle(self, *args, **kwargs):
        fn = kwargs.get("filename")
        if fn is None:
            self.stdout.write(self.style.WARNING("Define filename argument for import"))
        v = kwargs.get("vb")

        self.stdout.write("Import was started from file {}".format(fn))
        try:
            df = pd.read_csv(fn).fillna("")
        except Exception as exc:
            msg = "- raise error during read csv file {}: {}".format(fn, repr(exc))
            self.stdout.write(msg)
            return

        try:
            exec_import(df, self.stdout, v)
            self.stdout.write("Import was finished OK")
        except Exception as exc:
            msg = "- raise error write to database: {}".format(repr(exc))
            self.stdout.write(msg)
            return
        return
