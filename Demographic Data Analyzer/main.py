from data_loader import DataLoader
from demographic_analyzer import DemographicAnalyzer

def print_divider():

    print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    loader = DataLoader()
    loader.load_data()
    data = loader.get_data()

    analyzer = DemographicAnalyzer(data)

    print_divider()
    print("📊 **Demographic Data Analysis** 📊")
    print_divider()

    print("1️⃣ **Number of each race:**")
    print(analyzer.get_race_count().to_string())
    print_divider()

    print("2️⃣ **Average age of men:**")
    print(f"   {analyzer.get_average_age_men()} years")
    print_divider()

    print("3️⃣ **Percentage with Bachelors degrees:**")
    print(f"   {analyzer.get_percentage_bachelors()}%")
    print_divider()

    print("4️⃣ **Percentage with higher education that earn >50K:**")
    print(f"   {analyzer.get_higher_education_rich()}%")
    print_divider()

    print("5️⃣ **Percentage without higher education that earn >50K:**")
    print(f"   {analyzer.get_lower_education_rich()}%")
    print_divider()

    print("6️⃣ **Minimum work time:**")
    print(f"   {analyzer.get_min_work_hours()} hours per week")
    print_divider()

    print("7️⃣ **Percentage of rich among those who work the fewest hours:**")
    print(f"   {analyzer.get_rich_percentage_min_hours()}%")
    print_divider()

    highest_country, highest_percentage = analyzer.get_highest_earning_country()
    print("8️⃣ **Country with the highest percentage of rich:**")
    print(f"   {highest_country} ({highest_percentage}%)")
    print_divider()

    print("9️⃣ **Most popular occupation for those who earn >50K in India:**")
    print(f"   {analyzer.get_most_common_occupation_india()}")
    print_divider()
