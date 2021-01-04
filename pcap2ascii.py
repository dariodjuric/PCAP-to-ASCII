import subprocess
import sys


def main(tshark_path, pcap_path):
    # https://osqa-ask.wireshark.org/questions/56164/extract-payload-from-tcp-stream

    result = subprocess.run([tshark_path, "-r", pcap_path, "-Y", "usb", "-z", "follow,tcp,ascii,0"],
                            stdout=subprocess.PIPE)
    print(result.stdout.decode())


main(sys.argv[1], sys.argv[2])
