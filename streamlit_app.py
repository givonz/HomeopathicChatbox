import streamlit as st
import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="personal_collection2")

collection.add(
    documents=[
        "It affects the Mucous Membranes and Nerves. In stomach, it causes a catarrhal condition, which increases the patient’s hunger and craving for coarse food, such as pickles, radishes, turnips, etc. Patient wants to lie down, all the time, on account of nervous weakness and feels faint. In women, it causes uterine displacement, due to defective nutrition and debility. Peculiar sensations are-right lung and liver, feel hard and small; uterus feels soft. Lies with the legs drawn up.",
        "Easily fretful or quiet and careless.",
        "Feels, as if it is light or there is swimming in the head.",
        "Ravenous appetite. Tendency to eat, far beyond the capacity of digestion. Distension of abdomen and stomach, with palpitation.",
        "Sore feeling at the uterus better pressure. Uterus soft and feeble as if.",
        "Cold shivering, as if blood were ice-water.",
        "Clammy and sticky.",
        "It is a useful remedy, in many diseased conditions, when they are associated with gastric symptoms. It causes dyspepsia, with functional heart symptoms, especially in the aged persons. It is also useful, in indigestion of those, who abuse the drinking of tea and smoking, or chewing of tobacco. The chief, symptom in dyspepsia is a sensation, as if a hard boiled egg has lodged in the cardiac end of the stomach. Patients describe this sensation, as if a hard lump is felt in the pit of the stomach or in the lung which he wants to cough out.",
        "After eating.",
        "Very low spirited, unable to think or study.",
        "Total loss of appetite, in the morning, but craves food, at noon and at night. Pain in the stomach, always comes on after eating.",
        "Difficult breathing worse lying down. heart’s action heavy and slow, there may be tachycardia or bradycardia.",
        "Arnica montana is a traumatic remedy par excellence. Trauma in all its varieties – mental or physical and their effects recent or remote are met with by Arnica. It affects BLOOD, causing putrid and septic conditions. BLOOD VESSELS are relaxed, causing ecchymosis, blue-black spots; with TENDENCY To HAEMORRHAGE; epistaxis etc. It acts upon nerves causing neuralgia. Muscles feel VERY SORE, PAINFUL, BRUISED; all over. Parts become sore, after the pains, or after bleeding. It is a prophylactic for pus formation. Burrowing pus. Arnica has absorbent action. Progressive emaciation. Great prostration; tired feeling. Discharges are FOUL; breath, taste, flatus, stools etc. Crushing pain. BED FEELS HARD or full of lumps. Involuntary evacuations. Abscesses that do not mature. Pains of Arnica are paralytic; sudden, shifting pains from joint to joint. Arnica acts best in plethoric, dark, haired persons of rigid muscles, nervous sanguine nature. It acts but feebly on persons who are positively debilitated, with impoverished blood and soft flesh. Compound fractures. Twitching, in tendons, muscles. Osteomyelitis. Ill effects of fright, financial loss, anger, repentance; excessive use of any organ, vaginitis in females and impotence in males from excessive sexual indulgence. Exertion of any kind. Mind and uterine symptoms alternate. Complaints when over hurried. Apoplexy. Typhoid, septic fevers. Recurring boils. Surgical operations. Insect stings. Splinters. Thrombosis.",
        "INJURIES falls, blows, BRUISES; shock; jarring; after labour; over-exertion; sprains. TOUCH. After sleep. Motion. Old age. Alcohol. Damp cold. Coal gas. Lying on left side.",
        "Lying down and lying with head low or outstretched.",
        "FEAR; of being struck or touched; or approached; of sickness; of instant death; with cardiac distress at night; of space; on awakening; of crowds, public places. Morose, repentant mood. Mentally prostrate and apathetic, but physically restless; says nothing ails him. When spoken to, answers slowly with effort. Feels well in serious cases. Forgetful, what he reads, quickly escapes his mind. After rage sheds tears and makes exclamations. Hopeless; indifferent. Violent attacks of anguish – angina pectoris. Delirium tremens. A sudden fear that rouses one from sleep at night esp. after an accident. Great desire to scratch; will scratch, wall, bed, head, etc. Coma. Muttering delirium. Sensation of being good for nothing. Easily frightened, unexpected trifles cause him to start. Sits as if in thought.",
        "Brain; feels tired, burning in. Vertigo; chronic; of the aged; with nausea, vomiting and diarrhoea; objects whirl worse walking. Vertigo worse walking, sitting erect, closing eyes. Arnica has Headache as from a nail. Head hot with cold body. Cold spot on the forehead, hot spots on vertex. Meningitis from injury to head. Head throws backwards while walking.",
        "Bloodshot. Retinal haemorrhage. Photophobia. Feel tired and heavy, after sight seeing, moving pictures. High objects appear to lean forward and about to fall. Right eye protrudes, looks larger than left.",
        "Hardness of hearing; noises in ears. Blood from ears. Bruised pain in external ears. Hearing impaired from injury to the head. Sensitive to shrill noise.",
        "Bleeding; after every fit of coughing; after washing face. Violent sneezing from over-lifting. Nose; feels sore, cold. Post nasal dropping. Catarrh of antrum. Burning in typhoid fever.",
        "Ruddy congested, bluish red; in apoplexy, fevers. Sunken, pale. Lips; burn, swollen and cracked. Lower lip trembles, while eating. Lower jaw hangs down, paralysis. Painful acne. Cheeks puffed; red.",
        "Foetid breath. Dry, with much thirst. Taste; as from bad eggs, after operation- plugging etc. Bright red, puffy fauces. Tongue; dry, almost black. Swallowing is prevented by sort of nausea as if food would not go down.",
        "Eructations; tasting of bad eggs; after coughing. Loss of appetite by day, but canine hunger before midnight. Nausea. Vomiting of dark, red coagulated blood. Feeling as if stomach were passing against the spine. Foetid vomiting. As of a lump back of stomach. Arnica has aversion to milk and meat. Longing for vinegar. Constant desire to drink, but knows not what for, as all drinks are offensive.",
        "Cramps from epigastrium down over the bowels, then foul stools. Sharp pains from side to side. Stools; bloody, foamy, purulent, acrid; involuntary; during sleep; Dysentery; with dysuria, all summer and autumn. Cramps in rectum, while standing. Flatus smelling of rotten eggs. Must lie down after every stool. Prolapsus ani worse after walking for few minutes only better washing the whole body.",
        "Cutting pain in kidneys. Retention of urine in bladder, from over exertion, after labour is a keynote of Arnica. Involuntary dribbling, with constant urging. Arnica patient has to wait a long time for urine to pass. The bladder feels full and sore; the pressure of urine hurts him.",
        "Impotence from excess or abuse. Phimosis, from friction. Seminal emission during caress. Haematocele.",
        "After-pains worse suckling. Soreness of the parts after labour. Feeling as if foetus were lying crosswise. Cannot bear foetal movements; cause nausea and vomiting. Haemorrhage after coition. Nipples sore. Children lose their breath when angry. Mastitis. Threatened abortion from falls etc. Labour, weak and ceasing. Menses; early, hot, profuse. Soreness of the whole body during pregnancy. Tumours of mammae from injury. Puerperal fever.",
        "Hoarseness; worse exertion, colds, or getting wet. Cough in sleep without waking. Cough produced by yawning, weeping or lamenting. Child cries before paroxysms of whooping cough. Cough causes bloodshot eyes or epistaxis. Cardiac cough. Dyspnoea, with haemoptysis. Violent spasmodic cough, with facial herpes. Bones and cartilages of chest are painful worse motion, breathing or coughing. Heavy lower chest. Stitching pains in chest, taking the breath away; better pressure. Arnica also has hoarse voice from over use.",
        "Beats shake the whole body. Sudden pain as if the heart is squeezed or had got a shock, pain felt in left elbow (angina pectoris). Strain of heart from violent running. Cardiac dropsy. Hypertrophy of heart. Fatty heart. Heart pains; left to right. Pulse feeble and irregular. Weakened heart muscles. Horror of constant death, with cardiac distress at night. Palpitation after any exertion.",
        "Muscles of neck weak, head falls backwards, or any side. Back sore. Cervical vertebrae tender.",
        "In Arnica patient limbs ache as if beaten. Pain in arms better hanging down. Want of strength in the hands on grasping. Cramps in the fingers – writer’s cramp. Veins of hands distended. Cannot walk erect on account of bruised pain in pelvic region. Hygroma patellae. Gout. Knee joints suddenly bend when standing. Feet numb.",
        "Comatose drowsiness; drops to sleep as he answers. Dreams; of death mutilated bodies, anxious and terrible, awakes in terror, then sleepless. Severe fatigue causes restlessness and sleeplessness.",
        "Chilly with heat and redness of one cheek. Head or face alone hot, body cold. Coldness of part lain on. Thirst during chill. Must uncover but it chills him. Intermittent, typhoid, septic, traumatic fevers.",
        "Dusky, mottled. Every little hurt makes a black and blue spot. Very sore acne or crops of small boils. Symmetrical eruptions. Petechiae. Erysipelas. Bed sores. Tingling and itching which moves from place to place; after scratching, itching begins somewhere else. Carbuncle; of thigh.",
        "Bell-p; Echi; Hyper; Rhus-t.",
        "Acon; Calc; Nat-s; Psor; Rhus-t; Sul-ac."
    ],
    metadatas=[
        {"source": "Abies-canadensis-Generalities"},
        {"source": "Abies-canadensis-Mind"},
        {"source": "Abies-canadensis-Head"},
        {"source": "Abies-canadensis-Stomach"},
        {"source": "Abies-canadensis-Female"},
        {"source": "Abies-canadensis-Fever"},
        {"source": "Abies-canadensis-Skin"},
        {"source": "Abies-Nigra-Generalities"},
        {"source": "Abies-Nigra-Worse"},        
        {"source": "Abies-Nigra-Mind"},
        {"source": "Abies-Nigra-Stomach"},
        {"source": "Abies-Nigra-Chest"},
        {"source": "Arnica-Montana-Generalities"},
        {"source": "Arnica-Montana-Worse"},
        {"source": "Arnica-Montana-Better"},    
        {"source": "Arnica-Montana-Mind"}, 
        {"source": "Arnica-Montana-Head"},
        {"source": "Arnica-Montana-Eyes"},
        {"source": "Arnica-Montana-Ears"},    
        {"source": "Arnica-Montana-Nose"},
        {"source": "Arnica-Montana-Face"},
        {"source": "Arnica-Montana-Mouth"},
        {"source": "Arnica-Montana-Stomach"},     
        {"source": "Arnica-Montana-Abdomen"},
        {"source": "Arnica-Montana-Urinary-Organs"},    
        {"source": "Arnica-Montana-Male"},
        {"source": "Arnica-Montana-Females"},
        {"source": "Arnica-Montana-Respiratory-Organs"},
        {"source": "Arnica-Montana-Heart"},    
        {"source": "Arnica-Montana-Neck-and-Back"},
        {"source": "Arnica-Montana-Extremeties"},
        {"source": "Arnica-Montana-Sleep"},
        {"source": "Arnica-Montana-Fever"},
        {"source": "Arnica-Montana-Skin"},    
        {"source": "Arnica-Montana-Related"},
        {"source": "Arnica-Montana-Complementary"}
    ],
    ids=[
        "id01",
        "id02",
        "id03",
        "id04",
        "id05",
        "id06",
        "id07",
        "id08",
        "id09",
        "id10",
        "id11",
        "id12",
        "id13",
        "id14",
        "id15",
        "id16",
        "id17",
        "id18",
        "id19",
        "id20",
        "id21",
        "id22",
        "id23",
        "id24",
        "id25",
        "id26",
        "id27",
        "id28",
        "id29",
        "id30",
        "id31",
        "id32",
        "id33",
        "id34",
        "id35",
        "id36"
    ]
)

st.write("Homeopathic Chatbot")
#x=st.text_input("Symptom")
x=st.text_area("Symptoms:", height=200)
is_clicked=st.button("click here")
if is_clicked == 1:
     results=""

results = collection.query(
    query_texts=[x],
    n_results=5
)

st.text_area("Results",value=results,height=200)
