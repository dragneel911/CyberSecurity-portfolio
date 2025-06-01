This guide helps you set up a basic home lab to safely practice cybersecurity skills like ethical hacking, malware analysis, network monitoring, and more.

---

## 🛠 What You Need

- **Laptop/PC** with:
  - CPU: i5 or higher
  - RAM: Minimum 8GB (16GB recommended)
  - Storage: At least 50GB free space
- **Virtualization Software**:
  - [VirtualBox](https://www.virtualbox.org/) (Free)
  - or [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html) (Free for personal use)
- **ISO Files**:
  - [Kali Linux](https://www.kali.org/get-kali/)
  - [Windows 11 ISO](https://www.microsoft.com/software-download/windows11)
  - [Metasploitable 2](https://sourceforge.net/projects/metasploitable/)

## 🧱 Step-by-Step Lab Setup

### 1. Install Virtualization Software
- Download and install VirtualBox or VMware.
- Enable virtualization in BIOS/UEFI if disabled.

### 2. Download Required ISOs
- Download the ISO files listed above for attacker and victim machines.

### 3. Create Virtual Machines
- **VM 1:** Kali Linux (attacker)
- **VM 2:** Windows 11 (target system)
- **VM 3 (Optional):** Metasploitable or DVWA (vulnerable target)

### 4. Configure Network
((VIRTUAL BOX CONFIGURING)):-
🔧 Steps:
Open VirtualBox.

Select your VM (e.g., Kali Linux), click Settings.

Go to Network tab.

Under Adapter 1:

Check Enable Network Adapter.

Attached to: Internal Network.

Name: (use default or type a custom name like LabNet — all VMs must use the same name to talk to each other).

Click OK.

➡️ Repeat these steps for every VM you want on the lab network (e.g., Windows 11, Metasploitable).

((VMWARE WORKSTATION PRO)):-
🔧 Steps:
Open VMware Workstation Player.

Select your VM > Click Edit virtual machine settings.

Go to the Network Adapter tab.

Choose:

✅ Custom: Select VMnet1 (Host-only).

Click OK.

➡️ Do the same for other VMs that should be in the lab.

💡 You can manage VMnet adapters using:

Start Menu > VMware > Virtual Network Editor

There, VMnet1 = Host-only (edit IP range if needed).

### 5. Take Snapshots
- Take a VM snapshot before running malware or penetration tests to roll back if needed.

---

## 🔐 Safety Tips

- Never expose vulnerable VMs to the internet.
- Use snapshots before testing malware.
- Keep host antivirus and firewall enabled.

---

## ✅ What You Can Practice

- Nmap scanning
- Exploits with Metasploit
- Packet capture with Wireshark
- Log analysis with ELK/Splunk
- Malware behavior testing (in isolated VMs)

---

> This home lab is for **educational and ethical use only**. Never use these techniques on networks you don't own or have permission to test.

