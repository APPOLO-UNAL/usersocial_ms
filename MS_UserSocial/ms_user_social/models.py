from neomodel import StructuredNode, StringProperty, ArrayProperty,UniqueIdProperty, RelationshipTo, EmailProperty

#Users 
class User(StructuredNode):
    uid = UniqueIdProperty()
    emailAddr = EmailProperty(unique_index=True, required=True)
    userName = StringProperty(unique_index=True, required=True)
    keyIdAuth = StringProperty(unique_index=True, required=True) 
    arrArtists = ArrayProperty(StringProperty())
    arrTracks = ArrayProperty(StringProperty())
    arrAlbums = ArrayProperty(StringProperty())

    #Relations
    follow = RelationshipTo('User', 'Follow')

    