from django.contrib.auth.forms import UserCreationForm
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
        user = super().save(commit=True)
        user.role = "user"
        if commit:
            user.save()
        return user