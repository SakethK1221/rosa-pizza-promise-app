import numpy as np
import streamlit as st

from starter import COSTS, TIME_BLOCKS, ZONES, delivery_times


#Calulate total cost per late order
def cost_per_late_order(costs):
    refund = costs["refund"]
    churn = costs["churn_orders"]
    margin = costs["margin"]
    return refund + (churn*margin)


#Calculate net profit for one zone, time block, and promise
def net_profit(zone, time_block, promise, costs):
    times = delivery_times(zone, time_block, promise, seed=1)
    n_orders = len(times)
    n_late = np.sum(times > promise)
    profit_collected = n_orders * costs["margin"]
    late_costs = n_late * cost_per_late_order(costs)
    actual_profit = profit_collected - late_costs
    return actual_profit


#Calculate Best Promise
def best_promise(zone, time_block, promises, costs):
    best_profit = float('-inf')
    best_promise_value = None

    for promise in promises:
        profit = net_profit(zone, time_block, promise, costs)
        if profit > best_profit:
            best_profit = profit
            best_promise_value = promise

    return best_promise_value, best_profit


st.title("Rosa's Pizza Delivery Promise")
st.write("Choose a delivery promise that balances customer costs and order margin.")

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

st.subheader("Promise range")
minimum_promise = st.number_input("Minimum promise (minutes)", min_value=0, value=20, step=1)
maximum_promise = st.number_input("Maximum promise (minutes)", min_value=0, value=80, step=1)
promise_step = st.number_input("Promise step (minutes)", min_value=1, value=5, step=1)

st.subheader("Order economics")
margin = st.number_input("Profit margin per order $", min_value=0.0, value=float(COSTS["margin"]), step=0.01)
churn_orders = st.number_input(
    "Churn per late order $",
    min_value=0.0,
    value=float(COSTS["churn_orders"]),
    step=0.01,
)
refund = st.number_input(
    "Refund per late order $",
    min_value=0.0,
    value=float(COSTS["refund"]),
    step=0.01,
)

if st.button("Recommend promise"):
    if minimum_promise > maximum_promise:
        st.error("The minimum promise must not exceed the maximum promise.")
    else:
        promises = range(minimum_promise, maximum_promise + 1, promise_step)
        costs = {
            "margin": margin,
            "churn_orders": churn_orders,
            "refund": refund,
        }
        recommended_promise, profit = best_promise(zone, time_block, promises, costs)
        st.success(f"Recommended promise for {zone} / {time_block}: {recommended_promise} minutes")
        st.metric("Net profit", f"${profit:,.2f}")