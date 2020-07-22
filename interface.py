import apirequest
from pprint import pprint

login = apirequest.login()
pprint(apirequest.searchSongs(login, track="Under Pressure", artist="Queen"))

