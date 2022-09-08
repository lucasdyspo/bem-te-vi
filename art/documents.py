from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Art


@registry.register_document
class ArtDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'art'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Art # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'genre',
            'description',
            'tags',
        ]
        
        
# s = ArtDocument.search().filter("term", name="computer")[:30] 
# qs = s.to_queryset() 
# # qs é apenas um queryset django e é chamado com order_by para manter 
# # a mesma ordem como o resultado elasticsearch. 
# for gato in qs: 
#     print (gato.name)