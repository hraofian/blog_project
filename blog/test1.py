# from django.shortcuts import render
from datetime import date




all_posts =[
    {
        'slug': 'learning-java',
        'title': 'java course',
        'author': 'hadi ardokhani',
        'image': '02.jpeg',
        'date': date(2022 ,4 ,5) ,
        'short_description': 'this is the java course and is very good',
        'content': """
            this is content java ,  this is content java , this is content  java,  this is content , 
            this is content ,  this is content  javajava, this is content ,  this is content ,
            """
    },
        {
        'slug': 'learning-html',
        'title': 'html course',
        'author': 'mohamad rezaee',
        'image': '01.png',
        'date': date(2019 ,2 ,1) ,
        'short_description': 'this is the html course and is very good',
        'content': """
            this is content html,  this is content html , this is content html,  this is content , 
            this is content html,  this is content html, this is content ,  this is content ,
            """
    },
        {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'mohamad ardokhani',
        'image': '03.jpeg',
        'date': date(2022 ,9 ,9) ,
        'short_description': 'this is the django course and is very good',
        'content': """
            this is content ,  this is content , this is content ,  this is content , 
            this is content ,  this is content , this is content ,  this is content ,
            """
    },
]

# print(all_posts)

def get_date(a):
    # print(a)
    # print(a['date'])
    # return a
    return a['date']

b= get_date(all_posts['date'])
print(b)

# print(get_date(['date']))

# def index(request):
#     # print(request)
#     sorted_posts = sorted(all_posts , key=get_date)
#     # print(sorted_posts)
#     latest_post = sorted_posts[-2:]
#     # print(latest_post)
#     return render(request , 'blog/index.html' , {
#         'latest_post': latest_post
#     })




