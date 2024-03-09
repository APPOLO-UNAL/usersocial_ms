from neomodel import StructuredNode, StringProperty, ArrayProperty,UniqueIdProperty, RelationshipTo, EmailProperty

from .nodeutils import NodeUtils

#Users 
class User(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    emailAddr = EmailProperty(unique_index=True, required=True)
    userName = StringProperty(unique_index=True, required=True)
    keyIdAuth = StringProperty(unique_index=True, required=True) 
    arrArtists = ArrayProperty(StringProperty())
    arrTracks = ArrayProperty(StringProperty())
    arrAlbums = ArrayProperty(StringProperty())

    #Relations
    follow = RelationshipTo('User', 'Follow')


    @property
    def serialize(self):
        return {
            'node_properties': {
                'uid': self.uid,
                'emailAddr': self.emailAddr,
                'userName': self.userName,
                'keyIdAuth': self.keyIdAuth,
                'arrArtists': self.arrArtists,
                'arrTracks': self.arrTracks,
                'arrAlbums': self.arrAlbums,
            },
        }


    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'User',
                'nodes_related': self.serialize_relationships(self.users.all()),
            },
        ]
    

    