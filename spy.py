#!/data/data/com.termux/files/usr/bin/bash

RED='\033[031m'
GREEN='\033[032m'
BLUE='\033[034m'
CYAN='\033[036m'
WHITE='\033[037m'
BOLD='\033[1m'
NONE='\033[0m'

clear

echo -e "${RED}${BOLD}"
echo "  ██████  ██████  ██    ██        ███████ "
echo " ██      ██    ██  ██  ██         ██      "
echo "  █████  ██    ██   ████   █████  █████   "
echo "      ██ ██    ██    ██           ██      "
echo " ██████   ██████     ██           ███████ "
echo "                                          "
echo -e "${WHITE}    [+] CONSOLE v2.0 by 123Tool [+]${NONE}"
echo -e "${CYAN}    [+] Powered by SPY-E Team    [+]${NONE}"
echo "------------------------------------------------"

# --- MENU UTAMA ---
echo -e "${GREEN}1.${NONE} Install All Tools (Metasploit, SQLmap, Nikto, dll)"
echo -e "${GREEN}2.${NONE} SQL Injection Scanner (SQLmap)"
echo -e "${GREEN}3.${NONE} Web Vulnerability Scan (Nikto)"
echo -e "${GREEN}4.${NONE} Exploitation Framework (Metasploit)"
echo -e "${GREEN}5.${NONE} SMS Sender (Termux API)"
echo -e "${GREEN}6.${NONE} Image Scraper (Python OSINT)"
echo -e "${GREEN}7.${NONE} Network Scanner (Nmap)"
echo -e "${RED}0.${NONE} Exit"
echo "------------------------------------------------"
read -p "Pilih Senjata Bos: " pilihan

case $pilihan in
    1)
        echo -e "${BLUE}[*] Memulai instalasi massal... Tunggu Bos!${NONE}"
        pkg update && pkg upgrade -y
        pkg install python python-pip git nmap nikto termux-api php wget curl -y
        pip install requests beautifulsoup4
        # Install SQLmap
        git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git $HOME/sqlmap
        # Install Metasploit (Proses ini lama)
        pkg install metasploit -y
        echo -e "${GREEN}[+] Semua bahan sudah di gudang!${NONE}"
        ;;
    2)
        read -p "Masukkan URL Target SQLi: " sqlitarget
        python $HOME/sqlmap/sqlmap.py -u $sqlitarget --batch --banner
        ;;
    3)
        read -p "Masukkan URL Target Web: " target
        nikto -h $target
        ;;
    4)
        msfconsole
        ;;
    5)
        read -p "Nomor Tujuan: " nohp
        read -p "Isi Pesan: " pesan
        termux-sms-send -n $nohp "$pesan"
        echo -e "${GREEN}[+] SMS Terkirim!${NONE}"
        ;;
    6)
        read -p "Link Web Scrape: " link
        python -c "import requests; from bs4 import BeautifulSoup; r=requests.get('$link'); soup=BeautifulSoup(r.text, 'html.parser'); [print(img['src']) for img in soup.find_all('img') if 'src' in img.attrs]"
        ;;
    7)
        read -p "IP/Domain Target: " nmap_target
        nmap -A $nmap_target
        ;;
    0)
        exit
        ;;
    *)
        echo "Opsi salah Bos!"
        ;;
esac
