import re
import random
import requests

# List of tech quotes
TECH_QUOTES = [
    "\"The best way to predict the future is to invent it.\" — Alan Kay",
    "\"It's not a bug – it's an undocumented feature.\" — Anonymous",
    "\"Java is to JavaScript what car is to carpet.\" — Chris Heilmann",
    "\"Code is like humor. When you have to explain it, it's bad.\" — Cory House",
    "\"First, solve the problem. Then, write the code.\" — John Johnson",
    "\"Any fool can write code that a computer can understand. Good programmers write code that humans can understand.\" — Martin Fowler",
    "\"If debugging is the process of removing software bugs, then programming must be the process of putting them in.\" — Edsger Dijkstra",
    "\"The function of good software is to make the complex appear to be simple.\" — Grady Booch",
    "\"Talk is cheap. Show me the code.\" — Linus Torvalds",
    "\"Programs must be written for people to read, and only incidentally for machines to execute.\" — Harold Abelson",
    "\"Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.\" — John Woods",
    "\"Simplicity is the soul of efficiency.\" — Austin Freeman",
    "\"Software is a great combination of artistry and engineering.\" — Bill Gates",
    "\"Computers are good at following instructions, but not at reading your mind.\" — Donald Knuth",
    "\"The most disastrous thing that you can ever learn is your first programming language.\" — Alan Kay",
    "\"The computer was born to solve problems that did not exist before.\" — Bill Gates",
    "\"The most important property of a program is whether it accomplishes the intention of its user.\" — C.A.R. Hoare",
    "\"Software is like entropy: It is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics; i.e., it always increases.\" — Norman Augustine",
    "\"One of the best programming skills you can have is knowing when to walk away for a while.\" — Oscar Godson",
    "\"Without requirements or design, programming is the art of adding bugs to an empty text file.\" — Louis Srygley"
]

def update_readme_quote():
    try:
        # Optional: You could also fetch quotes from an API instead
        # response = requests.get("https://programming-quotesapi.vercel.app/api/random")
        # quote = response.json()["quote"]
        
        # For now, let's use our predefined list
        quote = random.choice(TECH_QUOTES)
        
        # Read the README file
        with open("README.md", "r", encoding="utf-8") as file:
            readme_content = file.read()
        
        # Replace the quote
        new_content = re.sub(
            r"<!-- QUOTE:START -->\n.*\n<!-- QUOTE:END -->",
            f"<!-- QUOTE:START -->\n          {quote}\n          <!-- QUOTE:END -->",
            readme_content,
            flags=re.DOTALL
        )
        
        # Write the new content back to the README
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(new_content)
            
        print("Successfully updated the daily quote.")
    
    except Exception as e:
        print(f"Error updating quote: {e}")

if __name__ == "__main__":
    update_readme_quote()
