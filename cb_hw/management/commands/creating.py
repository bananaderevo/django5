import random
import sys
from datetime import date

from django.core.management.base import BaseCommand

from faker import Faker

from ...models import Author, Book, Comments, Publisher, Store


fake = Faker()
fake_s = Faker(['en_US', 'ja_JP', 'it_IT'])

rand_books = ['English Lessons * for adults',
              'Recipes for everyone (part *)',
              'How to create c4 at home *',
              'Life Of No-One *',
              'See you on the beach (part *)',
              'Everyone needs a hug *',
              'My mom told me to go outside *...',
              'How to be retard *',
              'Murder in heaven (part *)',
              'Adventures From Kyiv To NY *', ]


class Command(BaseCommand):
    help = 'Creating some books'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)

    def handle(self, *args, **options):
        if 0 > options['num']:
            sys.stdout.write('Error, wrong number: number should be more than 0.\n')
        else:
            for i in range(options['num']):
                Author.objects.create(name=fake.name(),
                                      age=random.randint(20, 500))
                rl = fake.name().split()[1]
                rf = fake.name().split()[0]
                Publisher.objects.create(name=rl + rf + str(random.randint(0, 1000)) + "'s Pub. Company")
                Comments.objects.create(comment=fake.text())
                Book.objects.create(name=rand_books[random.randint(0, 8)].replace('*', str(random.randint(1, 20))),
                                    pages=random.randint(30, 500),
                                    price=random.randint(3, 50),
                                    rating=random.randint(10, 100) / 10,
                                    publisher=Publisher.objects.last(),
                                    pubdate=date(random.randint(1930, 2022), random.randint(1, 12),
                                                 random.randint(1, 28)),
                                    comment=Comments.objects.last()).authors.set([Author.objects.last()])

                Store.objects.create(name=fake_s.name().lower().replace(' ', '').title()
                                     ).books.set([Book.objects.last()])
