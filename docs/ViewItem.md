# ViewItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content of the view. | [optional] 
**name** | **str** | Name of the view item. In the case of code view, it would be the notebook’s name. In the case of dashboard view, it would be the dashboard’s name. | [optional] 
**type** | [**ViewType**](ViewType.md) |  | [optional] 

## Example

```python
from databricks_jobs.models.view_item import ViewItem

# TODO update the JSON string below
json = "{}"
# create an instance of ViewItem from a JSON string
view_item_instance = ViewItem.from_json(json)
# print the JSON string representation of the object
print ViewItem.to_json()

# convert the object into a dict
view_item_dict = view_item_instance.to_dict()
# create an instance of ViewItem from a dict
view_item_form_dict = view_item.from_dict(view_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


