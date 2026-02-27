import pandas as pd

# Function to load CSV data
def load_csv(file_path):
    return pd.read_csv(file_path)

# Function to display for a coach
def coach_display(df):
    print("\n--- Coach Dashboard ---")
    print(f"Total Calories Burned: {df['Calories'].sum()}")
    print(f"Total Active Minutes: {df['Active minutes'].sum()}")
    print(f"Avg Heart Rate: {df['Heart rate'].mean():.2f}")
    print(f"Avg Stress Levels: {df['Stress levels'].mean():.2f}")
    print(f"Fall Detection Incidents: {df[df['Fall detection'] == 'Yes'].shape[0]}")

# Function to display for a trainer
def trainer_display(df):
    print("\n--- Trainer Dashboard ---")
    print(f"Avg ECG: {df['ECG'].mean():.2f}")
    print(f"Avg Blood Oxygen (SpO2): {df['Blood oxygen (SpO2)'].mean():.2f}%")
    print(f"Avg Body Composition (Fat %): {df['Body composition'].mean():.2f}%")
    print(f"Avg Energy Score: {df['Energy score'].mean():.2f}")
    
# Function to display for a team doctor
def team_doctor_display(df):
    print("\n--- Team Doctor Dashboard ---")
    print(f"Avg Sleep Stages: Deep={df['Sleep stages (deep)'].mean():.2f}, Light={df['Sleep stages (light)'].mean():.2f}")
    print(f"Avg Blood Pressure: {df['Blood pressure'].mean():.2f}")
    print(f"Avg Antioxidant Index (Carotenoids): {df['Antioxidant index'].mean():.2f}")
    print(f"Avg Stress Levels: {df['Stress levels'].mean():.2f}")
    print(f"Menstrual Cycle Data: {df['Menstrual cycle'].value_counts()}")

# Function to display for an athlete
def athlete_display(df):
    print("\n--- Athlete Dashboard ---")
    print(f"Avg Calories Burned: {df['Calories'].mean():.2f}")
    print(f"Avg Active Minutes: {df['Active minutes'].mean():.2f}")
    print(f"Avg Heart Rate: {df['Heart rate'].mean():.2f}")
    print(f"Avg Sleep Stages (Deep): {df['Sleep stages (deep)'].mean():.2f} minutes")
    print(f"Avg Fall Detection Incidents: {df[df['Fall detection'] == 'Yes'].shape[0]}")
    print(f"Energy Score: {df['Energy score'].mean():.2f}")
    print(f"Avg Stress Levels: {df['Stress levels'].mean():.2f}")

# Main function to process the file and user input
def main():
    # Get user input for file path and role
    file_path = input("Enter the path to the CSV file: ")
    
    # Load the CSV data
    try:
        df = load_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    # Check that necessary columns exist
    required_columns = [
        'Calories', 'Active minutes', 'Heart rate', 'ECG', 'Blood oxygen (SpO2)', 
        'Menstrual cycle', 'Stress levels', 'Body composition', 'Sleep stages (deep)', 
        'Sleep stages (light)', 'Energy score', 'Blood pressure', 'Antioxidant index', 
        'Fall detection'
    ]
    
    if not all(col in df.columns for col in required_columns):
        print("CSV file is missing required columns.")
        return
    
    # Get user role input
    role = input("Enter your role (coach/trainer/team_doctor/athlete): ").lower()
    
    # Display relevant data based on the role
    if role == 'coach':
        coach_display(df)
    elif role == 'trainer':
        trainer_display(df)
    elif role == 'team_doctor':
        team_doctor_display(df)
    elif role == 'athlete':
        athlete_display(df)
    else:
        print("Invalid role entered.")

if __name__ == "__main__":
    main()
