"""
Parks and National Parks Explorer
Team: Deadly Duo (Birat Sapkota & Anup Kharel)
Description: A Python application that displays information about parks
             and national parks, with search and filter features.
"""

# Park database
PARKS = [
    {
        "name": "Royal National Park",
        "location": "New South Wales, Australia",
        "description": "The world's second oldest national park, featuring coastal walks, beaches, and rainforest.",
        "activities": ["hiking", "camping", "sightseeing", "swimming"]
    },
    {
        "name": "Blue Mountains National Park",
        "location": "New South Wales, Australia",
        "description": "Famous for the Three Sisters rock formation, stunning valleys, and eucalyptus forests.",
        "activities": ["hiking", "sightseeing", "camping", "rock climbing"]
    },
    {
        "name": "Yellowstone National Park",
        "location": "Wyoming, USA",
        "description": "America's first national park, known for geysers, hot springs, and diverse wildlife.",
        "activities": ["hiking", "camping", "sightseeing", "wildlife watching"]
    },
    {
        "name": "Yosemite National Park",
        "location": "California, USA",
        "description": "Known for its towering cliffs, waterfalls, giant sequoias, and stunning valley views.",
        "activities": ["hiking", "camping", "rock climbing", "sightseeing"]
    },
    {
        "name": "Fiordland National Park",
        "location": "South Island, New Zealand",
        "description": "Home to Milford Sound and Doubtful Sound, with dramatic fiords and rainforest.",
        "activities": ["hiking", "kayaking", "sightseeing", "wildlife watching"]
    },
    {
        "name": "Banff National Park",
        "location": "Alberta, Canada",
        "description": "Canada's oldest national park featuring turquoise lakes, glaciers, and Rocky Mountain peaks.",
        "activities": ["hiking", "camping", "skiing", "sightseeing"]
    },
    {
        "name": "Kakadu National Park",
        "location": "Northern Territory, Australia",
        "description": "A UNESCO World Heritage site with ancient Aboriginal rock art and diverse ecosystems.",
        "activities": ["hiking", "sightseeing", "wildlife watching", "camping"]
    },
    {
        "name": "Grand Canyon National Park",
        "location": "Arizona, USA",
        "description": "One of the world's greatest natural wonders, carved by the Colorado River over millions of years.",
        "activities": ["hiking", "sightseeing", "camping", "rafting"]
    }
]


def display_all_parks():
    """Display all parks in the database."""
    print("\n" + "=" * 60)
    print("       PARKS AND NATIONAL PARKS EXPLORER")
    print("=" * 60)
    print(f"Total parks available: {len(PARKS)}\n")
    for i, park in enumerate(PARKS, 1):
        print(f"{i}. {park['name']}")
        print(f"   Location   : {park['location']}")
        print(f"   Description: {park['description']}")
        print(f"   Activities : {', '.join(park['activities'])}")
        print()


def search_parks(keyword):
    """
    Search parks by keyword in name, location, or description.
    Returns a list of matching parks.
    """
    keyword = keyword.lower()
    results = [
        park for park in PARKS
        if keyword in park["name"].lower()
        or keyword in park["location"].lower()
        or keyword in park["description"].lower()
    ]
    return results


def filter_by_activity(activity):
    """
    Filter parks by a specific activity.
    Returns a list of parks that offer the given activity.
    """
    activity = activity.lower()
    results = [park for park in PARKS if activity in park["activities"]]
    return results


def display_parks(parks):
    """Display a list of parks."""
    if not parks:
        print("\nNo parks found matching your criteria.")
        return
    print(f"\nFound {len(parks)} park(s):\n")
    for i, park in enumerate(parks, 1):
        print(f"{i}. {park['name']}")
        print(f"   Location   : {park['location']}")
        print(f"   Description: {park['description']}")
        print(f"   Activities : {', '.join(park['activities'])}")
        print()


def get_all_activities():
    """Return a sorted list of all unique activities across all parks."""
    activities = set()
    for park in PARKS:
        activities.update(park["activities"])
    return sorted(activities)


def main():
    """Main function to run the Parks Explorer application."""
    while True:
        print("\n" + "=" * 60)
        print("         PARKS AND NATIONAL PARKS EXPLORER")
        print("              Team: Deadly Duo")
        print("=" * 60)
        print("1. View all parks")
        print("2. Search parks by keyword")
        print("3. Filter parks by activity")
        print("4. View all available activities")
        print("5. Exit")
        print("-" * 60)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_all_parks()

        elif choice == "2":
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                results = search_parks(keyword)
                display_parks(results)
            else:
                print("Please enter a valid keyword.")

        elif choice == "3":
            activities = get_all_activities()
            print("\nAvailable activities:")
            for act in activities:
                print(f"  - {act}")
            activity = input("\nEnter activity to filter by: ").strip()
            if activity:
                results = filter_by_activity(activity)
                display_parks(results)
            else:
                print("Please enter a valid activity.")

        elif choice == "4":
            activities = get_all_activities()
            print("\nAll available activities:")
            for act in activities:
                print(f"  - {act}")

        elif choice == "5":
            print("\nThank you for using Parks and National Parks Explorer!")
            print("Team Deadly Duo - Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
