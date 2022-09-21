import pandas as pd
import streamlit as st
from .carousel import build_html as build_carousel_html
from .algorithm_details import show as show_algorithm_details
from .algo import Algo
import datetime


def show():
    st.markdown('### Proportional advertisement algorithm')
    budget_count = st.number_input('Number of advertisers', step=1, min_value=1, max_value=10, value=3)
    for i in range(budget_count):
        st.number_input(f'Advertiser #{i + 1} budget', step=1, key=f'budget_{i}', min_value=1, max_value=1000000, value=100)

    carousel_products = st.number_input('Number of products in carousel', min_value=1, max_value=100, value=20)

    budgets = [st.session_state[f'budget_{i}'] for i in range(budget_count)]
    if 'algo' not in st.session_state:
        algo = Algo(budgets=budgets)
        st.session_state['algo'] = algo
    else:
        algo = st.session_state['algo']
        algo.update_params(budgets=budgets)

    def assign_carousel():
        algo.visit(carousel_products)
        print(f'{datetime.datetime.now()}')

    def reset_counters():
        algo.reset_counters()

    visit_col, reset_col = st.columns(2)
    with visit_col:
        st.button('New page visit', on_click=assign_carousel)
    with reset_col:
        st.button('Reset views', on_click=reset_counters)

    df = pd.DataFrame(algo.info())
    df.index = [f'#{i + 1}' for i in range(len(df))]
    st.table(df)

    if len(algo.last_arrangement) != 0:
        st.write('Product arrangement in carousel')
        st.write(build_carousel_html(algo.last_arrangement, budget_count), unsafe_allow_html=True)

    if st.checkbox('Show algorithm details'):
        show_algorithm_details()
