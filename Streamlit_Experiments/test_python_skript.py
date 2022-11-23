import streamlit as st
import pandas as pd
import graphviz

st.sidebar.title("Production line configurations")

#col1, col2 = st.sidebar.columns(2)
#machine_number = 0
#with col1:
#    add_machine_pressed = st.sidebar.button('add Machine')
#    if add_machine_pressed:
#        machine_number = machine_number + 1
#        remove_machine = st.sidebar.button('remove_machine')

machine_number = st.sidebar.number_input('Number of machines', min_value=int(0), max_value=int(8))

machine_names = list(range(machine_number))
for i in range(machine_number):
    col1, col2 = st.columns(2)

    with col1:
        machine_name = st.text_input('Name of Machine Nr. %s' % (i + 1))
    with col2:
        if machine_name == '':
            machine_name = str(i+1)
            print(machine_name)
        machine_ftr_number = st.number_input('Number of Features Machine:  %s' % (machine_name),
                                             min_value=int(0), max_value=int(8))
        machine_names[i] = machine_name

graph = graphviz.Digraph()
if machine_number >= 2:
    for i in range(len(machine_names)-1):
        graph.edge(machine_names[i], machine_names[i-1])
st.graphviz_chart(graph)


