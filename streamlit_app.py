import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. Introduction ---
st.title("AI-Powered Marketing with Free WiFi Analytics")
st.write("""
This showcase demonstrates how Artificial Intelligence can be leveraged by data scientists to improve marketing strategies using data from free WiFi analytics in various physical locations. We'll explore examples from a general perspective and then delve into more specific scenarios with a Nigerian Restaurant and a Supermarket.
""")

# --- 2. What Kind of Data Can We Get? ---
st.subheader("2. Data from Free WiFi Analytics")
st.write("""
Free WiFi analytics can provide valuable insights into customer behavior in physical spaces. This includes:
- Visit frequency (new vs. returning visitors).
- Visit duration.
- Foot traffic within the venue.
- Dwell time in specific zones.
- Path analysis.
- Potentially demographic data (if collected during login) and preferences (if surveys are used).
""")

# --- 3. How AI Can Enhance Marketing ---
st.subheader("3. How AI Enhances Marketing")
st.write("""
AI techniques can analyze this data to provide deeper insights and enable more effective marketing:
- **Customer Segmentation:** Identifying groups of customers with similar behaviors or preferences.
- **Personalized Promotions:** Delivering targeted offers and recommendations.
- **Optimizing Operations:** Informing decisions about layout, product placement, and staffing.
- **Predictive Analytics:** Forecasting future customer behavior.
- **Automated Campaigns:** Triggering marketing messages based on real-time behavior.
""")

st.markdown("---")

# --- Use Case: Nigerian Restaurant ---
st.subheader("Advanced Use Case: Nigerian Restaurant")
st.write("Let's consider a Nigerian restaurant with local and continental dishes.")

np.random.seed(42)
num_restaurant_visitors = 300
restaurant_data = {
    'Visitor ID': range(1, num_restaurant_visitors + 1),
    'Arrival Time': pd.to_datetime(['2025-05-25 10:00:00'] * num_restaurant_visitors) + pd.to_timedelta(np.random.randint(0, 540, num_restaurant_visitors), unit='min'),
    'Duration (minutes)': np.random.randint(15, 90, num_restaurant_visitors),
    'Frequent Visitor': np.random.choice(['Yes', 'No'], num_restaurant_visitors, p=[0.4, 0.6]),
    'Meal Type Preference': np.random.choice(['Local', 'Continental', 'Both'], num_restaurant_visitors, p=[0.4, 0.3, 0.3]),
    'Time of Visit': np.random.choice(['Lunch', 'Dinner', 'Breakfast'], num_restaurant_visitors, p=[0.5, 0.3, 0.2])
}
restaurant_df = pd.DataFrame(restaurant_data)
st.dataframe(restaurant_df.head())

st.subheader("AI-Driven Segmentation: Restaurant")
st.write("AI clustering can segment customers. Here's a conceptual segmentation:")

def assign_restaurant_segment(row):
    if row['Frequent Visitor'] == 'Yes' and row['Time of Visit'] == 'Lunch' and row['Meal Type Preference'] in ['Local', 'Both']:
        return "Loyal Local Lunch Goers"
    elif row['Time of Visit'] == 'Dinner' and row['Meal Type Preference'] in ['Continental', 'Both']:
        return "Continental Dinner Enthusiasts"
    elif row['Time of Visit'] == 'Breakfast' and row['Frequent Visitor'] == 'Yes':
        return "Regular Breakfast Crowd"
    else:
        return "General Patrons"

restaurant_df['Segment'] = restaurant_df.apply(assign_restaurant_segment, axis=1)
restaurant_segment_counts = restaurant_df['Segment'].value_counts().reset_index()
restaurant_segment_counts.columns = ['Segment', 'Count']

fig_pie_rest = px.pie(restaurant_segment_counts, names='Segment', values='Count', title='Restaurant Customer Segments')
st.plotly_chart(fig_pie_rest)

st.subheader("AI-Powered Marketing: Restaurant")
st.write("Personalized marketing based on restaurant segments:")
for segment in restaurant_df['Segment'].unique():
    st.subheader(f"Segment: {segment}")
    segment_data = restaurant_df[restaurant_df['Segment'] == segment]
    st.write(f"Number of visitors in this segment: {len(segment_data)}")
    if segment == "Loyal Local Lunch Goers":
        st.markdown("- **AI Suggestion:** Offer a special discount on popular local dishes during lunchtime for frequent visitors.")
        st.markdown("- **Example:** 'Enjoy 15% off your favorite Nigerian dish this lunch!'")
    elif segment == "Continental Dinner Enthusiasts":
        st.markdown("- **AI Suggestion:** Promote new continental dishes or a special continental set menu for dinner.")
        st.markdown("- **Example:** 'Try our new Italian Platter this evening!'")
    elif segment == "Regular Breakfast Crowd":
        st.markdown("- **AI Suggestion:** Introduce a breakfast loyalty program or a new breakfast item.")
        st.markdown("- **Example:** 'Get a free coffee with your 5th breakfast order!'")
    elif segment == "General Patrons":
        st.markdown("- **AI Suggestion:** Target with general promotions or gather more preference data.")
        st.markdown("- **Example:** 'Welcome! Take our quick survey for a chance to win a free meal!'")

