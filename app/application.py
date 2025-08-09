from flask import Flask,render_template,request,session,redirect,url_for
from app.components.retriever import create_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urandom(24)

from markupsafe import Markup
def nl2br(value):
    return Markup(value.replace("\n" , "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br

@app.route("/" , methods=["GET","POST"])
# ... (imports aur baaki code same)

# ... (imports aur baaki code same)

# ... (imports, other functions same)

def index():
    if 'messages' not in session:
        session['messages'] = []
    
    if request.method == 'POST':
        user_input = request.form.get('prompt')
        if user_input:
            messages = session['messages']
            messages.append({'role': 'user', 'content': user_input})
            session['messages'] = messages
            
            try:
                qa_chain = create_qa_chain()
                # Temporary: Increase k for more context if needed (add in chain creation if not)
                # qa_chain.retriever.search_kwargs['k'] = 3
                
                response = qa_chain.invoke({"query": user_input})  # Dict pass kar – LangChain ke liye zaroori
                logger.info(f"Full response from invoke: {response}")  # Logs mein dekh structure ('result' ya 'answer'?)
                result = response.get('result', response.get('answer', 'No response'))  # Agar key 'answer' ho to fallback
                if not result or result == 'No response':
                    result = 'Sorry, no relevant medical info found in data.'  # Better message
                messages.append({'role': 'assistant', 'content': result})
                session['messages'] = messages
            except Exception as e:
                error_message = str(e)
                return render_template('index.html', messages=session.get('messages', []), error=error_message)
        
        return redirect(url_for('index'))
    
    return render_template('index.html', messages=session.get('messages', []))

# ... (clear aur run same)
    if 'messages' not in session:
        session['messages'] = []
    
    if request.method == 'POST':
        user_input = request.form.get('prompt')
        if user_input:
            messages = session['messages']
            messages.append({'role': 'user', 'content': user_input})
            session['messages'] = messages
            
            try:
                qa_chain = create_qa_chain()
                response = qa_chain.invoke({"query": user_input})  # Add {"query": user_input} – LangChain mein input dict chahiye
                result = response.get('result', 'No response')  # Yeh key confirm kar, agar 'answer' hai to change kar 'answer'
                messages.append({'role': 'assistant', 'content': result})
                session['messages'] = messages
            except Exception as e:
                error_message = str(e)
                return render_template('index.html', messages=session.get('messages', []), error=error_message)
        
        return redirect(url_for('index'))
    
    return render_template('index.html', messages=session.get('messages', []))

# ... (baaki code same)
# ... (baaki code same)

@app.route("/clear")
def clear():
    session.pop("messages" , None)
    return redirect(url_for("index"))
if __name__=="__main__":
    app.run(host="0.0.0.0" , port=5000 , debug=False , use_reloader = False)



