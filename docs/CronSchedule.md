# CronSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quartz_cron_expression** | **str** | A Cron expression using Quartz syntax that describes the schedule for a job. See [Cron Trigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) for details. This field is required. | 
**timezone_id** | **str** | A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See [Java TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html) for details. This field is required. | 
**pause_status** | **str** | Indicate whether this schedule is paused or not. | [optional] 

## Example

```python
from databricks_jobs.models.cron_schedule import CronSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CronSchedule from a JSON string
cron_schedule_instance = CronSchedule.from_json(json)
# print the JSON string representation of the object
print CronSchedule.to_json()

# convert the object into a dict
cron_schedule_dict = cron_schedule_instance.to_dict()
# create an instance of CronSchedule from a dict
cron_schedule_form_dict = cron_schedule.from_dict(cron_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


