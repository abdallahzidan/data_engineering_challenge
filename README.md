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
- RabbitMQ is being used for buffering incoming data of Mertrics & Workorder and for better system decoupling
- There are two main queues Mertrics queue and Workorder queue 
-  Below figure shows queues details running on RabbitMQ http://localhost:15672/#/queues

![rabbitmq](https://user-images.githubusercontent.com/18703395/213935695-157f2985-9376-4b8f-b7d6-3727167e4c6d.png)

## Running workflow
- Running the workflow requires running to be as following 
- Run Webhook server which listen to any POST messages and redirect to RabbitMQ
- Run Both Consumers ( Mertrics_consumer.Py , Workorder_consumer.Py) in order to fetch new data and presist in Sqlite
- Run Stream.Py to stream the incoming metrics & workorder data. There are two modes Initail and Incremental mode 
- Below figure shows a demo for sending data through Stream.Py and whole workflow proccess the data accordingly 

![running](https://user-images.githubusercontent.com/18703395/213935698-503c2a2d-c43a-418c-a2b3-f5294be07636.png)

## Sqlite
- Sqlite is being used as the storage layer in this workflow 
- Sqlite stores the data into two main tables Mertrics , Workorder table 
- Below figure shows inserted data in Both tables after Consumers process the data 
![db](https://user-images.githubusercontent.com/18703395/213935721-4cf2ffbc-a4e0-403f-ba43-5fb777b9b46b.png)

## report
-- report has been refreshed as the last step in the workflow 
-- report is being generated using the following query : 
with top_three_parameters as (
select  product,production,val,dense_rank() over(partition by product order by production desc) as rank 
from workorder inner join metrics 
on product = id
) select * from top_three_parameters where rank<4


![report](https://user-images.githubusercontent.com/18703395/213935728-3f047724-a392-48fe-8e8d-c2ef1b322f79.png)
