
Mlcheap
API
18th November 2021
OVERVIEW
By mlcheap api you can upload your data, annotate them with high quality, check quality of labels, train model, and release your model. 
INSTALLATION
Install sdk
pip3 install MlCheap==0.1.4

Api
Create project
bash
curl --location --request POST 'api.unbiased.com/v1/create-project' \
--header 'token: {your_token}' \
--header 'Content-Type: application/json' \
--data-raw '{"project_name":"{your_project_name}", "labels_per_task":{your_labels_per_task}}'

Python sdk
from Client import Client
from Project import Project


client = Client(your_api_key)
project = Project(project_name, labels_per_task)
client.create_project(project)

 
Get project
bash
curl --location --request GET 'api.unbiased.com/v1/project' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}'

Python sdk
project = client.get_project(project_name)

 
 
Get all projects
bash
curl --location --request GET 'api.unbiased.com/v1/all-projects' \
--header 'token: {your_token}'

Python sdk
all_projects = client.get_all_projects()

 
 
Create task
bash
curl --location --request POST 'api.unbiased.com/v1/create-task' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "task-type": "text-tagging",
    "callback": "www.google.com",
    "data": {
        "text": "We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more cost-efficient. You'll be the go-to person for cost analysis and you'll get to prepare reports to help management make better decisions. To do this job well, we'd like you to be well-versed in data and financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of our efforts to ensure profitability and business success."
    },
    "meta-label": {
        "question": "tags?",
        "all-tags": ["data analyst","financial", "business","high skill"]
    }
}'

Python sdk
text_tagging_task = Text_Tagging(
   text="We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more " +
        "cost-efficient. You'll be the go-to person for cost analysis and you'll get to prepare reports to help " +
        "management make better decisions. To do this job well, we'd like you to be well-versed in data and " +
        "financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of " +
        "our efforts to ensure profitability and business success.",
   all_tags=["data analyst", "financial", "business", "high skill"],
   question="tags?",
   callback="google.com")

client.create_task(project_name, text_tagging_task)

 
Get task
bash
curl --location -g --request GET 'api.unbiased.com/v1/task?task_id={{api.task_id}}' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}'

Python sdk
task = client.get_task(project_name, task_id)

 
 
 
Get all tasks
bash
curl --location --request GET 'api.unbiased.com/v1/tasks?status=pending' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}'

Python sdk
all_tasks = client.get_all_tasks(project_name, {})

 
 
Count all tasks
bash
curl --location --request GET 'api.unbiased.com/v1/tasks-count?status=pending' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}'

Python sdk
count_tasks = client.get_tasks_count(project_name, {})

 
 
Cancel task
bash
curl --location --request DELETE 'api.unbiased.com/cancel-task?task_id={the_task_id}' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}'

Python sdk
client.cancel_task(project_name, task_id)

 
 

Add labelers
bash
curl --location --request POST 'api.unbiased.com/v1/add-labelers' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "emails": ["ari@gmail.com"]
}'

Python sdk
client.add_labelers(project_name, ['ras@gmail.com', 'ame@yahoo.com'])

 
 
All labelers
bash
curl --location --request GET 'api.unbiased.com/v1/all-labelers' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}' \
--header 'Content-Type: application/json'

Python sdk
client.all_labelers(project_name)

 
 
Cancel labeler
bash
curl --location --request DELETE 'api.unbiased.com/v1/cancel-labeler?email=maj@gmail.com' \
--header 'token: {your_token}' \
--header 'project_name: {your_project_name}' \
--header 'Content-Type: application/json'

Python sdk
client.cancel_labeler(project_name, 'ras@gmail.com')

 
