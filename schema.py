import graphene

import asylum.schema
import homepage.schema
import photos.schema
import recipes.schema


class Query(
    asylum.schema.Query,
    photos.schema.Query,
    homepage.schema.Query,
    recipes.schema.Query,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query)
