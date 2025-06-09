import sys
import os
import json
from robot.api import ExecutionResult

def extract_suite_data(suite):
    suite_data = {
        "name": suite.name,
        "tests": [],
        "suites": []
    }

    for test in suite.tests:
        suite_data["tests"].append({
            "name": test.name,
            "status": test.status,
            "start": test.starttime or "",
            "end": test.endtime or ""
        })

    for subsuite in suite.suites:
        child_data = extract_suite_data(subsuite)
        if child_data:
            suite_data["suites"].append(child_data)

    return suite_data if suite_data["tests"] or suite_data["suites"] else None

def save_robot_results_to_json(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    try:
        result = ExecutionResult(input_path)
        data = extract_suite_data(result.suite)

        if not data:
            print("⚠️ No test data found.")
            return

        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Results saved to {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python robot_to_json.py <input_output.xml> [output.json]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "robot_nested_results.json"
        save_robot_results_to_json(input_file, output_file)
