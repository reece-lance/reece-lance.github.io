# Team Exercise: Database Design Project for Transport for London (TfL)

## Overview

This team project involved designing a logical database for Transport for London (TfL). Our goal was to create a robust and efficient database solution to manage large volumes of transport data. The project required collaboration on database design, data management pipeline creation, and critical evaluation of the selected database management system (DBMS). The team's task was to deliver a comprehensive report that met the client's needs, adhered to best practices in database design, and demonstrated an understanding of data management principles.

### My Role and Contributions

- **Communication and Coordination:** Initiated communication through WhatsApp and forum threads to ensure clear, consistent updates and collaboration. This approach helped prevent miscommunications and ensured all team members were aligned on the project objectives and deadlines.
- **Task Assignment and Planning:** Created a detailed project plan and assigned tasks based on team members' strengths and availability. This strategy optimised workflow and helped meet deadlines efficiently.
- **Data Management Pipeline Development:** Led the design and implementation of a data management pipeline using Python. This included:
  - **Data Retrieval:** Developed Python scripts to access TfL's API, retrieve data in various formats (JSON, ZIP), and save it locally for further processing.
  - **Data Cleaning:** Implemented data cleaning techniques, such as handling missing values and removing duplicates, using Python libraries (e.g., `pandas`).
  - **Data Preparation for Database Loading:** Structured the cleaned data to be compatible with the chosen DBMS format, including normalising data to reduce redundancy.

### Specific Examples of My Work

#### 1. Data Retrieval and Processing Script

To automate data retrieval from TfL's API, I developed a Python script that fetches data from multiple endpoints, handles different file types (e.g., JSON, ZIP), and stores them in the appropriate directory for further processing:

```python
import requests
import zipfile
import io
import os

def fetch_and_process_data(url, files_list):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            file_name = url.split('/')[-1]
            base_name, file_extension = os.path.splitext(file_name)
            directory_name = base_name.replace('.', '_')
            raw_data_path = os.path.join("..", "data", "raw", directory_name)
            os.makedirs(raw_data_path, exist_ok=True)

            if 'zip' in content_type or file_extension == '.zip':
                with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                    for file_info in zip_file.infolist():
                        zip_file.extract(file_info, raw_data_path)
                        extracted_file_path = os.path.join(raw_data_path, file_info.filename)
                        files_list.append(extracted_file_path)
                print(f"Data downloaded and extracted successfully to {raw_data_path}.")
            else:
                file_path = os.path.join(raw_data_path, file_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                files_list.append(file_path)
                print(f"Data downloaded successfully and saved as {file_path}.")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            
        return files_list

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

# List of endpoints and processing loop
URL_NAME = "https://api.tfl.gov.uk"
endpoints = ["/stationdata/tfl-stationdata-detailed.zip", "/Line/Route", "/Vehicle/{ids}/Arrivals"]
files_list = []
for endpoint in endpoints:
    files_list = fetch_and_process_data(URL_NAME + endpoint, files_list)
```

2. Data Cleaning and Preparation
After retrieving the data, I implemented data cleaning procedures to handle missing values and remove duplicates:

```python
Copy code
import pandas as pd

df = pd.read_json('raw_data.json')
df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill method
df.to_csv('cleaned_data.csv', index=False)
print("Data cleaning completed and saved as cleaned_data.csv.")
```

### Key Outcomes

- **Effective Collaboration:** Established strong communication channels, ensuring all team members were informed, and tasks were coordinated efficiently. This resulted in meeting deadlines and maintaining a consistent workflow.
- **Logical Database Design:** Successfully designed a logical database featuring multiple tables, such as 'Stations', 'Routes', 'Vehicles', and 'Schedules', each representing key entities relevant to TfL operations. The design incorporated normalization techniques to minimize redundancy and maintain data integrity.
- **Data Pipeline Implementation:** The developed data pipeline efficiently retrieved, cleaned, and formatted data, enabling seamless integration into the chosen DBMS. This was achieved using Python, with the pipeline scripts automating data handling processes.
- **Enhanced Technical Skills:** Gained experience with API integration, data cleaning using Python libraries, and collaborative project management.

### Challenges Faced and Solutions

1. **Interoperability Issues Between Tools:**
   - *Challenge:* Encountered difficulties integrating data from various sources due to differences in formats (e.g., JSON, CSV).
   - *Solution:* Used Python’s pandas library to standardize the data formats and ensure compatibility with the database schema.

2. **Time Management Constraints:**
   - *Challenge:* Coordinating tasks with team members who had varying availability and skill levels.
   - *Solution:* Created a detailed project plan with milestones, enabling the team to track progress and adjust workloads as needed.

3. **Feedback on Report Content:**
   - *Challenge:* The report feedback indicated a need for more depth in logical design and clearer explanations in the data management pipeline.
   - *Solution:* Plan to incorporate more detailed descriptions and diagrams in future reports and ensure a tighter focus on the core requirements by continuously aligning with assignment guidelines.

### Feedback and Reflection

#### Feedback Received:
- **Strengths:**
  - The report demonstrated a good understanding of module topics and practical application.
  - Effective descriptions of data availability, user requirements, and a structured report format.
- **Areas for Improvement:**
  - More depth was needed in describing the logical design, particularly the ER diagrams.
  - The data management pipeline section required further elaboration and a clearer focus on essential elements.

#### Reflection:

Based on the feedback, I realised the importance of providing more detailed explanations and visual aids, such as ER diagrams, to convey the logical design more effectively. Additionally, I learned that adhering strictly to assignment requirements and avoiding unnecessary sections can strengthen the clarity and impact of a report.

**Key Learnings:**
- **Depth and Detail Matter:** Providing thorough explanations and visual aids (e.g., diagrams) can significantly improve the understanding of complex topics.
- **Clear Focus on Requirements:** It is essential to focus only on the required elements of the assignment to avoid diluting the report's effectiveness.
- **Importance of Team Dynamics:** Effective communication and task management are critical to the success of any team project, especially in a virtual environment.

**Future Application:**
I will apply these lessons by enhancing my technical documentation skills, focusing more on visual aids, and continuing to improve my ability to lead and coordinate team projects effectively.

### Conclusion

This project was a valuable learning experience in database design, data management, and teamwork. It equipped me with essential skills for future professional roles in data science and reinforced the importance of clear communication, detailed analysis, and a focus on core requirements.
