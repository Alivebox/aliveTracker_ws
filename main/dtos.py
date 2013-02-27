class PermissionGroupDTO(object):
    def __init__(self, user_id, group_id, role_id, idPermission, namePermission, idRole, roleName ):
        self.user_id = user_id
        self.group_id = group_id
        self.role_id = role_id
        self.idPermission = idPermission
        self.namePermission = namePermission
        self.idRole = idRole
        self.roleName = roleName
