# Rosa's Pizza: Best Delivery Promise

A Streamlit app that recommends the promised delivery time that maximizes net profit for a chosen delivery zone and time block.

**Live app:** https://rosa-pizza-promise-app-vpyfmjaaodcswl8r4x4m3g.streamlit.app/

## How it works

For each promised delivery time in the range you choose, the app simulates orders and calculates:

net profit = (orders × profit margin) − (late orders × cost per late order)

where the cost per late order = refund + (lost future orders × profit margin). It then recommends the promise with the highest net profit.

## Using the app

1. Pick a zone and a time block.
2. Set the range of promises to try (minimum, maximum, step in minutes).
3. Adjust the profit margin, lost orders per late order, and refund if you want.
4. Click the button to see the recommended promise and its net profit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notes

- Delivery times come from the `rosa-starter` simulator package, with a fixed seed so results are reproducible.