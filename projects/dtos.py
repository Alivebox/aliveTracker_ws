class ProjectUserListDTO(object):
    def __init__(self, id, name, created, description, groupID, users):
        self.id = id
        self.name = name
        self.created = created
        self.description = description
        self.groupID = groupID
        self.users = users

    def __unicode__(self):
        return self.name


class UserDTO(object):
    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

    def __unicode__(self):
        return self.email