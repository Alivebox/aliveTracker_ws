class ProjectUserDTO(object):
    def __init__(self, user_id, project_id, role_id, user_name, role_name ):
        self.project_id = project_id
        self.user_id = user_id
        self.role_id = role_id
        self.user_name = user_name
        self.role_name = role_name

    def __unicode__(self):
        return self.name