# --- Use Case: Supermarket ---
st.subheader("Advanced Use Case: Supermarket")
st.write("Now, let's look at a supermarket with various provisions.")

num_supermarket_visitors = 350
supermarket_data = {
    'Visitor ID': range(1, num_supermarket_visitors + 1),
    'Arrival Time': pd.to_datetime(['2025-05-25 11:00:00'] * num_supermarket_visitors) + pd.to_timedelta(np.random.randint(0, 720, num_supermarket_visitors), unit='min'),
    'Duration (minutes)': np.random.randint(10, 60, num_supermarket_visitors),
    'Frequent Visitor': np.random.choice(['Yes', 'No'], num_supermarket_visitors, p=[0.5, 0.5]),
    'Area of Interest': np.random.choice(['Produce', 'Groceries', 'Electronics', 'Home Goods', 'Snacks'], num_supermarket_visitors, p=[0.3, 0.4, 0.1, 0.1, 0.1])
}
supermarket_df = pd.DataFrame(supermarket_data)
st.dataframe(supermarket_df.head())

st.subheader("AI-Driven Segmentation: Supermarket")
st.write("AI can segment supermarket visitors based on their shopping behavior.")

def assign_supermarket_segment(row):
    if row['Frequent Visitor'] == 'Yes' and row['Area of Interest'] in ['Groceries', 'Produce']:
        return "Regular Grocery Shoppers"
    elif row['Area of Interest'] == 'Electronics' and row['Duration (minutes)'] > 30:
        return "Electronics Enthusiasts"
    elif row['Area of Interest'] == 'Snacks' and row['Duration (minutes)'] < 20:
        return "Quick Snack Buyers"
    else:
        return "General Shoppers"

supermarket_df['Segment'] = supermarket_df.apply(assign_supermarket_segment, axis=1)
supermarket_segment_counts = supermarket_df['Segment'].value_counts().reset_index()
supermarket_segment_counts.columns = ['Segment', 'Count']

fig_bar_supermarket = px.bar(supermarket_segment_counts, x='Segment', y='Count', title='Supermarket Customer Segments')
st.plotly_chart(fig_bar_supermarket)

st.subheader("AI-Powered Marketing: Supermarket")
st.write("Personalized marketing for supermarket segments:")
for segment in supermarket_df['Segment'].unique():
    st.subheader(f"Segment: {segment}")
    segment_data = supermarket_df[supermarket_df['Segment'] == segment]
    st.write(f"Number of visitors in this segment: {len(segment_data)}")
    if segment == "Regular Grocery Shoppers":
        st.markdown("- **AI Suggestion:** Offer discounts on frequently purchased groceries or introduce a subscription box for essentials.")
        st.markdown("- **Example:** 'Save 10% on your usual grocery items this week!'")
    elif segment == "Electronics Enthusiasts":
        st.markdown("- **AI Suggestion:** Notify them about new electronics arrivals or special offers on gadgets.")
        st.markdown("- **Example:** 'Check out the latest smartphones in our electronics section!'")
    elif segment == "Quick Snack Buyers":
        st.markdown("- **AI Suggestion:** Place promotional offers on snacks near the entrance or checkout.")
        st.markdown("- **Example:** 'Grab a discounted snack on your way out!'")
    elif segment == "General Shoppers":
        st.markdown("- **AI Suggestion:** Broad promotions or encourage them to explore different sections.")
        st.markdown("- **Example:** 'Discover new products throughout the store this week!'")

# --- Combined Insights ---
st.subheader("Combined Insights and AI's Role")
st.write("If the restaurant and supermarket are nearby, AI could help understand cross-shopping behavior.")
st.markdown("- **AI Role:** Association rule mining to find links between restaurant visits and supermarket purchases.")
st.markdown("- **Potential Insight:** Customers who frequent the restaurant for lunch might also buy certain grocery items.")
st.markdown("- **Marketing Potential:** Cross-promote between the two businesses.")

# Visualization 3: Restaurant Meal Type Preferences
meal_preference_counts = restaurant_df['Meal Type Preference'].value_counts().reset_index()
meal_preference_counts.columns = ['Meal Type', 'Count']
fig_bar_meal = px.bar(meal_preference_counts, x='Meal Type', y='Count', title='Restaurant Meal Type Preferences')
st.plotly_chart(fig_bar_meal)

st.subheader("4. Benefits for the Business")
st.write("""
Leveraging AI with WiFi analytics can lead to:
- Enhanced customer experience through personalization.
- Increased customer loyalty with relevant offers.
- Improved marketing ROI by targeting the right audiences.
- Data-driven decision-making for business operations.
""")

st.subheader("5. Privacy Considerations")
st.warning("""
Remember, ethical data handling is crucial. Real-world applications must prioritize:
- Anonymization of user data.
- Transparency about data collection.
- Compliance with privacy regulations.
""")

st.write("This showcase is written and Compiled by ZACHARIAH MESHACH illustrates how AI can be a powerful tool for data scientists to enhance marketing using free WiFi analytics.")
