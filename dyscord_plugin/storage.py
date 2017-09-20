class StorageManager:
    """ Generic storage manager, for implementation... """
    def __len__(self): raise NotImplementedError

    def __getitem__(self, key): raise NotImplementedError

    def __setitem__(self, key, value): raise NotImplementedError

    def __delitem__(self, key): raise NotImplementedError

    def __iter__(self): raise NotImplementedError

    def __contains__(self, key): raise NotImplementedError

    def get(self, key): raise NotImplementedError

    def set(self, key, value): raise NotImplementedError
