# TimeSheetManagement
TimeSheetManagement webapp for python training
Before starting the AWS training I decided to restart the project to correct the structure.

As of 02/21 I have almost finished the time sheet part, and am also working on the reports.
I got stuck pretty hard while working on the project during the AWS training because I wanted to force the user to create a profile at the same time as creating an auth_user.
I figured that out and finally got to move on to core functionality, which is what I've been working on over the weekend.

I will be finished with the plan I made for the project soon. Thank you for your patience.

Great Progress! Few points to consider -
1. Urls - Try to keep them seperate on app basis. Project level urls will do but program modularity is not achieved
2. Models - Here instead of maintaining hospitals data in program (which is fine now since we have only a few), it will be a good architecture if we create the new model for it and maintain it at DB layer, increasing the scope for future enhancements.
3. def time_sheet_view(), def delete_view() - All we are doing here is what generic view would do. To pass extra context data along with the queryset o/p, we can use the attribute called extra_context_data. Sign_up() view looks fine.
4. Same for Logout_view() as well. The redirect can be set in settings.py. 
-Kanchan 02/22
