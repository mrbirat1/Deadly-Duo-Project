"""
Test Cases for Parks and National Parks Explorer
Team: Deadly Duo (Birat Sapkota & Anup Kharel)
"""

import unittest
from parks_explorer import search_parks, filter_by_activity, get_all_activities, PARKS


class TestParksExplorer(unittest.TestCase):

    # -------------------------
    # Tests for search_parks()
    # -------------------------

    def test_search_by_name(self):
        """Search by park name should return matching parks."""
        results = search_parks("Yellowstone")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Yellowstone National Park")

    def test_search_by_location(self):
        """Search by location should return parks in that location."""
        results = search_parks("Australia")
        self.assertGreater(len(results), 0)
        for park in results:
            self.assertIn("Australia", park["location"])

    def test_search_case_insensitive(self):
        """Search should be case-insensitive."""
        results_lower = search_parks("yosemite")
        results_upper = search_parks("YOSEMITE")
        self.assertEqual(len(results_lower), len(results_upper))

    def test_search_no_results(self):
        """Search with no match should return empty list."""
        results = search_parks("xyznonexistent")
        self.assertEqual(results, [])

    def test_search_partial_keyword(self):
        """Search with partial keyword should still return results."""
        results = search_parks("Yello")
        self.assertGreater(len(results), 0)

    # --------------------------------
    # Tests for filter_by_activity()
    # --------------------------------

    def test_filter_by_hiking(self):
        """Filter by hiking should return parks with hiking."""
        results = filter_by_activity("hiking")
        self.assertGreater(len(results), 0)
        for park in results:
            self.assertIn("hiking", park["activities"])

    def test_filter_by_camping(self):
        """Filter by camping should return parks with camping."""
        results = filter_by_activity("camping")
        self.assertGreater(len(results), 0)
        for park in results:
            self.assertIn("camping", park["activities"])

    def test_filter_case_insensitive(self):
        """Activity filter should be case-insensitive."""
        results_lower = filter_by_activity("hiking")
        results_upper = filter_by_activity("HIKING")
        self.assertEqual(len(results_lower), len(results_upper))

    def test_filter_no_results(self):
        """Filter with non-existent activity should return empty list."""
        results = filter_by_activity("skydiving")
        self.assertEqual(results, [])

    # --------------------------------
    # Tests for get_all_activities()
    # --------------------------------

    def test_get_all_activities_returns_list(self):
        """get_all_activities should return a list."""
        activities = get_all_activities()
        self.assertIsInstance(activities, list)

    def test_get_all_activities_not_empty(self):
        """Activities list should not be empty."""
        activities = get_all_activities()
        self.assertGreater(len(activities), 0)

    def test_get_all_activities_sorted(self):
        """Activities list should be sorted alphabetically."""
        activities = get_all_activities()
        self.assertEqual(activities, sorted(activities))

    def test_get_all_activities_no_duplicates(self):
        """Activities list should have no duplicate entries."""
        activities = get_all_activities()
        self.assertEqual(len(activities), len(set(activities)))

    # -------------------------
    # Tests for PARKS database
    # -------------------------

    def test_parks_database_not_empty(self):
        """Parks database should contain parks."""
        self.assertGreater(len(PARKS), 0)

    def test_parks_have_required_fields(self):
        """Each park should have name, location, description, and activities."""
        for park in PARKS:
            self.assertIn("name", park)
            self.assertIn("location", park)
            self.assertIn("description", park)
            self.assertIn("activities", park)

    def test_parks_activities_are_lists(self):
        """Each park's activities field should be a list."""
        for park in PARKS:
            self.assertIsInstance(park["activities"], list)

    def test_parks_names_are_strings(self):
        """Each park name should be a non-empty string."""
        for park in PARKS:
            self.assertIsInstance(park["name"], str)
            self.assertGreater(len(park["name"]), 0)


if __name__ == "__main__":
    unittest.main()
