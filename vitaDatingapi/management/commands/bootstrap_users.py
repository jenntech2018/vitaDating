
from django.core.management.base import BaseCommand, CommandError
from vitaDatinguser.models import vitaDatinguser

class Command(BaseCommand):
    help = "Bootstraps users usable via manage.py"

    def handle(self, *args, **kwargs):
        celebrities = [
            {
                "display_name":"Justin Bieber",
                "username":"justinbieber",
                "email":"justinbieber@thebiebz.com",
                "bio":"hey go listen to my album it's pretty rad",
                "website":"www.JustinBieber.lnk.to/Justice",
            },
            {
                "display_name":"Queen Latifah",
                "username":"thequeen",
                "email":"queenlatifah@thequeen.com",
                "bio":"the queen up in this party!!",
                "website":"queenlatifah.com",
            }
        ]
        for celeb in celebrities:
            vitaDatinguser.objects.create(
                display_name=celeb["display_name"],
                username=celeb["username"],
                email=celeb["email"],
                bio=celeb["bio"],
                website=celeb["website"],
                verified=True,
                password="verysecurepassword123123"
            )

        self.stdout.write("Added celebs")