---
title: "How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors"
collection_source: "Federal Bureau of Investigation"
collection_url: https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors
final_url: https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors
collection_domain: fbi.gov
collection_date: 2026-04-25
publish_date: 2024-05-29
language: en
status: collected
text_status: parsed
fetcher: urllib
http_status: 200
content_type: "text/html;charset=utf-8"
content_hash: sha256:d4250a3cc17a4323e63dbec3585630cb53248564563a5ca422bbcc2cc78349df
word_count: 1002
extraction_date: 2026-04-25
source_page: wiki/sources/2024-05-29_fbi-gov_how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors.md
---
## Summary

Source text harvested from https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors.

## Extracted Text

How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors — FBI

A .gov website belongs to an official government organization in the United States.

A lock ( ) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

Search

FBI

More

Most Wanted

News

What We Investigate

How We Can Help You

Submit a Tip

About

Contact Us

Cyber

Search FBI

FBI Federal

Bureau of Investigation

How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors

Terrorism

Counterintelligence and Espionage

Public Corruption

Civil Rights

Transnational Organized Crime

White-Collar Crime

Violent Crime

Environmental Crime

Weapons of Mass Destruction

How We Investigate

Partners

Cyber Alerts

SEC Reporting Requirements

How to Identify and Remove VPN Applications That Contain 911 S5 Back Doors

The FBI, the Defense Criminal Investigative Service, and the Department of Commerce's Office of Export Enforcement have published a public service announcement (the “PSA”) for individuals and businesses to better understand and guard against the 911 S5 residential proxy service and botnet. The PSA is available at ic3.gov/Media/Y2024/PSA240529 .

As explained in the PSA, 911 S5 began operating in May 2014 and was taken offline by the administrator in July 2022 before reconstituting as Cloudrouter in October 2023. 911 S5 was likely the largest residential proxy service and botnet with over 19 million compromised IP addresses in over 190 countries and confirmed victim losses in the billions of dollars.

Free, illegitimate VPN applications that were created to connect to the 911 S5 service are: MaskVPN, DewVPN, PaladinVPN, ProxyGate, ShieldVPN, and ShineVPN.

Unaware of the proxy backdoor, once users downloaded these VPN applications, they unknowingly became a victim of the 911 S5 botnet. The proxy backdoor enabled 911 S5 users to re-route their devices through victims’ devices, allowing criminals to carry out crimes such as bomb threats, financial fraud, identity theft, child exploitation, and initial access brokering. By using a proxy backdoor, criminals made nefarious activity appear as though it was coming from the victims’ devices.

The below information is intended to help identify and remove 911 S5’s VPN applications from devices or machines.

Before electing to use this information, users may want to consult with legal counsel and cybersecurity professionals, potentially including an incident response firm if they deem necessary, to explore all options and assist with any remediation efforts to avoid further harm by malicious software applications or botnets. The FBI makes no warranties or representations regarding the efficacy of this information.

Check for Running Services

1. Press Control+Alt+Delete on the keyboard and select the “Task Manager” option or right-click on the Start menu (Windows icon) and select the "Task Manager" option.

2. Task Manager should now be running. Under the "Process" tab, look for the following:

MaskVPN (mask_svc.exe)

DewVPN (dew_svc.exe)

PaladinVPN (pldsvc.exe)

ProxyGate (proxygate.exe, cloud.exe)

ShieldVPN (shieldsvc.exe)

ShineVPN (shsvc.exe)

Example of running processes for ShieldVPN and ShieldVPN Svc:

If Task Manager doesn't detect any of these services, verify that by searching the Start menu for any traces of software labeled as "MaskVPN," "DewVPN," "ShieldVPN," "PaladinVPN," "ProxyGate," or "ShineVPN."

3. Click on the "Start" (Windows Icon) button typically found in the lower lefthand corner of the screen. Then, search for the following terms, which are the identified names of the malicious software applications:

MaskVPN

DewVPN

ShieldVPN

PaladinVPN

ShineVPN

ProxyGate

4. If one of the VPN applications is found, an uninstaller is sometimes located under the Start menu option of the VPN application. The example image below shows an instance where the uninstall option isn't available.

5. If the application doesn't contain an uninstall option, then follow the steps below to attempt to uninstall the application:

Click on the Start menu (Windows button) and type “Add or remove programs” to bring up the "Add and Remove Programs" menu.

Search for the malicious software application names.

An example image below shows the ShieldVPN application found within the “Add or remove programs” application list. Once you find the application in the list, click on the application name and select the “Uninstall” option.

After the application is uninstalled, you can try to verify that the application has been removed by clicking on "Start" (Windows Icon) and typing “File Explorer."

Click on the drive letter “C:”—sometimes labeled as “Windows (C:)”—and navigate to "Program Files(x86)." Then, look for the malicious software application names in the list of files and folders.

For ProxyGate, navigate to "C:\users\[Userprofile]\AppData\Roaming\ProxyGate."

If you don't see any folder labeled "MaskVPN," "DewVPN," "ShineVPN," "ShieldVPN," "PaladinVPN," or "Proxygate,"

then this particular malicious software application may not be installed.

If a service was found running, but not found under the Start menu or "Add and Remove Programs," then:

Navigate to the directories described in directions 5d and 5e.

Open “Task Manager."

Select the service related to one of the identified malicious software applications running in the process tab.

Select the option “End task” to attempt to stop the process from running.

Right-click on the folder named “MaskVPN,” “DewVPN,” “ShineVPN,” “ShieldVPN,” “PaladinVPN,” or "ProxyGate."

Select the “Delete” option.

You can also select all files found within the folder and then select the “Delete” option.

If you try to delete the folder—or to delete all files located inside the folder—and receive an error message, be sure that you've ended all processes related to the malicious software within in Windows Task Manager, as described in step 5g.

Ten Most Wanted

Fugitives

Kidnappings / Missing Persons

Seeking Information

Bank Robbers

ECAP

ViCAP

FBI Jobs

Crime Statistics

History

FOIPA

Scams & Safety

FBI Kids

Stories

Videos

Press Releases

Speeches and Testimony

Podcasts and Radio

Photos

Español

Apps

Law Enforcement

Victims

Parents and Caregivers

Students

Businesses

Safety Resources

Need an FBI Service or More Information?

Counterintelligence

Cyber Crime

Organized Crime

WMD

Mission & Priorities

Leadership & Structure

Partnerships

Community Outreach

FAQs

Field Offices

FBI Headquarters

Visit the FBI Experience

Overseas Offices

Additional Resources

Accessibility

eRulemaking

Freedom of Information / Privacy Act

Legal Notices

Legal Policies & Disclaimers

## Extraction Notes

- parser: document
- fetcher: urllib
- fetched_at: 2026-04-25T14:17:33+00:00
- final_url: https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors
