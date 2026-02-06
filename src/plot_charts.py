import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def plot_charts(model, user_data_scaled, predicted_risk_level, risk_level):
    if predicted_risk_level == 3:
        color = "red"
    elif predicted_risk_level == 2:
        color = "orange"
    elif predicted_risk_level == 1:
        color = "yellow"
    else:
        color = "green"

    col3, col4, col5 = st.columns([3,0.5,3])

    with col3:
        st.subheader("Student Risk Level:")

        fig = go.Figure(go.Pie(
            labels=["", ""],
            values=[1,0],
            hole=0.7,  
            marker=dict(colors=[color, color]),
            textinfo='none'
        ))

        fig.update_layout(
            showlegend = False,
            margin=dict(l=0,r=100,t=20,b=20),
            annotations=[dict(text=f"{risk_level}",
                            x=0.5, y=0.5, 
                            font_size=30, 
                            showarrow=False
                            )]
        )

        st.plotly_chart(fig)

    with col4:
        pass
        
    with col5:
        probs = model.predict_proba(user_data_scaled)[0]
        risk_labels = ["Low", "Moderate", "High", "Very High"]
        fig_probs = px.bar(
            x = risk_labels, 
            y = probs, 
            color = ["Low (GPA > 3.00)", "Moderate (2.50 < GPA < 3.00)", "High (2.00 < GPA < 2.50)", "Very High (GPA < 2.00)"],
            color_discrete_map = {"Low (GPA > 3.00)" : "green", 
                                  "Moderate (2.50 < GPA < 3.00)" : "yellow", 
                                  "High (2.00 < GPA < 2.50" : "orange", 
                                  "Very High (GPA < 2.00)" : "red"},
            
        )
        st.subheader("Risk Probabilities:")
        st.plotly_chart(fig_probs)
        
