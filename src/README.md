# Summary

This is the /src/ folder for discord webhooks. These can later be expanded to cover interactive discord apps, etc.

Feature Rollout plan, not necesarily in order

Prod env of incoming notifications on Raspberry Pi - User Facing
Gamma env of incoming notifications on Raspberry Pi - Internal
Deployment scripts for stages - Internal
Better separation of Prod and non-Prod envs
Containerization of runtime environments
Notifications on offensive military activity
Notifications on offensive military activity if adjacent to non-origin town
Notifications on offensive sieges
Email notifications for incoming
Text notifications for incoming
Logging of activities
Ticketing in case of failures
Frontend for user settings

## Customization

If you want to use this yourself, the state/database is currently being stored inside AWS DynamoDB. The access class for that is in `/src/aws/illyriad_db_dao.py`, and it is initialized inside `/src/dagger/aws_module.py`. Run your own version of that file, if youre using your own AWS account, or local db instance.

## Links

* https://pypi.org/project/boto3-stubs/
  * boto3 stubs
* 