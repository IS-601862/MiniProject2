from pprint import pprint

import unittest2
from numpy.random import randint
from numpy.random import seed

from src.statistics.statistics import Statistics
from src.utilities.csvHelper import CsvReader

unittest2.TestLoader.sortTestMethodsUsing = None


class StatisticsTestCases(unittest2.TestCase):
    """Tests all functions in statistics module using csv file."""

    test_data = CsvReader('data/Test_Data.csv').data
    column1 = [int(row['value1']) for row in test_data]
    column2 = [int(row['value2']) for row in test_data]
    p_answers = CsvReader('data/Test_Proportion.csv').data
    z_answers = CsvReader('data/Test_ZScores.csv').data
    column_proportion = [float(row['Proportion']) for row in p_answers]
    column_zscore = [float(row['Z-Score']) for row in z_answers]
    test_answer = CsvReader('data/UnitTestStatsAnswers.csv').data
    sample_data = CsvReader('data/Test_Data_Sample.csv').data
    column3 = [int(row['sample1']) for row in sample_data]
    sample_answer = CsvReader('data/UnitTestSampleAnswers.csv').data

    def setUp(self) -> None:
        seed(5)
        # self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        for row in self.sample_answer:
            pprint(row["mean"])
            self.assertEqual(self.statistics.mean(self.column3), float(row['mean']))
            self.assertEqual(self.statistics.get_result, float(row['mean']))

    def test_population_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["mean"])
            self.assertEqual(self.statistics.population_mean(self.column1), float(row['mean']))
            self.assertEqual(self.statistics.get_result, float(row['mean']))

    def test_median_statistics(self):
        for row in self.test_answer:
            pprint(row["median"])
            self.assertEqual(self.statistics.median(self.column1), float(row['median']))
            self.assertEqual(self.statistics.get_result, float(row['median']))

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
            self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.statistics.get_result, float(row['mode']))

    def test_standard_deviation_statistics(self):
        for row in self.test_answer:
            pprint(row["stddev"])
            self.assertEqual(self.statistics.stddev(self.column1), float(row['stddev']))
            self.assertEqual(self.statistics.get_result, float(row['stddev']))

    def test_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['variance'])
            self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
            self.assertEqual(self.statistics.get_result, float(row['variance']))

    def test_proportion_statistics(self):
        self.assertEqual(self.statistics.proportion(self.column1).sort(), self.column_proportion.sort())
        self.assertEqual(self.statistics.get_result, self.column_proportion)

    def test_zscore_statistics(self):
        self.assertEqual(self.statistics.zscore(self.column1).sort(), self.column_zscore.sort())
        self.assertEqual(self.statistics.get_result, self.column_zscore)

    def test_correlation_statistics(self):
        for row in self.test_answer:
            pprint(row['correlation'])
            self.assertEqual(self.statistics.correlation_coefficient(self.column1, self.column2),
                             float(row['correlation']))
            self.assertEqual(self.statistics._result, float(row['correlation']))

    def test_skewness_statistics(self):
        for row in self.test_answer:
            pprint(row["skewness"])
            self.assertEqual(self.statistics.skewness(self.column1), float(row['skewness']))
            self.assertEqual(self.statistics.get_result, float(row['skewness']))

if __name__ == '__main__':
    unittest2.main()
