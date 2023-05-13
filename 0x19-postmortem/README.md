# Postmortem: SSH Access Issue on Web Server Resulting in Server Rebuild
![Root Cause Analysis Image](https://images.pexels.com/photos/5310564/pexels-photo-5310564.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

**Date:** 28th March, 2023\
**Author:** Okoronkwo Chinedu Elijah\
**Status:** Closed

## Summary
On [Insert Date], an issue occurred where SSH access to the web server was blocked after the installation of UFW (Uncomplicated Firewall) without explicitly allowing SSH connections. Due to the severity of the issue and the inability to access the server, the decision was made to rebuild the web server from scratch. This postmortem aims to identify the root cause, outline the impact, document the resolution steps taken, and propose preventive measures to avoid similar incidents in the future.

## Timeline
- [Insert Date/Time]: UFW firewall was installed on the web server.
- [Insert Date/Time]: SSH access to the server became inaccessible.
- [Insert Date/Time]: After unsuccessful attempts to resolve the issue, the decision was made to rebuild the web server.
- [Insert Date/Time]: The web server was rebuilt from scratch.

## Root Cause
The root cause of the issue was the installation of UFW without explicitly configuring it to allow SSH connections. UFW, by default, denies all incoming connections, including SSH, unless rules are added to permit specific services. As a result, SSH access was completely blocked, making it impossible to rectify the issue remotely.

## Impact
The impact of the issue was severe as it led to a complete loss of SSH access to the web server. This prevented administrators from remotely accessing and managing the server, resulting in a disruption of ongoing operations and necessitating a full server rebuild.

## Resolution Steps
1. Attempted to investigate the issue by examining server logs and verifying network connectivity.
2. Identified that UFW was blocking SSH connections due to its default configuration.
3. Tried accessing the server through alternative methods (console access or physical access) but was unsuccessful due to unavailability or technical limitations.
4. Considering the severity of the issue and the inability to access the server, the decision was made to rebuild the web server from scratch.
5. Initiated the process of rebuilding the server, including reinstalling the operating system, configuring necessary services, and restoring data from backups or recreating it.
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
