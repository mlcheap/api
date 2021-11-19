# from Client import Client
# from Project import Project
# from Task import Text_Tagging
#
# LABELER_TEST_API = 'bf76eefd-8423-49e9-b63d-0f14bb615324'
# project_name = 'p4'
# labels_per_task = 3
#
# client = Client(LABELER_TEST_API)
# project = Project(project_name, labels_per_task)
# client.create_project(project)
#
# text_tagging_task = Text_Tagging(
#     text="We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more " +
#          "cost-efficient. You’ll be the go-to person for cost analysis and you’ll get to prepare reports to help " +
#          "management make better decisions. To do this job well, we’d like you to be well-versed in data and " +
#          "financial analysis, and have strong attention to detail. Ultimately, your job will be an integral part of " +
#          "our efforts to ensure profitability and business success.",
#     all_tags=["data analyst", "financial", "business", "high skill"],
#     question="tags?",
#     callback="google.com")
# #
# client.create_task(project_name, text_tagging_task)
#
# all_projects = client.get_all_projects()
#
# project = client.get_project(project_name)
#
# all_tasks = client.get_all_tasks(project_name, {})
#
# count_tasks = client.get_tasks_count(project_name, {})
#
# task_id = all_tasks['tasks'][0]['_id']
# task = client.get_task(project_name, task_id)
#
#
# client.get_all_tasks(project_name, {})
#
# client.cancel_task(project_name, task_id)
# client.get_all_tasks(project_name, {})
#
# client.all_labelers(project_name)
#
# client.add_labelers(project_name, ['ras@gmail.com', 'ame@yahoo.com'])
# client.all_labelers(project_name)
# client.cancel_labeler(project_name, 'ras@gmail.com')
# client.all_labelers(project_name)
