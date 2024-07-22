import pandas as pd
import streamlit as st

# Function to read data from multiple Excel files
def read_trainer_data(file_list):
    df_list = [pd.read_excel(file) for file in file_list]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Function to find trainer by name or email
def find_trainer(df, name=None, email=None):
    if name:
        filtered_df = df[df['Name'].str.contains(name, na=False, case=False)]
    elif email:
        filtered_df = df[df['Email'].str.contains(email, na=False, case=False)]
    else:
        filtered_df = pd.DataFrame()
    return filtered_df

# Streamlit app
def main():
    st.title("Trainer Engagement Processor")
    
    # File upload
    uploaded_files = st.file_uploader("Upload Excel files", accept_multiple_files=True, type="xlsx")
    if uploaded_files:
        file_list = [uploaded_file for uploaded_file in uploaded_files]
        df = read_trainer_data(file_list)
        
        # Search for trainer by name or email
        st.sidebar.header("Search Criteria")
        name = st.sidebar.text_input("Name")
        email = st.sidebar.text_input("Email")
        
        filtered_df = find_trainer(df, name=name, email=email)
        
        # Show filtered data
        st.subheader("Filtered Data")
        st.write(filtered_df)
        
        if not filtered_df.empty:
            selected_row = filtered_df.iloc[0]
            name = selected_row.get('Name', 'N/A')
            email = selected_row.get('Email', 'N/A')
            ttt_status = selected_row.get('TTT Status', 'N/A')
            
            st.subheader("Trainer Details")
            st.text(f"Name: {name}")
            st.text(f"Email: {email}")
            st.text(f"TTT Status: {ttt_status}")

if __name__ == "__main__":
    main()
