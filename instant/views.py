from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import MessageForm
from .models import Chat, Message
from vibe_user.models import Viber


class MessagesView(View):
    # users = {}
    def get(self, request, recipient):
        # try:
        messages = Message.objects.all()
        #     chat.message_set.filter(is_read=False).exclude(
        #         author=request.user).update(is_read=True)
        #     # else:
        #     #     chat = None
        # except Chat.DoesNotExist:
        #     chat = None

        return render(
            request,
            'messaging/dialog.html',
            {
                'messages': messages,
                'user_profile': request.user,
                'form': MessageForm(),
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse({'message':message}, kwargs={'chat_id': chat_id}))

