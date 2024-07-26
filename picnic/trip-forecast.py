"""
Trip Forecast at Picnic
Pincic wishes to forecast how many trips are required to deliver all customer
orders and optimize people planning. Planning too many people is a waste of 
money, and planning not enough people will limit the number of deliveries we 
can handle. To provide the most accurate forecast, we need to get constant 
updates on how many orders do we forse our customers will place. To calculate it
we have two sources, our delivery forecast and hub capacity. We need to select 
the most constraining source to ensure accurate predictions.

## GET /v1/updates




Return delivery updates for all the hubs in the Netherlands. Poll-based: any
update will only be visible once.


Example response:
    [
      {'hub_id': ‘DEV', 'deliveries': 5, 'source’:'forecast’},
      {'hub_id': ‘DEV', 'deliveries': 20, 'source’:'forecast’},
      {'hub_id': ‘EMM', 'deliveries': 5, 'source’:'forecast’},
      {'hub_id': ‘DEV', 'deliveries': 17, 'source’:'capacity’},
      ...
    ]
    
| hub_id | deliveries |
|--------|------------|
|     DEV|          17|
|     EMM|          5 |

# The output table
The output table will be used by our forecasting model as features. 
| hub_id | deliveries |
|--------|------------|
|     DEV|          17|
|     EMM|          24|
|     AMS|          18|
|     ...|         ...|
"""
# feature_store = {}

# def update_features(hub_id: str, deliveries: int, source: str):
    
#     if feature_store[hub_id] is None:
#         feature_store[hub_id] = deliveries
#     else:


class config:
    secrets:

class Hub:
    def __init(self, hub_id: str , deliveries,  source):
        self.hub_id = hub_id
        self.deliveries = deliveries
        self.source = source
        


# key hub id value is forecast or capacity whichever is less 
feature_store = {}

# key: hub_id value [forecast, capacity]
response_dict = {}
for row in responses:
    if row['source'] == 'forecast':
        response_dict[row['hub_id']][0] = row['deliveries']
    else:
        response_dict[row['hub_id']][1] = row['deliveries']
    
    final_delivery = min(response_dict[row['hub_id']][0], response_dict[row['hub_id']][1])
    feature_store['hub_id'] = final_delivery
    ('Update .... where hub_id = ? < ', final_delivery)
