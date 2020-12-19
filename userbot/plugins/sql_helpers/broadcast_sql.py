import threading

from sqlalchemy import Column, String, UnicodeText, distinct, func

from . import BASE, SESSION


class SkullBroadcast(BASE):
    __tablename__ = "skullbroadcast"
    keywoard = Column(UnicodeText, primary_key=True)
    group_id = Column(String(14), primary_key=True, nullable=False)

    def __init__(self, keywoard, group_id):
        self.keywoard = keywoard
        self.group_id = str(group_id)

    def __repr__(self):
        return "<Skull Broadcast channels '%s' for %s>" % (self.group_id, self.keywoard)

    def __eq__(self, other):
        return bool(
            isinstance(other, SkullBroadcast)
            and self.keywoard == other.keywoard
            and self.group_id == other.group_id
        )


SkullBroadcast.__table__.create(checkfirst=True)

SKULLBROADCAST_INSERTION_LOCK = threading.RLock()

BROADCAST_CHANNELS = {}


def add_to_broadcastlist(keywoard, group_id):
    with SKULLBROADCAST_INSERTION_LOCK:
        broadcast_group = SkullBroadcast(keywoard, str(group_id))

        SESSION.merge(broadcast_group)
        SESSION.commit()
        BROADCAST_CHANNELS.setdefault(keywoard, set()).add(str(group_id))


def rm_from_broadcastlist(keywoard, group_id):
    with SKULLBROADCAST_INSERTION_LOCK:
        broadcast_group = SESSION.query(SkullBroadcast).get((keywoard, str(group_id)))
        if broadcast_group:
            if str(group_id) in BROADCAST_CHANNELS.get(keywoard, set()):
                BROADCAST_CHANNELS.get(keywoard, set()).remove(str(group_id))

            SESSION.delete(broadcast_group)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def is_in_broadcastlist(keywoard, group_id):
    with SKULLBROADCAST_INSERTION_LOCK:
        broadcast_group = SESSION.query(SkullBroadcast).get((keywoard, str(group_id)))
        return bool(broadcast_group)


def del_keyword_broadcastlist(keywoard):
    with SKULLBROADCAST_INSERTION_LOCK:
        broadcast_group = (
            SESSION.query(SkullBroadcast.keywoard)
            .filter(SkullBroadcast.keywoard == keywoard)
            .delete()
        )
        BROADCAST_CHANNELS.pop(keywoard)
        SESSION.commit()


def get_chat_broadcastlist(keywoard):
    return BROADCAST_CHANNELS.get(keywoard, set())


def get_broadcastlist_chats():
    try:
        chats = SESSION.query(SkullBroadcast.keywoard).distinct().all()
        return [i[0] for i in chats]
    finally:
        SESSION.close()


def num_broadcastlist():
    try:
        return SESSION.query(SkullBroadcast).count()
    finally:
        SESSION.close()


def num_broadcastlist_chat(keywoard):
    try:
        return (
            SESSION.query(SkullBroadcast.keywoard)
            .filter(SkullBroadcast.keywoard == keywoard)
            .count()
        )
    finally:
        SESSION.close()


def num_broadcastlist_chats():
    try:
        return SESSION.query(func.count(distinct(SkullBroadcast.keywoard))).scalar()
    finally:
        SESSION.close()


def __load_chat_broadcastlists():
    global BROADCAST_CHANNELS
    try:
        chats = SESSION.query(SkullBroadcast.keywoard).distinct().all()
        for (keywoard,) in chats:
            BROADCAST_CHANNELS[keywoard] = []

        all_groups = SESSION.query(SkullBroadcast).all()
        for x in all_groups:
            BROADCAST_CHANNELS[x.keywoard] += [x.group_id]

        BROADCAST_CHANNELS = {x: set(y) for x, y in BROADCAST_CHANNELS.items()}

    finally:
        SESSION.close()


__load_chat_broadcastlists()
