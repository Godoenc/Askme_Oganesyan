from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

from app.models import UserMan, Profile, Tag, Question, Answer, Likes_Of_Question, Likes_Of_Answers
from faker import Faker
import random
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data generation')

    def handle(self, *args, **options):
        ratio = options['ratio']
        fake = Faker()

        num_users = ratio
        num_questions = ratio * 10
        num_answers = ratio * 100
        num_tags = ratio
        num_likes = ratio * 200

        self.stdout.write(self.style.SUCCESS(f'Starting data generation with ratio {ratio}'))

        # Create Users and Profiles
        users = []
        profiles = []
        existing_usernames = set(User.objects.values_list('username', flat=True))  # Существующие имена пользователей

        for _ in tqdm(range(num_users), desc="Creating Users and Profiles"):
            username = fake.user_name()
            while username in existing_usernames:  # Проверяем уникальность имени
                username = fake.user_name()

            email = fake.email()
            password = fake.password()

            user = User.objects.create_user(username=username, email=email, password=password)
            users.append(user)
            existing_usernames.add(username)  # Добавляем имя в множество существующих

            user_man = UserMan.objects.create(user=user)
            profile = Profile.objects.create(
                user=user_man,
                name=fake.name(),
                registration_at=fake.date(),
                about_me=fake.text(max_nb_chars=200),
            )
            profiles.append(profile)

        # Create Tags
        tags = []
        for _ in tqdm(range(num_tags), desc="Creating Tags"):
            tag = Tag.objects.create(
                name=fake.word(),
            )
            tags.append(tag)

        # Create Questions
        questions = []
        for _ in tqdm(range(num_questions), desc="Creating Questions"):
            author = random.choice(profiles)
            question = Question.objects.create(
                title=fake.sentence(),
                text=fake.text(max_nb_chars=500),
                author=author
            )
            question.tag.set(random.sample(tags, k=random.randint(1, 5)))
            questions.append(question)

        # Create Answers
        answers = []
        for _ in tqdm(range(num_answers), desc="Creating Answers"):
            author = random.choice(profiles)
            question = random.choice(questions)
            answer = Answer.objects.create(
                title=fake.sentence(),
                text=fake.text(max_nb_chars=500),
                author=author
            )
            answers.append(answer)

        # Create Likes for Questions
        likes_of_questions = []
        existing_question_likes = set(
            Likes_Of_Question.objects.values_list("profile_id", "question_id")
        )  # Существующие пары (profile_id, question_id)

        for _ in tqdm(range(num_likes), desc="Creating Likes for Questions"):
            question = random.choice(questions)
            profile = random.choice(profiles)

            while (profile.id, question.id) in existing_question_likes:  # Проверяем уникальность пары
                question = random.choice(questions)
                profile = random.choice(profiles)

            try:
                like = Likes_Of_Question.objects.create(
                    title=fake.sentence(),
                    question=question,
                    profile=profile,
                    count_of_goods=random.randint(0, 50),
                    count_of_bads=random.randint(0, 50),
                )
                likes_of_questions.append(like)
                existing_question_likes.add((profile.id, question.id))  # Добавляем в множество
            except IntegrityError:
                continue  # Обрабатываем редкие случаи гонок

        # Create Likes for Answers
        likes_of_answers = []
        existing_answer_likes = set(
            Likes_Of_Answers.objects.values_list("profile_id", "answer_id")
        )  # Существующие пары (profile_id, answer_id)

        for _ in tqdm(range(num_likes), desc="Creating Likes for Answers"):
            answer = random.choice(answers)
            profile = random.choice(profiles)

            while (profile.id, answer.id) in existing_answer_likes:  # Проверяем уникальность пары
                answer = random.choice(answers)
                profile = random.choice(profiles)

            try:
                like = Likes_Of_Answers.objects.create(
                    title=fake.sentence(),
                    answer=answer,
                    profile=profile,
                    count_of_goods=random.randint(0, 50),
                    count_of_bads=random.randint(0, 50),
                )
                likes_of_answers.append(like)
                existing_answer_likes.add((profile.id, answer.id))  # Добавляем в множество
            except IntegrityError:
                continue  # Обрабатываем редкие случаи гонок

        self.stdout.write(self.style.SUCCESS('Database filled successfully!'))