from time import sleep
import colorama
from colorama import *
from colorama import Style
colorama.init(autoreset=True)
banner=Fore.BLUE+Style.BRIGHT+'''       █████                 █████                    █████     
      ░░███                 ░░███                    ░░███      
       ░███  █████ █████  ███████   ██████  ████████  ░███ █████
       ░███ ░░███ ░░███  ███░░███  ███░░███░░███░░███ ░███░░███ 
       ░███  ░░░█████░  ░███ ░███ ░███ ░███ ░███ ░░░  ░██████░  
 ███   ░███   ███░░░███ ░███ ░███ ░███ ░███ ░███      ░███░░███ 
░░████████   █████ █████░░████████░░██████  █████     ████ █████
 ░░░░░░░░   ░░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░     ░░░░ ░░░░░ '''
intro=Fore.GREEN+Style.BRIGHT+'''                        Made by Jatin aka Mr.jtx
                            Made in python 
'''
os.system("clear")
print(banner)
print(intro)
def Direcotorylist(a):
      dork=('''"google site:{} intitle:index.of"'''.format(a))
      print('Here is the dork :-')
      print(' ')
      print("-> ",dork)

def Exposedconfig(a):
       
       dork=('site:{} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def ExposedDatafiles(a):
       
       dork=('site:{} ext:sql | ext:dbf | ext:mdb'.format(a))
       print("-> ",dork)
def findwordpress(a):
      
       dork=('site:{} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def exposelogfiles(a):
       
       dork=('site:{} ext:log | inurl:/9100'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)

def Backupandold(a):
       
       dork=('site:{} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def loginpages(a):
       
       dork=('site:{} inurl:login'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def sqlerror(a):
       
       dork=('site:{} intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def publiclyexposedoc(a):
      
       dork=('site:{} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def phpinfo(a):
       
       dork=('site:{} ext:php intitle:phpinfo "published by the PHP Group"'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def Findingbackdor(a):
       
       dork=('site:{} inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)

def Installsetup(a):
       
       dork=('site:{} inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def openredirect(a):
      
       dork=('site:{} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
     
def apacherce(a):
       
       dork=('site:{} ext:action | ext:struts | ext:do'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def findpastebin(a):
       
       dork=('site:pastebin.com {}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def employlinkden(a):
       
       dork=('site:linkedin.com employees {}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def htaccess(a):
       
       dork=('site:{} inurl:"/phpinfo.php" | inurl:".htaccess" | inurl:"/.git" google -github'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def subdommains(a):
       
       dork=('site:*.{}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def subsubdomain(a): 
      
       dork=('site:*.*.{}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def findwordpress2(a):
       dork=('site:{} inurl:wp-content | inurl:wp-includes'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)

def wordpressWayback(a):
       dork=('http://wwwb-dedup.us.archive.org:8083/cdx/search?url={}/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
       

def Github(a):
       dork=('https://github.com/search?q=%22*.{}%22&type=host'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
       

def openbugbounty(a):
       dork=('https://www.openbugbounty.org/search/?search={}&type=host'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
       
def crossDomain(a):
       dork=('https://{}/crossdomain.xml'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
       
def ThreatCrowd(a):
       dork=('https://threatcrowd.org/domain.php?domain={}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
    
def  Swfgoogle(a):
       
       dork=('inurl:{} ext:swf'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def swfyandex(a):
       dork=('https://yandex.com/search/?text=site%3A{}+mime%3Aswf&lr=112509'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
       
def Swfwayback(a):
       dork=('https://web.archive.org/cdx/search?url={}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)
def wayback3(a):
      dork=('https://web.archive.org/web/*/{}/*'.format(a))
      print('Here is the dork :-')
      print(' ')
      print("-> ",dork)


def crtsh(a):
       dork=('https://crt.sh/?q=%25.{}'.format(a))
       print('Here is the dork :-')
       print(' ')
       print("-> ",dork)

def shodan(a):
      dork=('https://www.shodan.io/search?query={}'.format(a))
      print('Here is the dork :-')
      print(' ')
      print("->",)
def Bugbountpro(a):
        dork=('site:{} inurl:/responsible disclosure'.format(a))
        print('Here is the dork :-')
        print(' ')
        print("->",dork)
        


print(Style.BRIGHT+Fore.RED+"[1] "+Style.BRIGHT+Fore.YELLOW+" Directory listing"+Style.BRIGHT+Fore.RED+"          [2]  "+Style.BRIGHT+Fore.YELLOW+"Exposed Configuration files")
print(Style.BRIGHT+Fore.RED+"[3] "+Style.BRIGHT+Fore.YELLOW+" Exposed Database files"+Style.BRIGHT+Fore.RED+"     [4]  "+Style.BRIGHT+Fore.YELLOW+"Find WordPress")
print(Style.BRIGHT+Fore.RED+"[5] "+Style.BRIGHT+Fore.YELLOW+" Exposed log files"+Style.BRIGHT+Fore.RED+"          [6]  "+Style.BRIGHT+Fore.YELLOW+"Backup and old files")
print(Style.BRIGHT+Fore.RED+"[7] "+Style.BRIGHT+Fore.YELLOW+" Login pages"+Style.BRIGHT+Fore.RED+"                [8]  "+Style.BRIGHT+Fore.YELLOW+"SQL errors")
print(Style.BRIGHT+Fore.RED+"[9] "+Style.BRIGHT+Fore.YELLOW+" Publicly exposed documents"+Style.BRIGHT+Fore.RED+" [10] "+Style.BRIGHT+Fore.YELLOW+"phpinfo()")
print(Style.BRIGHT+Fore.RED+"[11] "+Style.BRIGHT+Fore.YELLOW+"Finding Backdoors"+Style.BRIGHT+Fore.RED+"          [12] "+Style.BRIGHT+Fore.YELLOW+"Install / Setup files")
print(Style.BRIGHT+Fore.RED+"[13] "+Style.BRIGHT+Fore.YELLOW+"Open Redirects"+Style.BRIGHT+Fore.RED+"             [14] "+Style.BRIGHT+Fore.YELLOW+"Apache STRUTS RCE")
print(Style.BRIGHT+Fore.RED+"[15] "+Style.BRIGHT+Fore.YELLOW+"Find Pastebin entries"+Style.BRIGHT+Fore.RED+"      [16] "+Style.BRIGHT+Fore.YELLOW+"Employees on LINKEDIN")
print(Style.BRIGHT+Fore.RED+"[17] "+Style.BRIGHT+Fore.YELLOW+".htaccess sensitive files"+Style.BRIGHT+Fore.RED+"  [18] "+Style.BRIGHT+Fore.YELLOW+"Find Subdomains")
print(Style.BRIGHT+Fore.RED+"[19] "+Style.BRIGHT+Fore.YELLOW+"Find Sub-Subdomains"+Style.BRIGHT+Fore.RED+"        [20] "+Style.BRIGHT+Fore.YELLOW+"Find WordPress #2")
print(Style.BRIGHT+Fore.RED+"[21] "+Style.BRIGHT+Fore.YELLOW+"Search in GITHUB"+Style.BRIGHT+Fore.RED+"           [22] "+Style.BRIGHT+Fore.YELLOW+"Find WordPress [Wayback Machine]")
print(Style.BRIGHT+Fore.RED+"[23] "+Style.BRIGHT+Fore.YELLOW+"Test CrossDomain"+Style.BRIGHT+Fore.RED+"           [24] "+Style.BRIGHT+Fore.YELLOW+"Search in OpenBugBounty")
print(Style.BRIGHT+Fore.RED+"[25] "+Style.BRIGHT+Fore.YELLOW+"Check in crt.sh"+Style.BRIGHT+Fore.RED+"            [26] "+Style.BRIGHT+Fore.YELLOW+"Check in ThreatCrowd")
print(Style.BRIGHT+Fore.RED+"[27] "+Style.BRIGHT+Fore.YELLOW+"Search in SHODAN"+Style.BRIGHT+Fore.RED+"           [28] "+Style.BRIGHT+Fore.YELLOW+"Find .SWF file (Google)")
print(Style.BRIGHT+Fore.RED+"[29] "+Style.BRIGHT+Fore.YELLOW+"Search in WayBack Machine 3"+Style.BRIGHT+Fore.RED+"[30] "+Style.BRIGHT+Fore.YELLOW+"responsible disclosure")

website=input(Style.BRIGHT+Fore.GREEN+"Enter the website name:- ")
option=int(input(Style.BRIGHT+Fore.GREEN+"Enter option no.:- "))



if option==(1):
  Direcotorylist(website)
elif option==(2):
      Exposedconfig(website)
elif option==(3):
      ExposedDatafiles(website)
elif option==(4):
      findwordpress(website)
elif option==(5):
      exposelogfiles(website)
elif option==(6):
      Backupandold(website)
elif option==(7):
      loginpages(website)
elif option==(8):
      sqlerror(website)
elif option==(9):
      publiclyexposedoc(website)
elif option==(10):
      phpinfo(website)
elif option==(11):
      Findingbackdor(website)
elif option==(12):
      Installsetup(website)
elif option==(13):
      openredirect(website)
elif option==(14):
      apacherce(website)
elif option==(15):
      findpastebin(website)
elif option==(16):
      employlinkden(website)
elif option==(17):
      htaccess(website)
elif option==(18):
      subdommains(website)
elif option==(19):
      subsubdomain(website)
elif option==(20):
      findwordpress2(website)
elif option==(21):
      Github(website)
elif option==(22):
      wordpressWayback(website)
elif option==(23):
      crossDomain(website)
elif option==(24):
      openbugbounty(website)
elif option==(25):
      crtsh(website)
elif option==(26):
      ThreatCrowd(website)
elif option==(27):
      shodan(website)
elif option==(28):
      Swfgoogle(website)
elif option==(29):
      wayback3(website)
elif option==(30):
       Bugbountpro(website)
