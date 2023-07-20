# summer_project_bankend
## Author: Ihab Abaas

> ## The project idea
We are creating a website that will offer three distinct, hilarious, and practical games for our users' enjoyment.

> ## The first game
In this game, we aim to challenge the player's knowledge by offering two exciting modes: one-player and two-player.

Single Player Mode:
 Test your knowledge and skills by taking on challenging questions and tasks all on your own. With various levels of difficulty, you'll have the opportunity to expand your knowledge and become a true master!

Two-Player Mode:
 Invite a friend to join the fun! Compete head-to-head with someone else and see who possesses the superior knowledge. Show off your expertise across a range of topics and engage in a battle of wits!

With captivating questions and diverse challenges, this game will keep you engaged for hours on end. Sharpen your mind, learn new facts, and have a blast while playing either alone or with a friend. Let's embark on this knowledge adventure together! 


> ## The secoed game

> ## The third game


> # The backend side

>> I used to this part python django
1. create the project for the games
       *django-admin startproject games .*
2. create an app for the fisrt app game
       *python manage.py startapp questions*
3. create a superuser
       *python manage.py createsuperuser*
       username: admin
       email: admin@admin.com
       password: admin123
4. do python manage.py makemigrations
          python manage.py migrate
5. create the model to use in this game that will contain [type,question,correct, wrong1 ,wrong2 , wrong3]
6. fix the views and the urls:
         - QuestionsDataListView: A view for listing and creating QuestionsData objects.
         url:(api/v1/QC/questions/)
         - QuestionsDataDetailView: A view for listing and creating QuestionsData objects.
         url: (api/v1/QC/ question/<int:pk>)
         - upload_csv: Handle the CSV file upload and save data to the database.
         url: (api/v1/QC/upload)
         - download_csv: Download CSV file containing QuestionsData.
         url:(api/v1/QC/download)
         - clear_all_data(request): Clear all data from the database
         url: (api/v1/QC/clear)