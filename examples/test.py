from MlCheap.Client import Client
from MlCheap.Project import Project
from MlCheap.Task import Text_Tagging
import os

LABELER_TEST_API = 'e2fcd22b-4c71-4c37-a140-39835933edbe'
# LABELER_TEST_API = 'bf76eefd-8423-49e9-b63d-0f14bb615324'

client = Client(LABELER_TEST_API)
dir_path = os.path.dirname(os.path.realpath(__file__))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# upload a file

# icon_path = "1.jpg"
# file_path = os.path.join(dir_path, icon_path)
# response = client.upload_file(file_path)
# print(response)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# download a file

# down_path = "1.png"
# file_path = os.path.join(dir_path, down_path)
# response = client.download_file('61a9256ac50da0ed872e2178', file_path)
# print(response)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import a file

# down_path = "1.png"
# file_path = os.path.join(dir_path, down_path)
# response = client.download_file('61a9256ac50da0ed872e2178', file_path)
# print(response)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# create a project

# project_name = 'p12'
# labels_per_task = 3
# project = Project(project_name, labels_per_task)
# print("create a project", client.create_project(project))

# the output must be in dictionary format like this
# {'data': {'icon_id': '', 'labels_per_task': 3,
# 'project_id': '61ab262a7057be733d6cc844', 'project_name': 'p12'},
# 'message': 'successful', 'meta': {}}

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# edit project

# project_name = 'p12'
# labels_per_task = 3
# project = Project(project_name, labels_per_task)
# print("edit a project", client.edit_project(project, "61ab262a7057be733d6cc844"))

# the output must be in dictionary format like this
# {'data': {'icon_id': '', 'labels_per_task': 3,
# 'project_id': '61ab262a7057be733d6cc844',
# 'project_name': 'p12'}, 'message': 'successful', 'meta': {}}
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# create task

# project_id = '61ab262a7057be733d6cc844'
# text_tagging_task = Text_Tagging(
#     text="We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more " +
#          "cost-efficient. You’ll be the go-to person for cost analysis and you’ll get to prepare reports to help " +
#          "management make better decisions. To do this job well, we’d like you to be well-versed in data and " +
#          "financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of " +
#          "our efforts to ensure profitability and business success.",
#     all_tags=["data analyst", "financial", "business", "high skill"],
#     preferred_tags=["financial", "business"],
#     question="tags?",
#     callback="google.com")
#
# response = client.create_task(project_id=project_id, task=text_tagging_task)
# print(response)

# the output must be like this
# {
#     "data": {
#         "_id": "61aa49ab877b5c9ebcbd14ea",
#         "callbacks": [
#             "www.google.com"
#         ],
#         "created_at": "Fri, 03 Dec 2021 16:45:31 GMT",
#         "items": [
#             {
#                 "data": {
#                     "text": "We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more cost-efficient. You’ll be the go-to person for cost analysis and you’ll get to prepare reports to help management make better decisions. To do this job well, we’d like you to be well-versed in data and financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of our efforts to ensure profitability and business success."
#                 },
#                 "data-type": "text",
#                 "name": "text",
#                 "type": "data"
#             },
#             {
#                 "label-type": "tagging",
#                 "meta-label": {
#                     "all-tags": [
#                         "data analyst",
#                         "financial",
#                         "business",
#                         "high skill"
#                     ],
#                     "preferred-tags": [
#                         "financial",
#                         "business"
#                     ],
#                     "question": "tags?"
#                 },
#                 "name": "tagging",
#                 "type": "label"
#             }
#         ],
#         "project_id": "61aa477a21a287aae2ab21eb",
#         "status": "pending",
#         "task-type": "text-tagging",
#         "updated_at": "Fri, 03 Dec 2021 16:45:31 GMT"
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# get task

# project_id = '61ab262a7057be733d6cc844'
# task_id = '61ab3252f6a67a28c8910ab4'
# response = client.get_task(project_id, task_id)
# print(response)

