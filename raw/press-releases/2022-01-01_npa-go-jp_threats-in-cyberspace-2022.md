---
title: "Threats in Cyberspace 2022"
collection_source: "Japan NPA"
collection_url: https://www.npa.go.jp/english/bureau/cyber/document/threatsincyberspace2022.pdf
collection_domain: npa.go.jp
collection_date: 2026-04-17
publish_date: 2022-01-01
language: en
status: collected
final_url: https://www.npa.go.jp/english/bureau/cyber/document/threatsincyberspace2022.pdf
text_status: parsed
fetcher: jina
http_status: 200
content_type: "text/plain; charset=utf-8"
content_hash: sha256:1982247aed8c4ffbb6b429c6dc84fd70d1c95d8e583de9d88db2ddb9abb4dc6c
word_count: 1197
extraction_date: 2026-04-29
source_page: wiki/sources/2022-01-01_npa-go-jp_threats-in-cyberspace-2022.md
parser: jina_markdown
---
## Summary

The Cyber Affairs Bureau (サイバー警察局, Saibā keisatsu-kyoku) of Japan's National Police Agency (警察庁, Keisatsu-chō) was established on **1 April 2022** by restructuring the Info-Communications Bureau and integrating cyber-related divisions from several other NPA bureaus. It is now the central policing authority for cyberspace in Japan, with direct jurisdiction for the first time (historically, NPA coordinated rather than directly investigated).

## Extracted Text

２ Threats in Cyberspace

(1) Monitoring vulnerability scanning in the cyberspace

A) Unexpected connection attempts

The NPA sets up sensors on the internet to g ather communication

packets sent to the sensors. As these sensors do not provide any

services, they usually do not receive external communication packets

except for the observable ones sent indiscriminately to the unspecified

number of IP addresses by cybe rattackers to search for potential targets.

Analysis of these communication packets facilitates understanding of the

phenomena taking place on the internet e.g., vulnerability scanning of the

connected devices, consequent attacks, and behaviors of the

malw are -infected computers.

The number of unexpected connection attempts detected at the

sensors has risen to 7, 707 .9 per IP address per day in 202 2, showing a

continuous upward trend. Reasons for surge in extraordinary access

attempts may include the increase of potential targets resulting from the

diffusion of IoT devices, and continual evolvement of attackers’ methods

enabled by the advancement of technology.

> 【Fig .19:No. of Unexpected Connection Attempts Detected at the Sensors 】

B) Major Observation

○ Surge in Access from offshore

Focusing on the country/region of origin of the detected accesses

shows that a high percentage of the accesses originated from overseas .19 / 25

> 【Fig .20 : No. of Unexpected Connection Attempts by Originating IP Addresses 】

In 2022 as well, origins of the detected access es were mostly

overseas with 7,658.6 accesses per day/IP vs. 49.4 accesses per

day/IP from within Japan, suggesting a continuous need for measures

against the transnational threats .

○ Vulnerability search targeting IoT devices

Among the detected destination ports, a majority of the unexpected

accesses were made to ports 1024 or higher , causing the high level of

number of the unexpected accesses .

> 【Fig. 21 ：Trend in No. of Access Per Day/IP by Detected Destination Port 】

20 / 25

The unexpected accesses to 1024 or higher ports usually , which are

used as standard ports of IoT devices , suggests that a majority of the se

accesses are presumabl y intended to explore the IoT devices with

vulnerabilities or to launch cyberattack s targeting IoT devices.

○ Unexpected accesses targeting Remote Desktop services *3

From 2018 through 2022, unexpected accesses to port 3389/TCP,

which is used as the stan dard Remote Desktop port, has been on a

gradual rise. Notably in December 2022, the observed number of

unexpected accesses to port 3389/TCP almost doubled vs. that in

January 2022.

> 【Fig. 22 ：Trend in No. of Access to Port 3389/TCP Used by Remote Desktop 】

In -depth observation of the unexpected accesses reveals a surge in

number of accesses aimed to probe the operational status of Remote

Desktop services , reaching the record high in 2022. Besides,

unexpected accesses to explore weak credential settings were also

detected, suggesting the expanding risk of being cyberattacked.

As remote work has become socially accepted , the opportunities to

use Remote Desktop services are increasing. To ensure secure use of

Remote Desktop services, it is important to implement appropriate

security measures , such as limiting the number of access attempts to a

specified time, ch anging IDs and passwords to strong credentials , and

