import requests
import typing
    

class qbittorrent_rpc:
    def __init__(self, secured: bool = False, host: str = "127.0.0.1", port: int = 8080):
        self.s = requests.Session()
        self.rpc_url = "http{}://{}:{}".format("s" if secured else "", host, port)
        self.Authentication = Authentication()
        self.Authentication.post = self.post
        self.Application = Application()
        self.Application.post = self.post
        self.Log = Log()
        self.Log.post = self.post
        self.Sync = Sync()
        self.Sync.post = self.post
        self.Transfer_info = Transfer_info()
        self.Transfer_info.post = self.post
        self.Torrent_management = Torrent_management()
        self.Torrent_management.post = self.post
        self.RSS_experimental = RSS_experimental()
        self.RSS_experimental.post = self.post
        self.Search = Search()
        self.Search.post = self.post

    def post(self, api, params, files):
        r = self.s.post(self.rpc_url+api, data=params, files=files or None)
        try:
            return r.json()
        except:
            try:
                return r.content.decode()
            except:
                return r.content


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#authentication
class Authentication:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#login
    def login(
        self,
        # Username used to access the WebUI
        username: str = None,
        # Password used to access the WebUI
        password: str = None
    ):
        data = {k: v for k, v in [["username", username], ["password", password]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/auth/login", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#logout
    def logout(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/auth/logout", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#application
class Application:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-version
    def version(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/version", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-api-version
    def webapiVersion(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/webapiVersion", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-build-info
    def buildInfo(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/buildInfo", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#shutdown-application
    def shutdown(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/shutdown", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-preferences
    def preferences(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/preferences", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-application-preferences
    def setPreferences(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/setPreferences", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-default-save-path
    def defaultSavePath(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/app/defaultSavePath", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#log
class Log:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-log
    def main(
        self,
        # Include normal messages (default:  true )
        normal: bool = None,
        # Include info messages (default:  true )
        info: bool = None,
        # Include warning messages (default:  true )
        warning: bool = None,
        # Include critical messages (default:  true )
        critical: bool = None,
        # Exclude messages with "message id" <=  last_known_id  (default:  -1 )
        last_known_id: int = None
    ):
        data = {k: v for k, v in [["normal", normal], ["info", info], ["warning", warning], ["critical", critical], ["last_known_id", last_known_id]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/log/main", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-peer-log
    def peers(
        self,
        # Exclude messages with "message id" <=  last_known_id  (default:  -1 )
        last_known_id: int = None
    ):
        data = {k: v for k, v in [["last_known_id", last_known_id]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/log/peers", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#sync
class Sync:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-main-data
    def maindata(
        self,
        # Response ID. If not provided,  rid=0  will be assumed. If the given  rid  is different from the one of last server reply,  full_update  will be  true  (see the server reply details for more info)
        rid: int = None
    ):
        data = {k: v for k, v in [["rid", rid]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/sync/maindata", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-peers-data
    def torrentPeers(
        self,
        # Torrent hash
        hash: str = None,
        # Response ID. If not provided,  rid=0  will be assumed. If the given  rid  is different from the one of last server reply,  full_update  will be  true  (see the server reply details for more info)
        rid: int = None
    ):
        data = {k: v for k, v in [["hash", hash], ["rid", rid]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/sync/torrentPeers", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#transfer-info
class Transfer_info:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-transfer-info
    def info(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/info", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-alternative-speed-limits-state
    def speedLimitsMode(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/speedLimitsMode", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#toggle-alternative-speed-limits
    def toggleSpeedLimitsMode(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/toggleSpeedLimitsMode", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-download-limit
    def downloadLimit(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/downloadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-global-download-limit
    def setDownloadLimit(
        self,
        # The global download speed limit to set in bytes/second
        limit: int = None
    ):
        data = {k: v for k, v in [["limit", limit]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/setDownloadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-global-upload-limit
    def uploadLimit(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/uploadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-global-upload-limit
    def setUploadLimit(
        self,
        # The global upload speed limit to set in bytes/second
        limit: int = None
    ):
        data = {k: v for k, v in [["limit", limit]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/setUploadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#ban-peers
    def banPeers(
        self,
        # The peer to ban, or multiple peers separated by a pipe  | . Each peer is a colon-separated  host:port \n
        peers: str = None
    ):
        data = {k: v for k, v in [["peers", peers]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/transfer/banPeers", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management
class Torrent_management:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-list
    def info(
        self,
        # Filter torrent list by state. Allowed state filters:  all ,  downloading ,  seeding ,  completed ,  paused ,  active ,  inactive ,  resumed ,  stalled ,  stalled_uploading ,  stalled_downloading ,  errored \n
        filter: str = None,
        # Get torrents with the given category (empty string means "without category"; no "category" parameter means "any category" <- broken until  #11748  is resolved). Remember to URL-encode the category name. For example,  My category  becomes  My%20category \n
        category: str = None,
        # Get torrents with the given tag (empty string means "without tag"; no "tag" parameter means "any tag". Remember to URL-encode the category name. For example,  My tag  becomes  My%20tag \n
        tag: str = None,
        # Sort torrents by given key. They can be sorted using any field of the response's JSON array (which are documented below) as the sort key.
        sort: str = None,
        # Enable reverse sorting. Defaults to  false \n
        reverse: bool = None,
        # Limit the number of torrents returned
        limit: int = None,
        # Set offset (if less than 0, offset from end)
        offset: int = None,
        # Filter by hashes. Can contain multiple hashes separated by  | \n
        hashes: str = None
    ):
        data = {k: v for k, v in [["filter", filter], ["category", category], ["tag", tag], ["sort", sort], ["reverse", reverse], ["limit", limit], ["offset", offset], ["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/info", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-generic-properties
    def properties(
        self,
        # The hash of the torrent you want to get the generic properties of
        hash: str = None
    ):
        data = {k: v for k, v in [["hash", hash]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/properties", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-trackers
    def trackers(
        self,
        # The hash of the torrent you want to get the trackers of
        hash: str = None
    ):
        data = {k: v for k, v in [["hash", hash]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/trackers", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-web-seeds
    def webseeds(
        self,
        # The hash of the torrent you want to get the webseeds of
        hash: str = None
    ):
        data = {k: v for k, v in [["hash", hash]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/webseeds", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-contents
    def files(
        self,
        # The hash of the torrent you want to get the contents of
        hash: str = None,
        # The indexes of the files you want to retrieve.  indexes  can contain multiple values separated by  | .
        indexes: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["indexes", indexes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/files", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-pieces'-states
    def pieceStates(
        self,
        # The hash of the torrent you want to get the pieces' states of
        hash: str = None
    ):
        data = {k: v for k, v in [["hash", hash]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/pieceStates", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-pieces'-hashes
    def pieceHashes(
        self,
        # The hash of the torrent you want to get the pieces' hashes of
        hash: str = None
    ):
        data = {k: v for k, v in [["hash", hash]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/pieceHashes", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#pause-torrents
    def pause(
        self,
        # The hashes of the torrents you want to pause.  hashes  can contain multiple hashes separated by  | , to pause multiple torrents, or set to  all , to pause all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/pause", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#resume-torrents
    def resume(
        self,
        # The hashes of the torrents you want to resume.  hashes  can contain multiple hashes separated by  | , to resume multiple torrents, or set to  all , to resume all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/resume", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-torrents
    def delete(
        self,
        # The hashes of the torrents you want to delete.  hashes  can contain multiple hashes separated by  | , to delete multiple torrents, or set to  all , to delete all torrents.
        hashes: str = None,
        # If set to  true , the downloaded data will also be deleted, otherwise has no effect.
        deleteFiles: bool = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["deleteFiles", deleteFiles]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/delete", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#recheck-torrents
    def recheck(
        self,
        # The hashes of the torrents you want to recheck.  hashes  can contain multiple hashes separated by  | , to recheck multiple torrents, or set to  all , to recheck all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/recheck", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#reannounce-torrents
    def reannounce(
        self,
        # The hashes of the torrents you want to reannounce.  hashes  can contain multiple hashes separated by  | , to reannounce multiple torrents, or set to  all , to reannounce all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/reannounce", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-new-torrent
    def add(
        self,
        # URLs separated with newlines
        urls: str = None,
        # Raw data of torrent file.  torrents  can be presented multiple times.
        torrents: typing.IO = None,
        # Download folder
        savepath: str = None,
        # Cookie sent to download the .torrent file
        cookie: str = None,
        # Category for the torrent
        category: str = None,
        # Tags for the torrent, split by ','
        tags: str = None,
        # Skip hash checking. Possible values are  true ,  false  (default)
        skip_checking: str = None,
        # Add torrents in the paused state. Possible values are  true ,  false  (default)
        paused: str = None,
        # Create the root folder. Possible values are  true ,  false , unset (default)
        root_folder: str = None,
        # Rename torrent
        rename: str = None,
        # Set torrent upload speed limit. Unit in bytes/second
        upLimit: int = None,
        # Set torrent download speed limit. Unit in bytes/second
        dlLimit: int = None,
        # Set torrent share ratio limit
        ratioLimit: float = None,
        # Set torrent seeding time limit. Unit in seconds
        seedingTimeLimit: int = None,
        # Whether Automatic Torrent Management should be used
        autoTMM: bool = None,
        # Enable sequential download. Possible values are  true ,  false  (default)
        sequentialDownload: str = None,
        # Prioritize download first last piece. Possible values are  true ,  false  (default)
        firstLastPiecePrio: str = None
    ):
        data = {k: v for k, v in [["urls", urls], ["savepath", savepath], ["cookie", cookie], ["category", category], ["tags", tags], ["skip_checking", skip_checking], ["paused", paused], ["root_folder", root_folder], ["rename", rename], ["upLimit", upLimit], ["dlLimit", dlLimit], ["ratioLimit", ratioLimit], ["seedingTimeLimit", seedingTimeLimit], ["autoTMM", autoTMM], ["sequentialDownload", sequentialDownload], ["firstLastPiecePrio", firstLastPiecePrio]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [["torrents", torrents]] if v is not None}
        return self.post("/api/v2/torrents/add", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-trackers-to-torrent
    def addTrackers(
        self,
        # The hash of the torrent
        hash: str = None,
        # %0A (aka LF newline) between trackers. Ampersand in tracker urls MUST be escaped.
        urls: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["urls", urls]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/addTrackers", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#edit-trackers
    def editTracker(
        self,
        # The hash of the torrent
        hash: str = None,
        # The tracker URL you want to edit
        origUrl: str = None,
        # The new URL to replace the  origUrl \n
        newUrl: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["origUrl", origUrl], ["newUrl", newUrl]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/editTracker", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-trackers
    def removeTrackers(
        self,
        # The hash of the torrent
        hash: str = None,
        # URLs to remove, separated by  | \n
        urls: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["urls", urls]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/removeTrackers", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-peers
    def addPeers(
        self,
        # The hash of the torrent, or multiple hashes separated by a pipe  | \n
        hashes: str = None,
        # The peer to add, or multiple peers separated by a pipe  | . Each peer is a colon-separated  host:port \n
        peers: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["peers", peers]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/addPeers", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#increase-torrent-priority
    def increasePrio(
        self,
        # The hashes of the torrents you want to increase the priority of.  hashes  can contain multiple hashes separated by  | , to increase the priority of multiple torrents, or set to  all , to increase the priority of all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/increasePrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#decrease-torrent-priority
    def decreasePrio(
        self,
        # The hashes of the torrents you want to decrease the priority of.  hashes  can contain multiple hashes separated by  | , to decrease the priority of multiple torrents, or set to  all , to decrease the priority of all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/decreasePrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#maximal-torrent-priority
    def topPrio(
        self,
        # The hashes of the torrents you want to set to the maximum priority.  hashes  can contain multiple hashes separated by  | , to set multiple torrents to the maximum priority, or set to  all , to set all torrents to the maximum priority.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/topPrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#minimal-torrent-priority
    def bottomPrio(
        self,
        # The hashes of the torrents you want to set to the minimum priority.  hashes  can contain multiple hashes separated by  | , to set multiple torrents to the minimum priority, or set to  all , to set all torrents to the minimum priority.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/bottomPrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-file-priority
    def filePrio(
        self,
        # The hash of the torrent
        hash: str = None,
        # File ids, separated by  | \n
        id: str = None,
        # File priority to set (consult  torrent contents API  for possible values)
        priority: int = None
    ):
        data = {k: v for k, v in [["hash", hash], ["id", id], ["priority", priority]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/filePrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-download-limit
    def downloadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/downloadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-download-limit
    def setDownloadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # limit is the download speed limit in bytes per second you want to set
        limit: int = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["limit", limit]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setDownloadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-share-limit
    def setShareLimits(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # ratioLimit is the max ratio the torrent should be seeded until. -2 means the global limit should be used, -1 means no limit
        ratioLimit: float = None,
        # seedingTimeLimit is the max amount of time the torrent should be seeded. -2 means the global limit should be used, -1 means no limit
        seedingTimeLimit: int = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["ratioLimit", ratioLimit], ["seedingTimeLimit", seedingTimeLimit]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setShareLimits", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-torrent-upload-limit
    def uploadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/uploadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-upload-limit
    def setUploadLimit(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # limit is the upload speed limit in bytes per second you want to set
        limit: int = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["limit", limit]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setUploadLimit", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-location
    def setLocation(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # location is the location to download the torrent to. If the location doesn't exist, the torrent's location is unchanged
        location: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["location", location]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setLocation", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-name
    def rename(
        self,
        # Torrent hash
        hash: str = None,
        # new name
        name: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["name", name]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/rename", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-torrent-category
    def setCategory(
        self,
        # Torrent hash
        hash: str = None,
        # new name
        name: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["name", name]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setCategory", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-categories
    def categories(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/categories", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-new-category
    def createCategory(
        self,
        # new category
        category: str = None,
        # save path of new category
        savePath: str = None
    ):
        data = {k: v for k, v in [["category", category], ["savePath", savePath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/createCategory", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#edit-category
    def editCategory(
        self,
        # category
        category: str = None,
        # new save path of category
        savePath: str = None
    ):
        data = {k: v for k, v in [["category", category], ["savePath", savePath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/editCategory", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-categories
    def removeCategories(
        self,
        # categories can contain multiple cateogies separated by \n (%0A urlencoded)
        categories: str = None
    ):
        data = {k: v for k, v in [["categories", categories]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/removeCategories", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-torrent-tags
    def addTags(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # tags is the list of tags you want to add to passed torrents
        tags: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["tags", tags]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/addTags", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-torrent-tags
    def removeTags(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # tags is the list of tags you want to remove from passed torrents. Empty list removes all tags from relevant torrents
        tags: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["tags", tags]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/removeTags", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-tags
    def tags(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/tags", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#create-tags
    def createTags(
        self,
        # tags is a list of tags you want to create. Can contain multiple tags separated by ,
        tags: str = None
    ):
        data = {k: v for k, v in [["tags", tags]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/createTags", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-tags
    def deleteTags(
        self,
        # tags is a list of tags you want to create. Can contain multiple tags separated by ,
        tags: str = None
    ):
        data = {k: v for k, v in [["tags", tags]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/deleteTags", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-automatic-torrent-management
    def setAutoManagement(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # enable is a boolean, affects the torrents listed in hashes, default is false
        enable: bool = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["enable", enable]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setAutoManagement", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#toggle-sequential-download
    def toggleSequentialDownload(
        self,
        # The hashes of the torrents you want to toggle sequential download for.  hashes  can contain multiple hashes separated by  | , to toggle sequential download for multiple torrents, or set to  all , to toggle sequential download for all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/toggleSequentialDownload", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-first/last-piece-priority
    def toggleFirstLastPiecePrio(
        self,
        # The hashes of the torrents you want to toggle the first/last piece priority for.  hashes  can contain multiple hashes separated by  | , to toggle the first/last piece priority for multiple torrents, or set to  all , to toggle the first/last piece priority for all torrents.
        hashes: str = None
    ):
        data = {k: v for k, v in [["hashes", hashes]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/toggleFirstLastPiecePrio", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-force-start
    def setForceStart(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # value is a boolean, affects the torrents listed in hashes, default is false
        value: bool = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["value", value]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setForceStart", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-super-seeding
    def setSuperSeeding(
        self,
        # hashes can contain multiple hashes separated by | or set to all
        hashes: str = None,
        # value is a boolean, affects the torrents listed in hashes, default is false
        value: bool = None
    ):
        data = {k: v for k, v in [["hashes", hashes], ["value", value]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/setSuperSeeding", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-file
    def renameFile(
        self,
        # The hash of the torrent
        hash: str = None,
        # The old path of the torrent
        oldPath: str = None,
        # The new path to use for the file
        newPath: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["oldPath", oldPath], ["newPath", newPath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/renameFile", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-folder
    def renameFolder(
        self,
        # The hash of the torrent
        hash: str = None,
        # The old path of the torrent
        oldPath: str = None,
        # The new path to use for the file
        newPath: str = None
    ):
        data = {k: v for k, v in [["hash", hash], ["oldPath", oldPath], ["newPath", newPath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/torrents/renameFolder", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rss-(experimental)
class RSS_experimental:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-folder
    def addFolder(
        self,
        # Full path of added folder (e.g. "The Pirate Bay\Top100")
        path: str = None
    ):
        data = {k: v for k, v in [["path", path]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/addFolder", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#add-feed
    def addFeed(
        self,
        # URL of RSS feed (e.g. " http://thepiratebay.org/rss//top100/200 ")
        url: str = None,
        # Full path of added folder (e.g. "The Pirate Bay\Top100\Video")
        path: str = None
    ):
        data = {k: v for k, v in [["url", url], ["path", path]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/addFeed", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-item
    def removeItem(
        self,
        # Full path of removed item (e.g. "The Pirate Bay\Top100")
        path: str = None
    ):
        data = {k: v for k, v in [["path", path]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/removeItem", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#move-item
    def moveItem(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None,
        # New full path of item (e.g. "The Pirate Bay")
        destPath: str = None
    ):
        data = {k: v for k, v in [["itemPath", itemPath], ["destPath", destPath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/moveItem", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-items
    def items(
        self,
        # True if you need current feed articles
        withData: bool = None
    ):
        data = {k: v for k, v in [["withData", withData]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/items", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#mark-as-read
    def articleId(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None,
        # ID of article
        articleId: str = None
    ):
        data = {k: v for k, v in [["itemPath", itemPath], ["articleId", articleId]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/articleId", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#refresh-item
    def refreshItem(
        self,
        # Current full path of item (e.g. "The Pirate Bay\Top100")
        itemPath: str = None
    ):
        data = {k: v for k, v in [["itemPath", itemPath]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/refreshItem", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#set-auto-downloading-rule
    def setRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None,
        # JSON encoded rule definition
        ruleDef: str = None
    ):
        data = {k: v for k, v in [["ruleName", ruleName], ["ruleDef", ruleDef]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/setRule", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#rename-auto-downloading-rule
    def renameRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None,
        # New rule name (e.g. "The Punisher")
        newRuleName: str = None
    ):
        data = {k: v for k, v in [["ruleName", ruleName], ["newRuleName", newRuleName]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/renameRule", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#remove-auto-downloading-rule
    def removeRule(
        self,
        # Rule name (e.g. "Punisher")
        ruleName: str = None
    ):
        data = {k: v for k, v in [["ruleName", ruleName]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/removeRule", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-auto-downloading-rules
    def rules(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/rules", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-all-articles-matching-a-rule
    def matchingArticles(
        self,
        # Rule name (e.g. "Linux")
        ruleName: str = None
    ):
        data = {k: v for k, v in [["ruleName", ruleName]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/rss/matchingArticles", data, files)

    def post(self, *args, **kwargs):
        ...


# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#search
class Search:
    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#start-search
    def start(
        self,
        # Pattern to search for (e.g. "Ubuntu 18.04")
        pattern: str = None,
        # Plugins to use for searching (e.g. "legittorrents"). Supports multiple plugins separated by  | . Also supports  all  and  enabled \n
        plugins: str = None,
        # Categories to limit your search to (e.g. "legittorrents"). Available categories depend on the specified  plugins . Also supports  all \n
        category: str = None
    ):
        data = {k: v for k, v in [["pattern", pattern], ["plugins", plugins], ["category", category]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/start", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#stop-search
    def stop(
        self,
        # ID of the search job
        id: int = None
    ):
        data = {k: v for k, v in [["id", id]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/stop", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-status
    def status(
        self,
        # ID of the search job. If not specified, all search jobs are returned
        id: int = None
    ):
        data = {k: v for k, v in [["id", id]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/status", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-results
    def results(
        self,
        # ID of the search job
        id: int = None,
        # max number of results to return. 0 or negative means no limit
        limit: int = None,
        # result to start at. A negative number means count backwards (e.g.  -2  returns the 2 most recent results)
        offset: int = None
    ):
        data = {k: v for k, v in [["id", id], ["limit", limit], ["offset", offset]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/results", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#delete-search
    def delete(
        self,
        # ID of the search job
        id: int = None
    ):
        data = {k: v for k, v in [["id", id]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/delete", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-search-plugins
    def plugins(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/plugins", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#install-search-plugin
    def installPlugin(
        self,
        # Url or file path of the plugin to install (e.g. " https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/legittorrents.py "). Supports multiple sources separated by  | \n
        sources: str = None
    ):
        data = {k: v for k, v in [["sources", sources]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/installPlugin", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#uninstall-search-plugin
    def uninstallPlugin(
        self,
        # Name of the plugin to uninstall (e.g. "legittorrents"). Supports multiple names separated by  | \n
        names: str = None
    ):
        data = {k: v for k, v in [["names", names]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/uninstallPlugin", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#enable-search-plugin
    def enablePlugin(
        self,
        # Name of the plugin to enable/disable (e.g. "legittorrents"). Supports multiple names separated by  | \n
        names: str = None,
        # Whether the plugins should be enabled
        enable: bool = None
    ):
        data = {k: v for k, v in [["names", names], ["enable", enable]] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/enablePlugin", data, files)

    # https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#update-search-plugins
    def updatePlugins(
        self
    ):
        data = {k: v for k, v in [] if v is not None}
        files = {k: ("tmp.torrent", v, "application/x-bittorrent") for k, v in [] if v is not None}
        return self.post("/api/v2/search/updatePlugins", data, files)

    def post(self, *args, **kwargs):
        ...
