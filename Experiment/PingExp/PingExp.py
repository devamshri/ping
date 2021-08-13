import pandas as pd
import os

ip = pd.read_csv("ip.csv")
status = []

for i in ip["IP"]:
    exit_code = os.system(f"ping {i}")
    status.append(exit_code==0)

ip["Status"] = status
ip.to_csv("ip.csv", index=False)
print(ip)