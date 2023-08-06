import openai 
import json
from flask import Flask, jsonify, request
app = Flask(__name__)
openai.api_key = "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"

def ask_question(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 engine
        prompt=prompt,
        max_tokens=150,  # Set the desired length of the answer
        temperature=0.7,  # Higher value increases randomness, lower makes it more deterministic
        n=1,  # Number of responses to generate
        stop=None,  # Stop generation at this token
    )

    if response and response['choices'] and 'text' in response['choices'][0]:
        answer = response['choices'][0]['text'].strip()
        return answer
    else:
        return "Sorry, I couldn't generate an answer at the moment."

@app.route('/ask', methods=['POST'])
def ask():
   
   # data = request.json  # Assuming JSON data is received
 #if request.is_json:
   if 'json_file' in request.files:
    json_file = request.files['json_file']
    if json_file.content_type == 'application/json':
                # Load the JSON data from the uploaded file
                data = json.loads(json_file.read())
                
    question = data['question']
    uploaded_data = data['uploaded_data']  # This should be the content from the uploaded files
   
    # Combine question and uploaded data context to create the prompt
   prompt = f"Question: {question}\nContext: {uploaded_data}\n"
    
    # Call the function to get the answer from GPT-3.5
   answer = ask_question(prompt)

    # Return the answer as a JSON response
   return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"
# @app.route("/chatbot/<string:txt>")
# def chatbot(txt):
#     return txt

# if __name__ == "__main__":
#     app.run(debug=True)
