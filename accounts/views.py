from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, TemplateView
from django.views.generic.base import View

from Bookies.constants import OrderStatuses
from Bookies.models import Book, OrderItem
from accounts.forms import UserChangeForm


class UpdateUserView(UpdateView):
    template_name = 'EditUser.html'
    form_class = UserChangeForm
    success_url = reverse_lazy("index")
    model = User


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "EditUser.html"

    def form_valid(self, form):
        ret_val = super().form_valid(form)
        client_group = Group.objects.get(name='Client')
        self.object.groups.add(client_group)
        return ret_val



class UserProfileView(TemplateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'UserProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'user': self.request.user,
            'order_items': OrderItem.objects.filter(
                order__user=self.request.user,
                order__status=OrderStatuses.COMLETED
            )
        })
        return context


# password change view

class ChangePasswordView(View):
    def post(self,request):
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('userprofile', kwargs={'pk': request.user.id}))
        else:
            return redirect(reverse('userprofile', kwargs={'pk': request.user.id}))

    def get(self,request):
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)
