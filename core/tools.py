from .models import Single, Contributor, SingleViewContributors


class ImportRow:

    def __init__(self, n, row, stdout, verbose=0):
        self.n = n
        self.verbose = verbose
        self.stdout = stdout
        self.iswc = row["iswc"]
        self.title = row["title"]
        self.contributors = row["contributors"].split('|')
        self.contributors_dict = None

    def log(self, msg):
        if self.verbose > 0:
            self.stdout.write(msg)

    def get_contributor_id(self, title, insert_new=False):
        cf = Contributor.objects.filter(contributor=title)
        if len(cf) == 0:
            if not insert_new:
                return -1

            c = Contributor(contributor=title)
            c.save()
            self.log("   contributor ({}:{}) was inserted OK".format(c.pk, title))
            return c.pk
        c = cf[0]
        self.log("   contributor `{}` was found with id: {}".format(title, c.pk))
        return c.pk

    def update_contributors(self):
        self.contributors_dict = {c: self.get_contributor_id(c, True) for c in self.contributors}

    def update_single(self):
        sf = Single.objects.filter(pk=self.iswc)
        if len(sf) > 0:
            self.log("   single ({}: {}) was found.".format(self.iswc, self.title))
            return True

        s = Single(iswc=self.iswc, title=self.title)
        s.save()
        self.log("   single ({}: {}) was stored.".format(self.iswc, self.title))
        return True

    def detect_iswc_by_title(self):
        sf = Single.objects.filter(title=self.title)
        if len(sf) == 0:
            self.iswc = None
            self.log("   iswc was not found by title: {}".format(self.title))
            return False
        s = sf[0]
        self.iswc = s.iswc
        self.log("   iswc `{}` was detected by title: {}".format(self.iswc, self.title))
        return True

    def update_contributor_link(self, c_id, c_title):
        clf = SingleViewContributors.objects.filter(iswc=self.iswc, contributor_id=c_id)
        if len(clf) > 0:
            self.log("   contributor link `{}` already exist".format(c_title))
            return True

        cl = SingleViewContributors(iswc=Single(iswc=self.iswc), contributor_id=Contributor(pk=c_id))
        cl.save()
        self.log("   contributor link `{}` was inserted OK".format(c_title))
        return True

    def update_contributor_links(self):
        for c_title, c_id in self.contributors_dict.items():
            self.update_contributor_link(c_id, c_title)

    def start(self):
        self.log('- import record {}'.format(self.n))
        self.update_contributors()

        if len(self.iswc) < 10:
            self.detect_iswc_by_title()

        if self.iswc is None:
            self.log("   ! iswc was not detected, pending")
            return -1

        self.update_single()
        self.update_contributor_links()
        return 0


def exec_import(df, stdout, verbose):
    pending = list()
    for i, r in df.iterrows():
        ir = ImportRow(i+1, r, stdout, verbose)
        r = ir.start()
        if r < 0:
            pending.append(ir)
    for ir in pending:
        ir.start()
    return True
