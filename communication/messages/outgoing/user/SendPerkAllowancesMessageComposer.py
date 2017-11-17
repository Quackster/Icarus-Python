import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class SendPerkAllowancesMessageComposer:
    def __init__(self,):
        self.response = Response(outgoing.SendPerkAllowancesMessageComposer)
        self.response.write_int(16);
        self.response.write_string("USE_GUIDE_TOOL");
        self.response.write_string("");
        self.response.write_bool(False);
        self.response.write_string("GIVE_GUIDE_TOURS");
        self.response.write_string("requirement.unfulfilled.helper_le");
        self.response.write_bool(False);
        self.response.write_string("JUDGE_CHAT_REVIEWS");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("VOTE_IN_COMPETITIONS");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("CALL_ON_HELPERS");
        self.response.write_string("");
        self.response.write_bool(False);
        self.response.write_string("CITIZEN");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("TRADE");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("HEIGHTMAP_EDITOR_BETA");
        self.response.write_string("");
        self.response.write_bool(False);
        self.response.write_string("EXPERIMENTAL_CHAT_BETA");
        self.response.write_string("requirement.unfulfilled.helper_level_2");
        self.response.write_bool(True);
        self.response.write_string("EXPERIMENTAL_TOOLBAR");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("BUILDER_AT_WORK");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("NAVIGATOR_PHASE_ONE_2014");
        self.response.write_string("");
        self.response.write_bool(False);
        self.response.write_string("CAMERA");
        self.response.write_string("");
        self.response.write_bool(False);
        self.response.write_string("NAVIGATOR_PHASE_TWO_2014");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("MOUSE_ZOOM");
        self.response.write_string("");
        self.response.write_bool(True);
        self.response.write_string("NAVIGATOR_ROOM_THUMBNAIL_CAMERA");
        self.response.write_string("");
        self.response.write_bool(False);