# the output must be like this
# {
#     "data": {
#         "_id": "61ab336ef6a67a28c8910ab5",
#         "callbacks": [
#             "www.google.com"
#         ],
#         "created_at": "Sat, 04 Dec 2021 09:22:54 GMT",
#         "items": [
#             {
#                 "data": {
#                     "text": "We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more cost-efficient. You’ll be the go-to person for cost analysis and you’ll get to prepare reports to help management make better decisions. To do this job well, we’d like you to be well-versed in data and financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of our efforts to ensure profitability and business success."
#                 },
#                 "data-type": "text",
#                 "name": "text",
#                 "type": "data"
#             },
#             {
#                 "label-type": "tagging",
#                 "meta-label": {
#                     "all-tags": [
#                         "data analyst",
#                         "financial",
#                         "business",
#                         "high skill"
#                     ],
#                     "preferred-tags": [
#                         "financial",
#                         "business"
#                     ],
#                     "question": "tags?"
#                 },
#                 "name": "tagging",
#                 "type": "label"
#             }
#         ],
#         "project_id": "61a9fb113113c9fb80c1e2c2",
#         "status": "pending",
#         "task-type": "text-tagging",
#         "updated_at": "Sat, 04 Dec 2021 09:22:54 GMT"
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# get all projects

# response = client.get_all_projects()
# print(response)

# output format
# {
#     "data": {
#         "projects": [
#             {
#                 "created_at": "Wed, 01 Dec 2021 10:49:58 GMT",
#                 "project_id": "61a75356bd82060af3f440bc",
#                 "project_name": "p1",
#                 "updated_at": "Wed, 01 Dec 2021 10:49:58 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 13:37:48 GMT",
#                 "project_id": "61a8cc2c50d6f1b9ef9fbc98",
#                 "project_name": "p2",
#                 "updated_at": "Thu, 02 Dec 2021 13:37:48 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 14:29:38 GMT",
#                 "project_id": "61a8d852a67b81621d37e07e",
#                 "project_name": "p3",
#                 "updated_at": "Thu, 02 Dec 2021 14:29:38 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 14:35:53 GMT",
#                 "project_id": "61a8d9c910b4c3820dbe0856",
#                 "project_name": "p4",
#                 "updated_at": "Thu, 02 Dec 2021 14:35:53 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 14:39:33 GMT",
#                 "project_id": "61a8daa5b48b4d276ca5ba9a",
#                 "project_name": "p5",
#                 "updated_at": "Thu, 02 Dec 2021 14:39:33 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 18:07:29 GMT",
#                 "project_id": "61a90b61888f4fe4007b71e2",
#                 "project_name": "p6",
#                 "updated_at": "Thu, 02 Dec 2021 18:07:29 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 18:10:44 GMT",
#                 "project_id": "61a90c24888f4fe4007b71e7",
#                 "project_name": "p8",
#                 "updated_at": "Thu, 02 Dec 2021 18:10:44 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 19:46:49 GMT",
#                 "project_id": "61a922a9e75c83661c0d1616",
#                 "project_name": "p7",
#                 "updated_at": "Thu, 02 Dec 2021 19:46:49 GMT"
#             },
#             {
#                 "created_at": "Thu, 02 Dec 2021 19:47:56 GMT",
#                 "project_id": "61a922ec9e4af6ee3b551a56",
#                 "project_name": "p9",
#                 "updated_at": "Thu, 02 Dec 2021 19:47:56 GMT"
#             },
#             {
#                 "created_at": "Fri, 03 Dec 2021 11:10:09 GMT",
#                 "project_id": "61a9fb113113c9fb80c1e2c2",
#                 "project_name": "p10",
#                 "updated_at": "Fri, 03 Dec 2021 11:10:09 GMT"
#             }
#         ]
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# get all tasks

# status can be one of ['pending','canceled','completed','in_progress']
# pending means it is not labeled yet
# canceled means the task is canceled
# completed means total labels for this task is equal to project labels_per_task feature
# in_progress means the task has at least one label

# project_id = '61ab262a7057be733d6cc844'
# response = client.get_all_tasks(project_id, status='pending')
# print(response)

# output sample
# {
#     "data": {
#         "project_id": "61a9fb113113c9fb80c1e2c2",
#         "tasks": [
#             {
#                 "_id": "61aa01d1e83f5d9314ef848a",
#                 "created_at": "Fri, 03 Dec 2021 11:38:57 GMT",
#                 "labelers": [
#                     "617b069e392d18749522bc26"
#                 ],
#                 "status": "pending",
#                 "task-type": "text-tagging",
#                 "total_labels": 1,
#                 "updated_at": "Fri, 03 Dec 2021 11:38:57 GMT"
#             },
#             {
#                 "_id": "61ab336ef6a67a28c8910ab5",
#                 "created_at": "Sat, 04 Dec 2021 09:22:54 GMT",
#                 "labelers": [],
#                 "status": "pending",
#                 "task-type": "text-tagging",
#                 "total_labels": 0,
#                 "updated_at": "Sat, 04 Dec 2021 09:22:54 GMT"
#             }
#         ]
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# get project

