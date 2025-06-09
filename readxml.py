from robot.api import ExecutionResult

def print_tests(suite):
    for test in suite.tests:
        print("I am in suite")
        print(f"Test is: {test.name} → {test.status}")
    for subsuite in suite.suites:
        print("I am in sub-suite")
        print_tests(subsuite)

result = ExecutionResult("output.xml")
print_tests(result.suite)

# Option2, should work for all xml
# from robot.api import ExecutionResult, ResultVisitor

# class MyVisitor(ResultVisitor):
#     def visit_test(self, test):
#         print(f"Visited test: {test.name} - {test.status}")

# result = ExecutionResult("output.xml")
# result.visit(MyVisitor())