import subprocess
import sys


def main(tshark_path, pcap_path):
    session_list_lines = subprocess.run([tshark_path, "-r", pcap_path, "-Y", "usb", "-z", "conv,tcp"],
                                        stdout=subprocess.PIPE).stdout.decode().splitlines()

    stream_count = len(session_list_lines) - 6  # Minus headers and footers

    for stream_id in range(stream_count):
        result = subprocess.run(
            [tshark_path, "-r", pcap_path, "-Y", "usb", "-z", "follow,tcp,ascii,{}".format(stream_id)],
            stdout=subprocess.PIPE)
        result_lines = result.stdout.decode().splitlines()
        lines_without_header = result_lines[result_lines.index("Follow: tcp,ascii") + 4:]
        tcp_stream_ascii = "".join([lines_without_header[i] for i in range(len(lines_without_header)) if i % 2 == 1])

        with open("stream-{}.log".format(stream_id), "a") as result_file:
            result_file.write(tcp_stream_ascii)


if len(sys.argv) == 3:
    main(sys.argv[1], sys.argv[2])
else:
    print("The script requires two arguments: path to TShark and path to PCAP file")
