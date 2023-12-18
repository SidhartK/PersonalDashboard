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
custom_field_settings_api_instance = asana.CustomFieldSettingsApi(api_client)
project_gid = "1204994036429250" # str | Globally unique identifier for the project.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    # 'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "custom_field,custom_field.asana_created_field,custom_field.created_by,custom_field.created_by.name,custom_field.currency_code,custom_field.custom_label,custom_field.custom_label_position,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.description,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.format,custom_field.has_notifications_enabled,custom_field.is_formula_field,custom_field.is_global_to_workspace,custom_field.is_value_read_only,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.people_value,custom_field.people_value.name,custom_field.precision,custom_field.resource_subtype,custom_field.text_value,custom_field.type,is_important,offset,parent,parent.name,path,project,project.name,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project's custom fields
    api_response = custom_field_settings_api_instance.get_custom_field_settings_for_project(project_gid, opts)
    all_data = [data for data in api_response]
    import pdb; pdb.set_trace()
    # for data in api_response:
    #     pprint(data)
except ApiException as e:
    print("Exception when calling CustomFieldSettingsApi->get_custom_field_settings_for_project: %s\n" % e)