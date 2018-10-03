class Action:
    def __init__(self, account, name, actor, permission, data):
        self.account = account
        self.name = name
        self.authorization = [{
            'actor': actor,
            'permission': permission
        }]
        self.data = data

