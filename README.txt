Selected Pytest framework

Components & Features Pytest:
1.	Test Functions: 
•	Pytest allows you to define test functions using a simple naming convention.
•	Test functions should start with "test_" to be discovered by Pytest as test cases.

2.	Test Fixtures:
•	Fixtures in Pytest are functions that provide a set of data or resources needed for test cases.
•	Fixtures can be used to set up preconditions, initialize test objects, or provide test data.
•	They are defined using the @pytest.fixture decorator.

3.	Assertions:
•	Pytest provides a wide range of built-in assertions that you can use to validate the expected behaviour of your code.
•	These assertions make it easy to check conditions and compare values, simplifying the process of writing test cases.

4.	Test Discovery:
•	Pytest automatically discovers and runs test cases based on the defined naming conventions.
•	By default, it searches for files and directories with names starting with "test_" or ending with "_test.py" and executes the associated test functions.

5.	Test Execution and Reporting:
•	Pytest executes test cases and provides detailed reporting of the results, including information about passed, failed, and skipped tests.
•	It generates concise and informative output that highlights any failures or errors encountered during test execution.

6.	Test Parametrization:
•	Pytest allows you to parameterize test functions, enabling you to run the same test logic with different input values.
•	This feature is useful when you want to test a function or method with multiple sets of test data.

7.	Test Markers:
•	Pytest supports test markers, which are used to categorize or select specific tests for execution.
•	Markers can be used to run subsets of tests, skip certain tests, or apply custom behaviours and configurations to specific test cases.

8.	Test Coverage:
•	Pytest integrates with coverage tools, such as Coverage.py, to measure code coverage during test execution.
•	It helps identify which parts of your codebase are covered by tests and which areas may require additional testing.
