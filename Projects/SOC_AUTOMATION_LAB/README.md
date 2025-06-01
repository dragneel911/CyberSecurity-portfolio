## Make sure to check the 'Prerequisites.md' 
## This is the day 1 that i am working on this project
first we have to draw a diagram to map out how we want to build our lab 
I use draw.io to create a diagram to understand it logically and visually. This will help you to better know how the things that done by you is related to your home lab.

We use Wazuh Manager which is the central server component of the Wazuh security platform, responsible for managing and analyzing security data from Wazuh agents deployed on various systems. It collects, analyzes, and stores data from agents, and triggers alerts when security events match defined rules

https://documentation.wazuh.com/current/user-manual/manager/wazuh-manager.html

Installation guide Provided:-

https://documentation.wazuh.com/current/deployment-options/deploying-with-ansible/guide/install-wazuh-manager.html

Shuffle Automation SOAR(Security Orchestartion Automation Response) is a free open-source automation tool that helps us to build this SOC automation lab and enrich the alerts that have been passing through it.

It Goes as follows:-

🛡️ SOC Automation Setup
This project illustrates a Security Operations Center (SOC) automation workflow designed to streamline event monitoring, alerting, enrichment, and automated response actions.

📌 Project Overview
The SOC automation setup integrates various components to detect, analyze, and respond to security events in real-time. It includes a flow that starts from event generation on endpoints and moves through event collection, analysis, enrichment of Indicators of Compromise (IOCs), alerting, and automated response execution.

🔄 Workflow Description
Send Events: Endpoints (workstations/servers) generate security events and forward them to the SIEM system.

Receive Events: SIEM collects and stores incoming events from all sources.

Send Alerts: Based on predefined rules, SIEM generates alerts for suspicious events.

Enrich IOCs: The alert data is sent to a threat intelligence platform for IOC enrichment.

Send Alerts: Enriched IOCs and contextual alerts are pushed to an orchestration tool.

Send Email: Notifications are sent to SOC analysts via email.

Send and Receive Email: Analysts receive alerts and can take actions via email or dashboard.

Send Response Action: Automated response actions are sent back from the orchestration tool to the relevant endpoint.

Perform Response Action: The endpoint executes the response (e.g., isolate host, kill process, block IP).

⚙️ Tools Used
SIEM (Security Information and Event Management)

SOAR (Security Orchestration, Automation, and Response)

Threat Intelligence Platform

Email Server

Endpoints/Workstations

✅ Use Case
This setup is ideal for:

Real-time threat detection and response

Reducing mean time to detect (MTTD) and respond (MTTR)

Enhancing SOC efficiency through automation


## This is day 2 of my working on this project
Today I am going to install the required tools and configure my vm.
These are the main steps i have done today:-

=>Installing *Sysmon* on a Windows 10 virtual machine to capture detailed system activity logs

Installation Process:-

First go to your virtual machine(VM) and go to the website link i am about to give 
"https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon"-- Download the sysmon.zip file and extract it.Go to the github link and save the configuration .xml file of the sysmon. 
https://github.com/olafhartong/sysmon-modular/blob/master/sysmonconfig.xml

clone it or download it raw do whatever you want but you need the file.

Now go to the powershell with administrator and locate to the sysmon folder where we unzipped it and save the config file in the unzipped folder and press cd to locate to that folder

After that you have to type in this command to install the sysmon with the downloaded .xml configuration file. 

command:-

.\Sysmon64.exe -i .\sysmonconfig.xml 

After installing check the services by clicking on windows button and go to services and find the sysmon64 to check whether if it is installed or not.

