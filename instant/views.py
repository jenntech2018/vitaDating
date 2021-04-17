from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.views import View
from .forms import MessageForm
from .models import Chat, Message
from vibe_user.models import Viber


class MessagesView(View):
    # users = {}
    def get(self, request, recipient):
        # try:
        messages = Message.objects.filter(recipient=request.user.id)
        print(messages)
        #     chat.message_set.filter(is_read=False).exclude(
        #         author=request.user).update(is_read=True)
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

    def post(self, request, recipient):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.recipient = recipient
            message.author = request.user
            message.save()
        return redirect(reverse({'message':message}, kwargs={'recipient': recipient}))

    def new_message(request):
        context = {}
        if request.method == "POST":
            form = MessageForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_msg = Message.objects.create(
                    message=data['message'],
                    recipient=data['recipient'],
                )
                return redirect('/messages/new/')
        form=MessageForm()   
        context.update({'message': "Submitted Successfully!!!!! YAY!"})
        form = MessageForm()
        context.update({'form': form})
        return render(
            request,
            "messaging/new_message.html", 
            context
        )
