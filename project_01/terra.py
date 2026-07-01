import subprocess

TERRAFORM_DIRECTORY = "/home/ubuntu/PYTHON_PRACTICE/project_01/terraform-automation/terraform"


def run_terraform(command):
    result = subprocess.run(
        command,
        cwd=TERRAFORM_DIRECTORY,
        capture_output=True,
        text=True,
        check=True
    )
    return result


try:
#    result = run_terraform(["terraform", "init"])
#    result = run_terraform(["terraform", "plan"])
#    result = run_terraform(["terraform", "apply", "-auto-approve"])
    result = run_terraform(["terraform", "destroy", "-auto-approve"])
    print(result.stdout)

except subprocess.CalledProcessError as error:
    print("Terraform command failed!\n")

    print("Return Code:", error.returncode)

    print("\n----- STDOUT -----")
    print(error.stdout)

    print("\n----- STDERR -----")
    print(error.stderr)
