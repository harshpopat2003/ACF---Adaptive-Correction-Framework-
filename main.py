import json
from tqdm import tqdm
from dotenv import load_dotenv
import os
from agent import *
from together import Together
from langchain_community.chat_models import ChatOpenAI

'''
Getting and Setting Keys
'''
load_dotenv()
together_api_key = os.getenv('TOGETHER_API_KEY')
open_ai_key = os.getenv('OPEN_AI_KEY')
os.environ['TOGETHER_API_KEY'] = together_api_key
os.environ['OPENAI_API_KEY'] = open_ai_key
#--------------------------------#
'''
Initialize Together API
'''
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
model = "google/gemma-2-27b-it"
#--------------------------------#

'''
Initialize OpenAI API
'''
llm_model = "gpt-4-turbo"
llm = ChatOpenAI(model=llm_model,)
#--------------------------------#

'''
Initialize Directory Paths
'''
GRAPH_RAG_DIR = './Graph_RAG'
DATASET_DIR = './Datasets'
RESULT_DIR = './Results'
#--------------------------------#

'''
Topic Mappings
'''
MMLU_Dict = {
    "Modern_Physics": "Modern_Physics",
    "Waves": "Waves",
    "Thermodynamics": "Thermodynamics",
    "Optics": "Optics",
    "Electromagnetism": "Electromagnetism",
    "Mechanics": "Mechanics"
}

SciEval_Dict = {
    "Work and Energy": "Mechanics",
    "Forces and Newton's Laws": "Mechanics",
    "Electrical Energy and Current": "Electromagnetism",
    "Sound": "Waves",
    "Heat": "Thermodynamics",
    "Interference and Diffraction": "Optics",
    "2D Motion": "Mechanics",
    "Subatomic Physics": "Modern Physics",
    "Circular Motion and Gravitation": "Gravitation",
    "Light and Reflection": "Optics",
    "Rotational Motion": "Mechanics",
    "Momentum and Collisions": "Mechanics",
    "Electric Forces and Fields": "Electromagnetism",
    "Waves and Vibrations": "Waves",
    "Fluid Mechanics": "Fluid",
    "Magnetism": "Electromagnetism",
    "Atomic Physics": "Modern Physics",
    "1D Motion": "Mechanics",
    "Thermodynamics": "Thermodynamics",
    "Electromagnetic Induction": "Electromagnetism",
    "Refraction": "Optics",
    "Circuits": "Electromagnetism"
}

PhysicsQA_Dict = {
    "Work Power Energy": "Mechanics",
    "Capacitor": "Electromagnetism",
    "Kinematics 1D": "Mechanics",
    "Alternating Current": "Electromagnetism",
    "Nuclear Physics": "Modern Physics",
    "Simple Harmonic Motion": "Waves",
    "Elasticity": "Elasticity",
    "Communication System": "Semiconductor",
    "Current Electricity": "Electromagnetism",
    "Kinetic Theory of Gases": "Thermodynamics",
    "Rotational Motion": "Mechanics",
    "Waves on String": "Waves",
    "Heat Transfer": "Thermodynamics",
    "Thermal Expansion": "Thermodynamics",
    "Sound Waves": "Waves",
    "Semiconductors": "Semiconductor",
    "Wave Optics": "Optics",
    "Fluid Mechanics": "Fluid",
    "Electrostatics": "Electromagnetism",
    "Magnetism": "Electromagnetism",
    "Friction": "Mechanics",
    "Electromagnetic Waves": "Electromagnetism",
    "Kinematics 2D": "Mechanics",
    "Radioactivity": "Modern Physics",
    "Thermodynamics": "Thermodynamics",
    "Gravitation": "Gravitation",
    "Electromagnetic Induction": "Electromagnetism",
    "Ray Optics": "Optics",
    "Centre of Mass": "Mechanics"
}
#--------------------------------#

def load_data(data_path):
    topic_dict = {}
    with open(data_path, 'r') as f:
        data = json.load(f)
    if 'MMLU' in data_path:
        topic_dict = MMLU_Dict
    elif 'SciEval' in data_path:
        topic_dict = SciEval_Dict
    elif 'PhysicsQA' in data_path:
        topic_dict = PhysicsQA_Dict
    for i in range(len(data)):
        data[i]['INPUT_DIR'] = topic_dict[data[i]['topic']]
    return data

def evaluate(filename, steps):
    results = []
    agent = MORA(llm, client, model, graph_llm, token_encoder, text_embedder, steps)
    data_path = f'{DATASET_DIR}/{filename}'
    result_path = f'{RESULT_DIR}/{filename}'
    data = load_data(data_path)

    for idx, item in enumerate(tqdm(data)):
        print("STARTED")
        result = item

        # print("Id: ", idx, "\n")
        # print("Question: ", item['question'], "\n")
        # print("LLM Response: ", item['response'], "\n")

        input_dir = f"{GRAPH_RAG_DIR}/{item['INPUT_DIR']}/output/ENTITES/artifacts"
        # LLM Response Refinement
        refined_solution, scratchpad = agent.run(input_dir, item['question'], item['response'], True)
        result['refined_solution'] = refined_solution
        result['scratchpad'] = scratchpad
        
        results.append(result)

    with open(result_path, 'w') as f:
        json.dump(results, f, indent=2)
    

if __name__ == "__main__":
    dataset_filename = 'PhysicsQA.json'
    max_steps = 1
    evaluate(dataset_filename, max_steps)




