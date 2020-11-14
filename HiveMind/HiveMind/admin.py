class UserInfoAdmin(admin.ModelAdmin):
    model = UserInfo
    list_display = ['user', 'language']
    list_editable = ['language']
    search_fields = ['user__username']


class NotifiableModelAdmin(admin.ModelAdmin):
    actions = ['notify_researcher']
    search_fields = ['name', 'researcher__username', 'groups__name', 'comment']
    
    
def user_display_name(self, instance):
        if instance.user:
            return instance.user.username
        else:
            return ''
    user_display_name.short_description = _('User')
    user_display_name.admin_order_field = 'user'

    def groups_display_name(self, instance):
        if instance.groups.count() > 0:
            return ", ".join(str(group) for group in instance.groups.all())
        return ''
    groups_display_name.short_description = _('Groups')
    

class IosAppAdmin(NotifiableModelAdmin):
    form = iOSAppAdminForm
    list_display = ('name', 'user_display_name', 'groups_display_name', 'version', 'comment', 'updatedAt')
    filter_horizontal = ['groups']

    fieldsets = (
        (_('App info'), {
            'fields': ('user', 'groups', 'name', 'version', 'bundle_identifier', 'app_binary', 'comment')
        }),
        (_('Provide these deploy on iOS 12'), {
            'fields': ('display_image', 'full_size_image')
        }),
    )

    
    
   
