### Robotic Process Automation (RPA)

This project automates the process of verifying email inboxes, downloading files, and comparing ratings from different sources, using the Dispatcher-Performer model in UiPath.

- **Project Description:**
  - **Dispatcher Component:** The robot acts as a dispatcher by checking the Outlook inbox for unread emails with the subject "Rating Relevance on Stailer." It downloads the input file (Excel) containing location and service category information from the Stailer platform and uploads the data to an Orchestrator queue.
  - **Performer Component:** The performer robot retrieves data from the Orchestrator queue. It processes each item by extracting the top 10 salons from the Stailer platform for the specified location and category, retrieves their rating grades, and compares these with the ratings found on Google Maps.
  - **Output:** The result is an Excel document with a sheet for each location + service category pair, containing columns for the Salon Name, Stailer Rating Grade, Google Rating Grade, and a column indicating if the Stailer rating is relevant (difference <0.4).
  - The output file is uploaded to Google Drive.

- **Technologies Used:**
  - UiPath for automation (utilizing Dispatcher and Performer patterns)
  - UiPath Orchestrator for queue management
  - Microsoft Outlook
  - Microsoft Excel
  - Google Maps
  - Google Drive 

- **Key Automations:**
  - Email Inbox Monitoring
  - Excel File Processing
  - Data Extraction and Rating Comparison
  - Excel File Generation
  - File Upload to Google Drive

---
