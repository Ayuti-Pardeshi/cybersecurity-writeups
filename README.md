# cybersecurity-writeups
Cybersecurity learning documentation and technical writeups.
🛰 DNS Reconnaissance – Understanding Domain Intelligence Gathering
📌 Objective

To understand how DNS reconnaissance works in a controlled lab environment and how publicly available DNS information can be analyzed for security assessment and defensive monitoring.

🌐 What is DNS?

The Domain Name System (DNS) translates human-readable domain names (like example.com) into IP addresses.

Without DNS, we would need to remember numerical IP addresses instead of domain names.

DNS acts like the "phonebook of the internet."

🔍 What is DNS Reconnaissance?

DNS reconnaissance refers to collecting publicly available DNS information about a domain.

This process helps security professionals:

Identify exposed infrastructure

Detect misconfigurations

Understand attack surface

Monitor subdomain exposure

Evaluate security posture

It is commonly used in:

Threat intelligence

Blue team investigations

Security audits

Incident response

🛠 Types of DNS Records

Understanding record types is critical for security analysis.

A Record

Maps domain → IPv4 address

AAAA Record

Maps domain → IPv6 address

MX Record

Mail servers responsible for handling email

NS Record

Authoritative name servers for the domain

TXT Record

Used for:

SPF

DKIM

Domain verification

Security policies

CNAME Record

Alias of one domain to another

🧪 Lab Environment

All DNS queries were performed:

Using publicly available tools

Against domains meant for testing

Without targeting private or restricted systems

This research was conducted strictly for educational and defensive understanding purposes.

🔎 Common DNS Reconnaissance Techniques
1️⃣ Basic DNS Lookup

Tools:

nslookup

dig

Purpose:

Identify IP address

Validate DNS resolution

2️⃣ MX Record Enumeration

Helps understand:

Email infrastructure

Third-party mail services

Potential email spoofing risks (if misconfigured)

3️⃣ Subdomain Enumeration

Subdomains may expose:

Development servers

Staging environments

Admin panels

APIs

Security teams use this to:

Reduce attack surface

Identify forgotten assets

4️⃣ TXT Record Analysis

TXT records often contain:

SPF policies

Domain verification tokens

Security-related configurations

Misconfigurations may lead to:

Email spoofing risks

Improper authentication policies

🧠 Why DNS Recon Matters for Blue Team

From a defensive perspective, DNS reconnaissance helps:

Monitor shadow IT

Detect unauthorized subdomains

Ensure proper SPF/DKIM configuration

Identify exposed internal systems

Reduce infrastructure footprint

SOC teams often analyze DNS logs to detect:

Data exfiltration via DNS

Command-and-control traffic

Suspicious domain lookups

📊 Example Analysis Workflow

Identify domain

Query DNS records

Map IP addresses

Identify hosting provider

Analyze mail security configuration

Document findings

Recommend mitigation

🔐 Defensive Recommendations

Implement DNSSEC

Restrict zone transfers

Audit subdomains regularly

Monitor DNS logs

Harden mail authentication (SPF, DKIM, DMARC)

Remove unused records

⚖ Ethical Statement

This study was conducted in a controlled and responsible manner using publicly available information for educational and defensive cybersecurity purposes only.

No unauthorized systems were accessed or targeted.

📚 Key Takeaways

DNS is a critical intelligence source

Public records reveal infrastructure details

Proper configuration reduces exposure

DNS monitoring is essential for SOC teams

🏷 Tags

#Cybersecurity
#BlueTeam
#DNS
#ThreatDetection
#NetworkSecurity
