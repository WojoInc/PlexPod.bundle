PREFIX = "music/plexpod"
NAME = "PlexPod Podcast Plugin"

# Called by plex when first initializing the plugin
def Start():
    ObjectContainer.title1 = NAME

@handler(PREFIX,NAME)
def MainMenu():
    oc = ObjectContainer()
    oc.add(DirectoryObject(key=Callback(ChannelMenu, channel = 1), title="Channel 1")
    return oc