# project_id = '61ab262a7057be733d6cc844'
# response = client.get_project(project_id)
# print(response)

# output sample
# {
#     "data": {
#         "created_at": "Thu, 02 Dec 2021 19:47:56 GMT",
#         "icon_id": "61a9256ac50da0ed872e2178",
#         "labels_per_task": 4,
#         "project_id": "61a922ec9e4af6ee3b551a56",
#         "project_name": "p9",
#         "stat": {
#             "labelers": {
#                 "active_labelers": [
#                     "ari@gmail.com",
#                     "amir@test.com"
#                 ],
#                 "deactivated_labelers": []
#             },
#             "total_complete_tasks": 0,
#             "total_labels": 0,
#             "total_tasks": 0,
#             "total_tasks_labeled": 0
#         },
#         "updated_at": "Thu, 02 Dec 2021 19:47:56 GMT"
#     },
#     "message": "successful",
#     "meta": {}
# }

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# count tasks

# project_id = '61ab262a7057be733d6cc844'
# response = client.get_tasks_count(project_id, status='pending')
# print(response)
# output sample
# {'data': {'count': 1}, 'message': 'successful', 'meta': {}}
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# cancel tasks

# project_id = '61ab262a7057be733d6cc844'
# task_id = '61ab3252f6a67a28c8910ab4'
# response = client.cancel_task(project_id, task_id=task_id)
# print(response)

# output sample
# {
#     "data": {
#         "_id": "61aa01d1e83f5d9314ef848a",
#         "callbacks": [
#             "www.google.com"
#         ],
#         "created_at": "Fri, 03 Dec 2021 11:38:57 GMT",
#         "items": [
#             {
#                 "data": {
#                     "text": "We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more cost-efficient. You’ll be the go-to person for cost analysis and you’ll get to prepare reports to help management make better decisions. To do this job well, we’d like you to be well-versed in data and financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of our efforts to ensure profitability and business success."
#                 },
#                 "data-type": "text",
#                 "name": "text",
#                 "type": "data"
#             },
#             {
#                 "label-type": "tagging",
#                 "meta-label": {
#                     "all-tags": [
#                         "data analyst",
#                         "financial",
#                         "business",
#                         "high skill"
#                     ],
#                     "preferred-tags": [
#                         "financial",
#                         "business"
#                     ],
#                     "question": "tags?"
#                 },
#                 "name": "tagging",
#                 "type": "label"
#             }
#         ],
#         "project_id": "61a9fb113113c9fb80c1e2c2",
#         "status": "canceled",
#         "task-type": "text-tagging",
#         "updated_at": "Fri, 03 Dec 2021 11:38:57 GMT"
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# add labelers

# project_id = '61ab262a7057be733d6cc844'
# response = client.add_labelers(project_id, ['ras@gmail.com', 'amir@test.com'])
# print(response)

# output sample
# {
#     "data": {
#         "active_labelers": [
#             "ari@gmail.com",
#             "amir@test.com"
#         ],
#         "deactivated_labelers": [],
#         "project_id": "61aa477a21a287aae2ab21eb",
#         "token": "bf76eefd-8423-49e9-b63d-0f14bb615324"
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# add cancel labeler

project_id = '61ab262a7057be733d6cc844'
response = client.cancel_labeler(project_id, 'amir@test.com')
print(response)

# output sample
# {
#     "data": {
#         "active_labelers": [
#             "ari@gmail.com"
#         ],
#         "deactivated_labelers": [
#             "amir@test.com"
#         ],
#         "project_id": "61a9fb113113c9fb80c1e2c2",
#         "token": "e2fcd22b-4c71-4c37-a140-39835933edbe"
#     },
#     "message": "successful",
#     "meta": {}
# }
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# get all labelers

project_id = '61ab262a7057be733d6cc844'
response = client.all_labelers(project_id)
print(response)

# output sample
# {
#     "data": {
#         "active_labelers": [
#             "ari@gmail.com"
#         ],
#         "deactivated_labelers": [
#             "amir@test.com"
#         ],
#         "project_id": "61a9fb113113c9fb80c1e2c2",
#         "token": "e2fcd22b-4c71-4c37-a140-39835933edbe"
#     },
#     "message": "successful",
#     "meta": {}
# }