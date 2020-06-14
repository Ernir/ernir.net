import graphene

import homepage.schema
import photos.schema
import asylum.schema


class Query(
    asylum.schema.Query, photos.schema.Query, homepage.schema.Query, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
