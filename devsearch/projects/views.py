from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': "RoomieHunt",
        'description': 'Web app to find your best match to live with!'
    },
      {
        'id': '2',
        'title': "GoalHub",
        'description': 'All your teamwork activities, progress and more in once place!'
    },
      {
        'id': '3',
        'title': "Fridge2Table",
        'description': 'Grab your availble groceries and start creating awesome recipes!'
    },
]
def projects(request):
    msg = 'Hello, you are on the projects page'
    return render(request, 'projects/projects.html', {'projectList': projectList})

def project(request, pk):
    project = None
    for i in projectList:
        if i['id'] == pk :
            project= i
    return render(request, 'projects/single-project.html', {'project': project})