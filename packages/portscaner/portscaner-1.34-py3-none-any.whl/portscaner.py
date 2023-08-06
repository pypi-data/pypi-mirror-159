import logging
from progress.bar import Bar
import socket

"""                
**                   ██████╗░░█████╗░██████╗░████████╗░██████╗░█████╗░░█████╗░███╗░░██╗                               **
****                 ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║                             ****   
******               ██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░██║░░╚═╝███████║██╔██╗██║                           ******  
*******              ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗██║░░██╗██╔══██║██║╚████║                          *******
**********           ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║                       **********
************         ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝                     ************ 
"""


logging.basicConfig(level=logging.INFO)

class Scanner:
    def __init__(self):
        logging.info("portscan v.1.34")

    def scan_ports(self, seek_ip = '192.168.1.1',port_range = 65535, enable_bar = True):
        """
        {
        seek_ip: IP address for port search : String = '192.168.1.1',
        port_range: Number of ports to search : Int = 65535,
        enable_bar: Enables or disables the progress bar : Bool = True
        }

        Returns a list of open ports
        """

        ports = []
        ip = socket.gethostbyname(seek_ip)

        if(enable_bar):
            logging.info("We start checking the ports with the progress bar")
            with Bar('Processing', max=port_range) as bar:
                for i in range(port_range):
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    if client.connect_ex((ip, i)):
                        pass
                    else:
                       ports.append(i)
                    bar.next()
            logging.info("Finish")

        else:
            logging.info("We start checking the ports")
            for i in range(port_range):
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if client.connect_ex((ip,i)):
                    pass
                else:
                    ports.append(i)
            logging.info("Finish")

        return ports


if __name__ == '__main__':
    logging.info("This file is the main one in the portscan library.You can use it in your projects as a dependency. Usage examples are in the file example.py")