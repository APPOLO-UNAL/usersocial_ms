from neomodel import StructuredNode, StringProperty, ArrayProperty,UniqueIdProperty, RelationshipTo, EmailProperty

#Users 
class User(StructuredNode):
    uid = UniqueIdProperty()
    emailAddr = EmailProperty(unique_index=True, required=True)
    userName = StringProperty(unique_index=True, required=True)
    nickname = StringProperty(required=True)
    keyIdAuth = StringProperty(unique_index=True, required=True) 
    description = StringProperty()
    picture = StringProperty()
    favArtists = ArrayProperty(StringProperty())
    favAlbums = ArrayProperty(StringProperty())
    favSongs = ArrayProperty(StringProperty())
    favPlaylists = ArrayProperty(StringProperty())
    pinnedComm = ArrayProperty(StringProperty())

    #Relations
    follow = RelationshipTo('User', 'Follow')
    

    