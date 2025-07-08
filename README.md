# 🧮 Prevailing Interest Calculator

A simple and intuitive Streamlit web app to calculate the estimated interest earned from a **High Yield Savings Plus Account** based on user-inputted deposit amount and duration.

## 📌 Project Overview

This calculator helps users estimate their interest earnings over a specified time period using tiered interest rates:

- **First $50,000** → 1.5% p.a.
- **Next $25,000** → 1.6% p.a.
- **Next $25,000** → 1.8% p.a.
- **Amount over $100,000** → 2.0% p.a.

The app computes the interest based on the number of days between a user-specified start and end date.

## 🖼️ Demo Screenshot

![Screenshot](assets/screenshot.png) <!-- Replace with actual image path if you add one -->

## 🚀 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/interest-calculator-dashboard.git
   cd interest-calculator-dashboard
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a new conda environment**:
   ```bash
   conda env create -f environment.yml
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run interest_calculator.py
   ```

## 🧪 Example

Enter:
- A deposit amount (e.g., `$120,000`)
- A start and end date (e.g., `2024-01-01` to `2024-12-31`)

You will receive:
- Number of days
- Estimated interest earned (e.g., `$2,010.68`)

## 📦 Project Files

```
interest-calculator-dashboard/
├── notebooks/
│   └── interest_calculator.py     # Streamlit dashboard script
├── assets/
│   └── screenshot.png             # Optional: screenshot used in README
├── environment.yml                # Conda environment file
├── requirements.txt               # pip dependencies
├── .gitignore                     # Files to ignore in version control
├── README.md                      # Project documentation
```

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- datetime module

## 📎 License

This project is licensed under the [MIT License](LICENSE).

---

**Created with ❤️ using Streamlit**
