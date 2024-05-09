class Job:
    def __init__(self):
        # Dictionary containing available jobs as keys and their descriptions and salaries as values
        self.availableJobs = {
            "Mental Health Technician\nJob Description : Provides care and support to individuals with mental health conditions.":
                "\nAverage Annual Salary : $77,448\n",
            "Loan Officer\nJob Description : Evaluates, authorizes, or recommends approval of loan applications.":
                "\nAverage Annual Salary : $192,339\n",
            "Mental Health Therapist\nJob Description :  Assesses and treats individuals with mental, emotional, or substance abuse problems.":
                "\nAverage Annual Salary : $76,410\n",
            "Electrical Engineer\nJob Description : Designs, develops, and tests electrical equipment and systems.":
                "\nAverage Annual Salary : $102,590\n",
            "Construction Project Manager\nJob Description : Plans and oversees construction projects to ensure they are completed in a timely and cost-effective manner.":
                "\nAverage Annual Salary : $103,431\n",
            "Mechanical Engineer\nJob Description : Designs, develops, and tests mechanical and thermal devices.":
                "\nAverage Annual Salary : $96,091\n",
            "Psychiatrist\nJob Description :  Diagnoses and treats mental illnesses through medication, psychotherapy, or a combination of both.":
                "\nAverage Annual Salary : $258,440\n",
            "Human Resources Manager\nJob Description :  Oversees the recruiting, interviewing, and hiring of new staff; consults with top executives on strategic planning.":
                "\nAverage Annual Salary : $79,174\n",
            "Senior Accountant\nJob Description : Prepares and examines financial records, ensuring accuracy and compliance with laws.":
                "\nAverage Annual Salary : $82,811\n",
            "Data Engineer\nJob Description : Develops, constructs, tests, and maintains architectures such as databases and large-scale processing systems.":
                "\nAverage Annual Salary : $130,135\n"
        }

        # Sorting the available jobs dictionary based on salary in descending order
        sorted_jobs = sorted(self.availableJobs.items(), key=lambda x: float(x[1].split('$')[-1].replace(',', '').strip()), reverse=True)
        # Creating a new dictionary from the sorted list of tuples
        self.sorted_jobs_dict = dict(sorted_jobs)

    def applyJobs(self):
        print("\nAVAILABLE JOBS")

        # Loop through the sorted jobs dictionary to display job options
        for index, (jobs, salary) in enumerate(self.sorted_jobs_dict.items(), 1):
            print(f"\n{index}.) {jobs}{salary}")

        while True:
            try:
                # Prompting the user to choose a job option
                userChoose = int(input("Choose what job you want to apply based on the rankings (press '0' to exit): "))

                if userChoose == 0:
                    break
                elif userChoose < 1 or userChoose > len(self.sorted_jobs_dict.items()):
                    # Checking if the user input is within the valid range
                    print("Number is not in the option, Please Try Again!")
                    continue
                else:
                    # Getting the selected job and its description
                    selected_jobs = list(self.sorted_jobs_dict.items())[userChoose - 1]
                    selected_jobs_description = selected_jobs[0]
                    selected_salary_description = selected_jobs[1]

                    # Displaying the selected job and salary
                    print(f"\nSuccessfully Applied to :\n{selected_jobs_description}{selected_salary_description}")

                    # Asking the user if they want to apply for more jobs
                    userApplyAgain = str(input("Do you want to apply more jobs (y/n)?: ")).lower()

                    try:
                        if userApplyAgain != "y":
                            # Exiting the loop if the user does not want to apply for more jobs
                            print("Thank You For Applying Make Sure To Check Your Gmail to see if there`s an email about the next screening of your application ^_^\n")
                            break
                        else:
                            continue
                    except TypeError:
                        # Handling invalid input for applying more jobs
                        print("Your option is an invalid letter, Please Try Again!")
                        continue

            except ValueError:
                # Handling non-numeric input for job selection
                print("Your option is not a number, Please Try Again!")
                continue

# Creating an instance of the Job class
jobApplicationPortalSystem = Job()
print("Welcome to Job Application Portal System!")
# Prompting the user to enter their Gmail
user_gmail = str(input("Enter your Gmail Here To Start: "))
# Calling the applyJobs method to start the application process
jobApplicationPortalSystem.applyJobs()
