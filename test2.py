from tkinter import *
import requests

def generate_resume():
    """
    Fetches resume content from the Gemini API and displays it in a text box.
    """
    # Replace with your actual Gemini API endpoint
    api_endpoint = "YOUR_GEMINI_API_ENDPOINT" 

    # Get user input (replace with actual input fields)
    name = name_entry.get()
    contact = contact_entry.get()
    summary = summary_entry.get("1.0", END)  # Get all text from text area
    experience = experience_entry.get("1.0", END)
    education = education_entry.get("1.0", END)
    skills = skills_entry.get("1.0", END)
    job_description = job_description_entry.get("1.0", END)

    # Prepare data for API request
    data = {
        "name": name,
        "contact": contact,
        "summary": summary,
        "workExperience": experience,
        "education": education,
        "skills": skills,
        "jobDescription": job_description
    }

    try:
        response = requests.post(api_endpoint, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        resume_text = response.json()["resume"]  # Assuming the API returns resume in JSON format

        # Display generated resume in the text box
        result_text.delete("1.0", END)  # Clear previous content
        result_text.insert(END, resume_text)

    except requests.exceptions.RequestException as e:
        result_text.delete("1.0", END)
        result_text.insert(END, f"Error generating resume: {e}")

# Create the main window
window = Tk()
window.title("AI Resume Builder")

# Create labels and input fields
name_label = Label(window, text="Name:")
name_entry = Entry(window)

contact_label = Label(window, text="Contact:")
contact_entry = Entry(window)

summary_label = Label(window, text="Summary/Objective:")
summary_entry = Text(window, height=5)

experience_label = Label(window, text="Work Experience:")
experience_entry = Text(window, height=5)

education_label = Label(window, text="Education:")
education_entry = Text(window, height=5)

skills_label = Label(window, text="Skills:")
skills_entry = Text(window, height=5)

job_description_label = Label(window, text="Job Description:")
job_description_entry = Text(window, height=5)

generate_button = Button(window, text="Generate Resume", command=generate_resume)

result_label = Label(window, text="Generated Resume:")
result_text = Text(window, height=15, width=80)

# Grid layout for organizing widgets
name_label.grid(row=0, column=0, sticky=W)
name_entry.grid(row=0, column=1)

contact_label.grid(row=1, column=0, sticky=W)
contact_entry.grid(row=1, column=1)

summary_label.grid(row=2, column=0, sticky=W)
summary_entry.grid(row=2, column=1, rowspan=2)

experience_label.grid(row=4, column=0, sticky=W)
experience_entry.grid(row=4, column=1, rowspan=2)

education_label.grid(row=6, column=0, sticky=W)
education_entry.grid(row=6, column=1, rowspan=2)

skills_label.grid(row=8, column=0, sticky=W)
skills_entry.grid(row=8, column=1, rowspan=2)

job_description_label.grid(row=10, column=0, sticky=W)
job_description_entry.grid(row=10, column=1, rowspan=3)

generate_button.grid(row=13, column=1)

result_label.grid(row=14, column=0, sticky=W)
result_text.grid(row=15, column=0, columnspan=2)

window.mainloop()