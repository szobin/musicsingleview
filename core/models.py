from __future__ import unicode_literals
from django.db import models


class Single(models.Model):
    iswc = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=280, db_index=True)

    class Meta:
        verbose_name = 'List of the single views'
        ordering = ['title']
        get_latest_by = 'title'


class Contributor(models.Model):
    id = models.AutoField(primary_key=True)
    contributor = models.CharField(max_length=280, db_index=True)

    class Meta:
        verbose_name = 'List of the contributors'
        ordering = ['contributor']
        get_latest_by = 'contributor'


class SingleViewContributors(models.Model):
    iswc = models.ForeignKey(Single, related_name='contributors', on_delete=models.CASCADE)
    contributor_id = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    def __str__(self):
        return self.contributor_id.contributor

    class Meta:
        verbose_name = 'Link table btween contributors and singles'
        ordering = ['iswc', 'contributor_id']
        get_latest_by = 'iswc'
        index_together = [
            ("iswc", "contributor_id"),
        ]
