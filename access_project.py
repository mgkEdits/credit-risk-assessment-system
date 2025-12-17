import webbrowser
import time

def main():
    """
    This script serves as a gateway to the project hosted on Kaggle.
    Since the dataset involves millions of records (Freddie Mac),
    the computation and storage are handled in the Kaggle environment.
    """
    
    # --- CONFIGURATION ---
    # Replace these with your actual URLs
    KAGGLE_NOTEBOOK_URL = "https://www.kaggle.com/code/elijahnyasiando/creditriskmodel-masterdataset"
    DATASET_URL = "https://www.kaggle.com/datasets/elijahnyasiando/2018-2019-small-loans-data/data" 
    # Or the official Freddie Mac link if you didn't upload the dataset publicly
    
    print("="*60)
    print("      🏦 CREDIT RISK ASSESSMENT SYSTEM LAUNCHER")
    print("="*60)
    print("\n[INFO] This project uses the Freddie Mac Single-Family Dataset (3M+ records).")
    print("[INFO] Due to size constraints, the full analysis environment is hosted on Kaggle.")
    
    print("\nSelect an option:")
    print("1. Open Project Notebook (Source Code & Analysis)")
    print("2. Open Dataset Source")
    print("3. Exit")
    
    choice = input("\nEnter choice (1/2/3): ")
    
    if choice == '1':
        print(f"\n🚀 Redirecting to Notebook: {KAGGLE_NOTEBOOK_URL}...")
        time.sleep(1)
        webbrowser.open(KAGGLE_NOTEBOOK_URL)
    elif choice == '2':
        print(f"\n📂 Redirecting to Dataset: {DATASET_URL}...")
        time.sleep(1)
        webbrowser.open(DATASET_URL)
    elif choice == '3':
        print("\nExiting. You can find the links in the README.md file.")
    else:
        print("\nInvalid selection.")

if __name__ == "__main__":
    main()
