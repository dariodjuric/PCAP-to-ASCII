import subprocess
import sys


def main(tshark_path, pcap_path):
    # https://osqa-ask.wireshark.org/questions/56164/extract-payload-from-tcp-stream

    result = subprocess.run([tshark_path, "-r", pcap_path, "-Y", "us", "-z", "follow,tcp,ascii,{}".format(0)],
                            stdout=subprocess.PIPE)
    result_lines = result.stdout.decode().splitlines()
    lines_without_header = result_lines[result_lines.index("Follow: tcp,ascii") + 4:]
    tcp_stream_ascii = "".join([lines_without_header[i] for i in range(len(lines_without_header)) if i % 2 == 1])
    print(tcp_stream_ascii)


main(sys.argv[1], sys.argv[2])
