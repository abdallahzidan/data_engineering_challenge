# data_engineering_challenge
this repo contains solution for analyzing streaming data of machines in real time

## System Design 
- Stream.Py scripts loads the data which exists in resouces folder ( Mertrics.Json, Workorder.json). 
- By comparing latest time offset Stream.Py Streams only the new data then it will push to Webhook hosted in localhost:5000/
- Webhooks has two end points listen to any Post Message and Push to RabbitMQ queues using Producer.py script . 
- Once message arrives to RabbitMQ, Both Consumers ( Mertrics_consumer.Py , Workorder_consumer.Py) fetch & presist data in Sqlite db. 
- Below figure shows a high overview of Solution design/workflow.  
![360view](https://user-images.githubusercontent.com/18703395/213935687-70af8f6b-d2f9-4bf4-898b-5f7032e517ac.png)

## Rabbit MQ
![rabbitmq](https://user-images.githubusercontent.com/18703395/213935695-157f2985-9376-4b8f-b7d6-3727167e4c6d.png)

## Running workflow
![running](https://user-images.githubusercontent.com/18703395/213935698-503c2a2d-c43a-418c-a2b3-f5294be07636.png)

## Sqlite
![db](https://user-images.githubusercontent.com/18703395/213935721-4cf2ffbc-a4e0-403f-ba43-5fb777b9b46b.png)

## report
![report](https://user-images.githubusercontent.com/18703395/213935728-3f047724-a392-48fe-8e8d-c2ef1b322f79.png)
