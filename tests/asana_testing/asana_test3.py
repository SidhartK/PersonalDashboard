import asana
from asana.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

configuration = asana.Configuration()
configuration.access_token = os.getenv("ASANA_ACCESS_TOKEN")
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {
    'opt_fields': "email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,workspaces,workspaces.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a user
    api_response = users_api_instance.get_user(user_gid, opts)
    import pdb; pdb.set_trace()
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)