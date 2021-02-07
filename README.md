<h2>COVID DATA CHALLENGE</h2>

<h3><ins><b>Project includes:</b></ins></h3>
    <ol>
    <li><b>Source code</b></li>
    <li><b>Tests</b></li>
    <li><b>ImportCovidDataTaskExecutable</b>, which is a Python Script converted executable to run the Data Ingestion Job (Only for Linux and Unix Env's) </li>
    <li><b>scheduleCron.py</b>, which is a Python script which schedules the execution of this task either from Executable or the main source python script </li>
    <li><b>requirements.txt</b> a file which contains all the dependencies required for this project </li>
    </ol>

----

<h3><ins><b>Use case 1 - For Linux/Unix Environment (To run the task only once)</b></ins></h3>
     Locate to the project directory from the terminal and execute the following command:
     (When running for the first time, you may have to provide it with the right permissions from your system settings which says "allow the execution from unidentified developers" to avoid permission issues.)
     
     
     ./ImportCovidDataTaskExecutable
     
----
<h3><ins><b>Use case 2 -  To schedule the task to run as Cron Job</ins></b></h3>
    <h4>For Linux/Unix Env</h4>
        <b><ul><ins>Installing and creating a Virtual Environment and activating it for the project </ins></ul></b>
        <ol>
            <li>Locate to the project directory and make sure pip is installed on your machine</li>
            <li>Run the command "pip install virtualenv"</li>
            <li>Run the command "virtualenv venv", which should create a folder in the project directory called 'venv'</li>
            <li>Navigate to this folder from terminal and run the command "source activate" or just "./activate.sh" for Windows Users</li>
            <li>The virtual environment is now active! </li>
         </ol>
         <br><br>
        <b><ul><ins> Install the dependencies: </ins></b></ul>
         <ol>
            <li>Locate to the project directory and make sure pip is installed on your machine</li>
            <li>Run the command "pip install --upgrade -r requirements.txt"   (Wait till this installs all the dependencies required for the project)</li>
         </ol>
        <br><br>
        <b><ul><ins> Running the script which creates a Cron job: </ins></b></ul>
         <ol>
            <li>Locate to the project directory from the terminal and run the command "python scheduleCron.py"  (If to use executable instead of Script, please open the scheduleCron.py file and uncomment the 2 lines below "For Unix/Linux Environments" and comment the 3 lines below "For any Environments" and run the command given above)</li>
            <li>Make sure you allow any permission pop-ups related to Crontab</li>
            <li>Verify that the CronJob has been scheduled using command "crontab -l", and you can see the command which is scheduled to run.</li>
         </ol>
    <br><br>
    <h4>For Windows users:</h4>
    
    
    The first two steps: Installing and Creating of Virtuenv and activating it, and the Installing the dependencies remain the same given in the Linux/Unix Env. 
    
    Create a .bat file with any name For ex: ImportDataTask.bat and add the following command to it:</li>
    
    <path_to_venv_bin_folder_in_project>/python <path_to_source_folder_in_project>/importDataTask.py
    
    Open WindowsTaskScheduler and create a task which runs everyday at 9:00 am, and use the above created .bat file to use as the Program/Script
    
    
----
<h3><ins><b>Run Tests</ins></b></h3>
  <ol>
     <li>Make sure the virtualenv is activated and all the dependencies have been installed.</li>
     <li>Navigate to the 'tests' directory in the project from your terminal and run the following command</li>
   </ol>      
     
     
    pytest -v
         
    
