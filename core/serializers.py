from .models import Single, Contributor, SingleViewContributors
from rest_framework import serializers


class SingleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Single
        fields = ['iswc', 'title']


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'contributor']


class ContributorLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SingleViewContributors
        fields = ['iswc', 'contributor_id']


class SingleViewSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='core:single-detail', read_only=True)
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Single
        fields = ['url', 'iswc', 'title', 'contributors']


class SV_API_Serializer(serializers.HyperlinkedModelSerializer):
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Single
        fields = ['iswc', 'title', 'contributors']
