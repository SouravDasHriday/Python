# importing a library to run shell commands for terraform commands:
import subprocess

TERRAFORM_DIRECTORY = "/home/ubuntu/PYTHON_PRACTICE/project_01/terraform-automation/terraform" # terraform directory path

# declare a function to run terraform commands:
def run_terraform(command):
    result = subprocess.run(
        command,
        cwd=TERRAFORM_DIRECTORY,
        capture_output=True,
        text=True,
        check=True
    )
    return result


while True:
    print("\nAvailable Terraform Commands:")
    print("-----------------------------------")
    print("init")
    print("plan")
    print("apply")
    print("destroy")
    print("exit")
    user_input = input("\nEnter a Terraform command (or 'exit' to quit):  ").strip().lower()

    if user_input == "exit":
        print("Exiting the program.")
        break

    commands = {
            "init": ["terraform", "init"],
            "plan": ["terraform", "plan"],
            "apply": ["terraform", "apply", "-auto-approve"],
            "destroy": ["terraform", "destroy", "-auto-approve"],
            }

    try:
        if user_input in commands:
            command = commands[user_input]
            result = run_terraform(command)
            print("\n✅ Terraform command executed successfully.")
            print("\n------STDOUT------")
            print(result.stdout)
            print("\n------STDERR------")
            print(result.stderr)
        else:
            print("Invalid command. Please try again.")

    except subprocess.CalledProcessError as error:
        print("\n❌ Terraform command failed.")
        print("\nReturn code:", error.returncode)
        print("\n------STDOUT------")
        print(error.stdout)
        print("\n------STDERR------")
        print(error.stderr)
