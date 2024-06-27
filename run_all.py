import subprocess


def run_script(script_path):
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_path}:")
        print(result.stderr)
        return False
    else:
        print(f"Successfully ran {script_path}:")
        print(result.stdout)
        return True


if __name__ == "__main__":
    scripts = [
        'scripts/download_data.py',
        'scripts/preprocess_data.py',
        'scripts/train_model.py',
        'scripts/evaluate_model.py'
    ]

    for script in scripts:
        success = run_script(script)
        if not success:
            print(f"Script {script} failed. Stopping execution.")
            break
