from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from users.models import Profile


class OwnerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ("role",)
        
        
class NormalUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = UserCreationForm.Meta.fields
        
    def save(self, commit=True):
        content_type = ContentType.objects.get_for_model(Profile)
        permission = Permission.objects.get(content_type=content_type , codename= "can_change_profile")
        user = super().save(commit=True)
        user.role = "user"
        user.user_permissions.add(permission)
        if commit:
            user.save()
        return user