implementing multifactor authentication.

> *3The function to operate the desktop environment of other networked computers.

21 / 25

(2) Spear Phishing Attack

A) Observed T rends

Among the spear -phishing email attack incidents observed by the

nationwide police in 2022, attachment of various types of malwares

attached to the sp ear phishing emails w ere detected. The identified crime

methods include sendi ng and exchanging emails impersonating real

people in order to deceive the recipients in to executing malware fil es

named with keywords of interest to the recipients.

B) Counter Cyber -intelligence Information -Sharing Network

The police and approximately 8,500 organizations nationwide (as of

December 31st, 2022) with cutting -edge technologies have established

the Counter Cyber -intelligence Information -Sharing Network (CCI

Network) to integrate and analyze information on cyberattacks including

the spear phi shing attacks to provide warnings to businesses. The CCI

Network also shares analyses on spear phishing attacks against

government agencies provided from the NISC with businesses.

> 【Fig . 23: Sample Scheme of Data Theft by Spear Phishing Attack 】

C) Major /Typical Incidents

The following are the spear -phishing incidents reported by businesses

through the CCI Network .

In 2022 , as in the previous years, sophistic ated business -spoofing spear

phishing emails and suspicious emails , including phishing emails 22 / 25

apparently intended for password theft , were continuously detected .

○ Spear phishing email attacks targeting a think tank

Spear -phishing emails directing the recipients to open the

malware -embedded attachments were sent to the think tank .

○ Spear phishing email attacks targeting a pharmaceutical manufacture

Spear phishing emails were sent to the pharmaceutical manufacturer

that urge d the recipients to open the attachment leading to the fa ke

login webpage and to enter the work account passwords , .

(3) Cybercrime Status

A) Violations of the Act on Prohibition of Unauthorized Computer Access *4

a. The number of cleared cases

The number of cleared cases of violations of the Act on Prohibition of

Unauthorized Computer Access reached 522 in 202 2, 93 cases

increased from 2021 .

> 【Fig .24: No. of Cleared Cybercrime Cases 】

> *4The following 5 acts are defined as violations of the Act on Prohibition of Unauthorized

> Compute r Access: 1) Acts of Unauthorized Computer Access, 2) Acts of Obtaining Someone

> Else’s Identification Code, 3) Acts of Facilitating Unauthorized Computer Access, 4) Acts of

> Wrongfully Storing Someone Else’s Identification Code, and 5) Acts of Illicitly Req uesting the

> Input of Identification Codes.

23 / 25

b. Major Observation

482 cases of all the cleared cases were classified as the

identification -code -abuse type *5 and accounted for approx. 92. 3% of

the total.

○ ‘Exploited the authorized users’ lax password management’ was the

most

Among the crime methods used in identity theft types of

unauthorized accesses, ‘exploited the authorized users’ lax password

management’ was the most prevalent with 230 cases (47.7 %),

followed by ‘Committed by ex -employees or acquaintances who could

know others’ IDs ’ with 41 cases ( 8.5 %).

○ Onl ine game community websites were most abused

The services most abused by suspects of the password theft -based

unauthorized accesses were online game community websites with

233 incidents (48.3 %), followed by ‘Closed websites for

employees/members ’ wit h 104 incidents ( 21.6 %).

> *5Unauthorized access can be categorized as the ’identity theft’ which abuse the identifiers of

> others, and the ‘security hole attack’ which abuse the non -identifier data or commands to evade

> specific access re strictions.

24 / 25

【Fig. 25 ：No. of Cleared Cases in Unauthorized Access by Modus Operandi 】

【Fig.: No. of Cleared Cases in Unauthorized Access by Service 】25 / 25

B) Crimes targeting computers or electromagnetic records *6

The number of cleared cases regarding crimes targeting computers

or electromagnetic records in 202 2 was 948 , increasing from 202 1.

b. Major Observations

The most dominant crime type among the cleared cases in this

category w as computer frauds, reaching 918 cases and 9 6.8 % of the

total.

> 【Fig. 27 :No. of Cleared Cases Target ing Computers or Electromagnetic Records 】

*6 Crimes defined by the Penal Code as targeting computers or electronic records.

## Extraction Notes

- parser: jina_markdown
- fetcher: jina
- normalized_at: 2026-04-28T16:03:45+00:00
- final_url: https://www.npa.go.jp/english/bureau/cyber/document/threatsincyberspace2022.pdf
- cleanup: jina navigation trim
