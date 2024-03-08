from neomodel import StructuredNode, StringProperty, ArrayProperty,UniqueIdProperty, RelationshipTo, EmailProperty

#Users 
class User(StructuredNode):
    uid = UniqueIdProperty()
    emailAddr = EmailProperty(unique_index=True, required=True)
    userName = StringProperty(unique_index=True, required=True)
    keyIdAuth = StringProperty(unique_index=True, required=True) 
    idArtist = ArrayProperty(StringProperty())
    idTracks = ArrayProperty(StringProperty())
    idAlbums = ArrayProperty(StringProperty())

    #Relations
    follow = RelationshipTo('User', 'Follow')

    