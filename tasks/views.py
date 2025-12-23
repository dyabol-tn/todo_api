from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

tasks = []
next_id = 1

class TaskList(APIView):
    def get(self, request):
        return Response(tasks)

    def post(self, request):
        global next_id
        data = request.data
        task = {
            "id": next_id,
            "title": data.get("title"),
            "description": data.get("description"),
            "status": data.get("status", "todo")
        }
        tasks.append(task)
        next_id += 1
        return Response(task, status=status.HTTP_201_CREATED)

class TaskDetail(APIView):
    def get(self, request, id):
        for task in tasks:
            if task["id"] == id:
                return Response(task)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        for task in tasks:
            if task["id"] == id:
                task.update(request.data)
                return Response(task)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        for task in tasks:
            if task["id"] == id:
                task.update(request.data)
                return Response(task)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        for task in tasks:
            if task["id"] == id:
                tasks.remove(task)
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)