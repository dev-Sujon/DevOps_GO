import subprocess

def run_behave_tests():
    subprocess.run(["behave", "--format", "allure_behave.formatter:AllureFormatter", "--outfile=features/reports/allure-results"])

if __name__ == "__main__":
    run_behave_tests()
