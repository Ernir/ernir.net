import graphene

import homepage.schema
import photos.schema


class Query(photos.schema.Query, homepage.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
