from django.http.response import Http404
from django.shortcuts import get_object_or_404
from .models import Profile, MyUser


class UserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs.get('id')
        profile = get_object_or_404(MyUser, id=pk)
        if profile.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Cant See This Page")