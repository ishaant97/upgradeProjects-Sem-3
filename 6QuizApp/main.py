import tkinter as tk
import json


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")

        # Load questions from a JSON file
        self.questions = self.load_questions("questions.json")

        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar(value=None)
        self.wrong_answers = []
        self.score_window = None
        self.timer = 30
        self.timer_id = None

        # Enable fullscreen mode
        root.attributes('-fullscreen', True)

        # Create the label to display the question
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack()

        # Create radio buttons for answer options
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(
                root, text="", variable=self.selected_option, value=str(i+1))
            self.option_buttons.append(option_button)
            option_button.pack()

        # Create "Next" and "Finish Test" buttons
        self.next_button = tk.Button(
            root, text="Next", command=self.check_answer, fg="black")
        self.next_button.pack()

        self.finish_button = tk.Button(
            root, text="Finish Test", command=self.finish_test, fg="black")
        self.finish_button.pack()

        # Create label to display the score
        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        # Create label to display the timer
        self.timer_label = tk.Label(
            root, text="", font=("Arial", 14), fg="black")
        self.timer_label.pack(side=tk.RIGHT)

        # Load the first question and start the timer
        self.load_next_question()
        self.update_timer()

    def load_questions(self, filename):
        # Load questions from a JSON file
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions

    def load_next_question(self):
        # Load the next question and update the UI
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text = question_data["question"]
            options = question_data["options"]
            self.correct_answer = question_data["correct_answer"]
            self.question_label.config(
                text=f"Q{self.current_question + 1}: {question_text}")
            for i, option_button in enumerate(self.option_buttons):
                option_button.config(text=options[i])
            self.selected_option.set(None)
        else:
            # All questions have been answered, submit the quiz
            self.submit_quiz()

    def check_answer(self):
        # Check the selected answer and update the score
        if self.selected_option.get():
            selected_answer = int(self.selected_option.get())
            if selected_answer == self.correct_answer:
                self.score += 1
            else:
                self.wrong_answers.append(self.current_question + 1)
            self.current_question += 1
            self.load_next_question()

    def submit_quiz(self):
        # Display the score and disable buttons
        self.show_score_and_wrong_answers()
        self.next_button.config(state="disabled")
        self.finish_button.config(state="disabled")
        self.timer_label.config(text="Time's up!")
        self.stop_timer()

    def show_score_and_wrong_answers(self):
        # Display the score and list of wrong answers
        score_text = f"Your score: {self.score}/{len(self.questions)}"
        wrong_answers_text = ""
        if self.wrong_answers:
            wrong_answers_text = "\nWrong Answers:\n"
            for question_number in self.wrong_answers:
                question_data = self.questions[question_number - 1]
                question_text = question_data["question"]
                correct_answer = question_data["options"][question_data["correct_answer"] - 1]
                wrong_answers_text += f"Q{question_number}: {question_text}\nCorrect Answer: {correct_answer}\n"

        # Create a score window to display the results
        self.score_window = tk.Toplevel(self.root)
        self.score_window.title("Quiz Score")
        score_label = tk.Label(
            self.score_window, text=score_text + wrong_answers_text, font=("Arial", 14))
        score_label.pack()

        # Add a button to retake the quiz
        retry_button = tk.Button(
            self.score_window, text="Retake Quiz", command=self.restart_quiz)
        retry_button.pack()

    def restart_quiz(self):
        # Reset the quiz to its initial state
        self.current_question = 0
        self.score = 0
        self.wrong_answers = []
        self.next_button.config(state="active")
        self.finish_button.config(state="active")
        self.score_label.config(text="")
        self.timer = 30
        self.load_next_question()
        self.update_timer()

        if self.score_window and self.score_window.winfo_exists():
            self.score_window.withdraw()

    def finish_test(self):
        # Finish the test (same as submitting)
        self.submit_quiz()

    def update_timer(self):
        if self.timer > 0:
            # Update the timer label and button colors
            timer_color = "red" if self.timer < 10 else "black"
            self.timer_label.config(
                text=f"Time Left: {self.timer} sec", fg=timer_color)

            next_button_color = "green" if self.timer > 10 else "black"
            finish_button_color = "red" if self.timer <= 10 else "black"

            self.next_button.config(fg=next_button_color)
            self.finish_button.config(fg=finish_button_color)

            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.timer == 0:
            # Timer has reached zero, submit the quiz
            self.submit_quiz()
            self.timer = -1

    def stop_timer(self):
        # Stop the timer (cancel timer event)
        if self.timer_id:
            self.root.after_cancel(self.timer_id)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
