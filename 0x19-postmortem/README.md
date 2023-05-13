# Postmortem: SSH Access Issue on Web Server Resulting in Server Rebuild
![Root Cause Analysis Image](https://camo.githubusercontent.com/4a0ccc51dc9c06e80e2d73410af1c1e891b43de55bcdf5e9188d4ade8b542004/68747470733a2f2f74332e667463646e2e6e65742f6a70672f30342f39322f30392f37322f3234305f465f3439323039373234365f79616745387839556b384d3949656b50793747427545307831556f61376573442e6a7067)

> **Date: 28th March, 2023**\
> **Author: Okoronkwo Chinedu Elijah**\
> **Status: Closed**

## Summary
![Summary image](https://images.pexels.com/photos/6980523/pexels-photo-6980523.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
On 28th March, 2023, an issue occurred where SSH access to my web server was blocked after the installation of UFW (Uncomplicated Firewall) without explicitly allowing SSH connections. Due to the severity of the issue and the inability to access the server, I made the decision to ask for a new web server and started from the scratch.  This postmortem aims to identify the root cause, outline the impact, document the resolution steps taken, and propose preventive measures to avoid similar incidents in the future.

## Timeline
- 10:15 AM - UFW firewall was installed on the web server.
- 10:45 AM - SSH access to the server became inaccessible.
- 11:00 AM - After unsuccessful attempts to resolve the issue, the decision was made to generate new web server.
- 11:05 AM - The web server was rebuilt from scratch.

## Root Cause
![Root cause image](https://camo.githubusercontent.com/a9b24d1a20a11218c19d6d25b37e758b2eb81060ae88105e40e1d2a5968d1382/68747470733a2f2f626c6f672e73797374656d73656e67696e656572696e672e636f6d2f68732d66732f68756266732f626c6f672d66696c65732f526f6f7425323043617573652e6a70673f77696474683d363030266e616d653d526f6f7425323043617573652e6a7067)
The root cause of the issue was the installation of UFW without explicitly configuring it to allow SSH connections. UFW, by default, denies all incoming connections, including SSH, unless rules are added to permit specific services. As a result, SSH access was completely blocked, making it impossible to rectify the issue remotely.

## Impact
The impact of the issue was severe as it led to a complete loss of SSH access to the web server. This prevented me from remotely accessing and managing the server, resulting in a disruption of ongoing operations and necessitating a full server rebuild.

## Resolution Steps
1. Attempted to investigate the issue by examining server logs and verifying network connectivity.
2. Identified that UFW was blocking SSH connections due to its default configuration.
3. Tried accessing the server through alternative methods (console access or physical access) but was unsuccessful due to unavailability or technical limitations.
4. Considering the severity of the issue and the inability to access the server, the decision was made to request a new web server.
5. Initiated the process of reinnstalling necessary services required by the project.
6. Ensured that the new web server was set up with appropriate firewall rules, including explicitly allowing SSH connections.
7. Tested SSH connectivity to ensure it was successfully restored.
8. Verified that the server was functioning correctly and all other services were operational.

## Preventive Measures
To prevent similar incidents in the future, the following preventive measures are recommended:

1. **Planning and Documentation:** Before making any changes to critical server configurations, thoroughly review the documentation and understand the potential impact on accessibility.
2. **Testing in a Staging Environment:** Test any changes in a staging environment before applying them to production servers. This allows for thorough testing and identification of potential issues.
3. **Backup and Recovery:** Regularly backup critical server configurations and data to facilitate quick recovery in case of unexpected issues.
4. **Rule Verification:** When configuring a firewall, double-check the rules to ensure that essential services like SSH are explicitly allowed.
5. **Limited Scope of Firewall Rules:** Minimize the scope of firewall rules to only allow necessary connections, reducing the attack surface and potential for misconfigurations.
6. **Monitoring and Alerts:** Implement monitoring and alerting systems to detect any sudden loss of connectivity or unusual firewall activities, enabling prompt investigation and resolution.

## Lessons Learned
1. The severity of the issue and the inability to remotely access the server can sometimes require drastic measures like a full server rebuild.
2. Thorough planning, documentation, and testing can help avoid such severe incidents
3. Regular backups and testing in a staging environment can mitigate
