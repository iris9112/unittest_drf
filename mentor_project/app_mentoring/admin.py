from django.contrib import admin

from app_mentoring.models.role import Role
from app_mentoring.models.node import Node
from app_mentoring.models.user import User
from app_mentoring.models.user_profile import UserProfile
from app_mentoring.models.mentoring import Mentoring


admin.site.register(Role)
admin.site.register(Node)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Mentoring)

