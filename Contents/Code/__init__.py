import os, platform

APPLICATIONS_PREFIX = "/applications/steamtv"

NAME = L('Title')
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

system = platform.system()
if system == 'Darwin':
    command = 'open'
elif system == 'Linux':
    command = 'steam'
else: # Not sure what to do on other OS (windows?)
    command = ''

def Start():
    Plugin.AddPrefixHandler(APPLICATIONS_PREFIX, ApplicationsMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="List", mediaType="items")

    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "InfoList"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)

def ApplicationsMainMenu():
    dir = MediaContainer(viewGroup="InfoList")

    dir.Append(
        Function(
             DirectoryItem(
                 LaunchApplication,
                 NAME,
                 subtitle=L('LaunchSubtitle'),
                 summary=L('LaunchSummary'),
                 thumb=R(ICON),
                 art=R(ART)
             )
         )
     )



    return dir

def LaunchApplication(sender):
    os.system("%s steam://open/bigpicture" % command)
    return MessageContainer(NAME, L('WaitMessage'))
