import requests,sys, os
import json
import time
import pandas as pd
import dao as da
import yaml


config=[]
# Read configurations from config.yaml
with open("config.yaml", "r") as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
        
def send_webhook(data_obj,webhook_url):
    requests.post(webhook_url,data=json.dumps(data_obj),headers={'content-type':'application/json'})

def Get_offsets():
    initialload=config['InitialLoad']
    return da.get_offset_time(initialload)
    
    
def filter_stream(df,tablename):
    offsets_dict  = Get_offsets()
    delta_df =df[df['time'] > offsets_dict[tablename]] 
    return delta_df.to_json(orient="records")
    
def main():
     
    webhook_metrics=config['webhooks']['metrics']
    webhook_workorder=config['webhooks']['workorder']
    
    metrics_df = pd.read_json(config['src']['metrics_relative_path']) 
    workorder_df = pd.read_json(config['src']['workorder_relative_path']) 
    
    incominmg_metrics = filter_stream(metrics_df,'metrics')
    incominmg_workorders= filter_stream(workorder_df,'workorder')

    send_webhook(incominmg_metrics,webhook_metrics)
    send_webhook(incominmg_workorders,webhook_workorder)
    
    print('Data sent to send_webhook...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)