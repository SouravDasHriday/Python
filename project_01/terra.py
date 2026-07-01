# importing a library
import subprocess
# Path where the Terraform files are located:
TERRAFORM_DIRECTORY = "/home/ubuntu/PYTHON_PRACTICE/terraform-automation/terraform"

# declering a function to run terraform commands:
def run_terraform(command):
    result = subprocess.run(
        command,
        cwd=TERRAFORM_DIRECTORY,
        capture_output=True,
        text=True,
        check=True
    )
    return result

# callign the function:
result = run_terraform(["terraform", "init"])
#result = run_terraform(["terraform", "plan"])
#result = run_terraform(["terraform", "apply", "-auto-approve"])
#result = run_terraform(["terraform", "destroy", "-auto-approve"])
print(result.stdout)





