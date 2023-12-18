import asana
from asana.rest import ApiException
from pprint import pprint
import os

configuration = asana.Configuration()
configuration.access_token = os.getenv("ASANA_ACCESS_TOKEN")
api_client = asana.ApiClient(configuration)

# create an instance of the API class
user_task_lists_api_instance = asana.UserTaskListsApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
workspace = "1204994054943927" # str | The workspace in which to get the user task list.
opts = {
    'opt_fields': "name,owner,workspace", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a user's task list
    api_response = user_task_lists_api_instance.get_user_task_list_for_user(user_gid, workspace, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTaskListsApi->get_user_task_list_for_user: %s\n" % e)