class PermissionGroupDTO(object):
    def __init__(self, idPermission, namePermission):
        self.idPermission = idPermission
        self.namePermission = namePermission


class UserDTO(object):
    def __init__(self, user_id, email, role_id):
        self.user_id = user_id
        self.email = email
        self.role_id = role_id


class UserLoginDTO(object):
    def __init__(self, id, email, name, entity_status):
        self.id = id
        self.email = email
        self.name = name
        self.entity_status = entity_status

