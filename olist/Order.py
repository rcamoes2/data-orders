import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from olist.data import Olist
olist = Olist()
data = olist.get_data()

orders = data['orders'].copy() # good practice to be sure not to modify your `data` variable

assert(orders.shape == (99441, 8))

# Inspect the orders dataframe
#filter the dataframe on delivered orders
#delivered_orders = orders[orders.order_status == 'delivered'].copy()
#delivered_orders.loc[:, 'order_purchase_timestamp'] = delivered_orders.loc[:, 'order_purchase_timestamp'].apply(pd.to_datetime)
#delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]] = delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]].apply(pd.to_datetime)


def get_wait_time():
    """
    Returns the wait time for a given order status.
    """
    delivered_orders = orders[orders.order_status == 'delivered'].copy()
    delivered_orders.loc[:, 'order_purchase_timestamp'] = delivered_orders.loc[:, 'order_purchase_timestamp'].apply(pd.to_datetime)
    delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]] = delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]].apply(pd.to_datetime)
    #convert dates from "string" type to "pandas.datetime' using pandas.to_datetime()
    delivered_orders.loc[:, 'order_purchase_timestamp'] = delivered_orders.loc[:, 'order_purchase_timestamp'].apply(pd.to_datetime)
    delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]] = delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]].apply(pd.to_datetime)
    # add wait_time column
    delivered_orders.loc[:, 'wait_time'] = delivered_orders.order_delivered_customer_date - delivered_orders.order_purchase_timestamp
    # Compute expected_wait_time using loc
    delivered_orders.loc[:, 'expected_wait_time'] = delivered_orders.order_estimated_delivery_date - delivered_orders.order_purchase_timestamp
    # Compute delay_vs_expected
    delivered_orders.loc[:, 'delay_vs_expected'] = delivered_orders.order_delivered_customer_date - delivered_orders.order_estimated_delivery_date
    #show only order_id, wait_time, expected_wait_time, delay_vs_expected, order_status
    delivered_orders = delivered_orders[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected', 'order_status']]

    return delivered_orders

print(get_wait_time())
