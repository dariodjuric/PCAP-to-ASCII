# PCAP to ASCII script

This Python script takes a PCAP file (result of Wireshark/TCPdump capture), extracts all TCP streams and writes them to separate files. This is useful if you have a large capture file with many TCP streams to analyze.

It relies on TShark, which is a command-line tool that comes installed with Wireshark.

To run the script, execute:

```python
python pcap2ascii.py "[path to TShark]" "[path to PCAP file]" 
```

This will write a separate file for each stream. Each file will be named `stream-X.log` where `X` is stream ID.