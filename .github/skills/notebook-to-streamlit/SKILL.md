---
name: notebook-to-streamlit
description: Convert analysis logic from a Jupyter notebook into a Streamlit app. Use when asked to port notebook functions into app.py, keep results identical to the notebook, and connect Streamlit widgets to function inputs.
---
# Notebook to Streamlit

Use this skill to turn tested notebook functions into a Streamlit app without changing their behavior.

## Rules

1. **Reuse the notebook logic exactly.** Copy `cost_per_late_order`, `net_profit`, and `best_promise` with the same names, parameters, and formulas. Do not rewrite or "improve" the math.
2. **Keep the signatures.** `best_promise(zone, time_block, promises, costs)` returns `(best_promise, net_profit)`. `costs` is a dict with keys `refund`, `churn_orders`, and `margin`.
3. **Import the given data, never redefine it.** Use `from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times`.
4. **Keep `seed=1`** in every `delivery_times` call so the app matches the notebook.
5. **Widgets feed the functions.** Build a `costs` dict from the user's inputs and a `promises` list from the range inputs, then pass them in. Never hardcode values inside the functions.
6. **Use the `COSTS` values as widget defaults.**
7. **Validate input.** Show a clear error (`st.error`) if the minimum promise exceeds the maximum, and do not run the search.
8. **Run the search only when the button is clicked.**

## Required inputs

- Dropdowns: zone, time block
- Range of promises: minimum, maximum, step (whole minutes, step at least 1)
- Numbers: profit margin per order, churn (lost orders) per late order, refund per late order

## Output

The recommended promise in minutes and its net profit, shown after the button click.

## Checks before finishing

With default inputs and range 20 to 80, step 5:
- Far West / Fri/Sat eve recommends 55 minutes, net profit $1,212.40
- Central / Other recommends 45 minutes, net profit $1,579.00

`requirements.txt` must list `streamlit`, `numpy`, and `git+https://github.com/zhouy185/rosa-starter.git`.