import tkinter as tk
from PIL import Image, ImageTk
import os

# Creăm fereastra principală
root = tk.Tk()
root.title("Joc Interactiv")
root.attributes('-fullscreen', True)

fullscreen = True

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)

root.configure(bg="#D3E8F5")

# Lista cu întrebări, variante și imagini pentru răspunsuri
intrebari = [
    {
        "intrebare": "Ce faci dimineața când te ridici din pat?",
        "imagine": "imagine1.png",
        "variante": [
            {"text": "Mă spăl pe față și mă îmbrac", "corect": True, "imagine": "raspuns1.png"},
            {"text": "Mă culc din nou", "corect": False, "imagine": "raspuns2.png"},
            {"text": "Încep să mă joc cu jucăriile", "corect": False, "imagine": "raspuns3.png"}
        ]
    },
    {
        "intrebare": "Ce faci înainte de a mânca micul dejun?",
        "imagine": "imagine2.png",
        "variante": [
            {"text": "Îmi spăl mâinile", "corect": True, "imagine": "raspuns4.png"},
            {"text": "Ies afară", "corect": False, "imagine": "raspuns5.png"},
            {"text": "Mă pun în pat", "corect": False, "imagine": "raspuns6.png"}
        ]
    },
    {
        "intrebare": "Ce ai nevoie când ieși afară?",
        "imagine": "imagine3.png",
        "variante": [
            {"text": "Ochelari de soare", "corect": False, "imagine": "raspuns8.png"},
            {"text": "Umbrelă", "corect": True, "imagine": "raspuns7.png"},
            {"text": "Șlapi", "corect": False, "imagine": "raspuns9.png"}
        ]
    },
    {
        "intrebare": "Ce faci când te simți obosit după o zi lungă?",
        "imagine": "imagine4.png",
        "variante": [
            {"text": "Să te joci toată noaptea", "corect": False, "imagine": "raspuns10.png"},
            {"text": "Să bei foarte mult suc", "corect": False, "imagine": "raspuns11.png"},
            {"text": "Să îți iei puțin timp să te odihnești sau să te culci", "corect": True, "imagine": "raspuns12.png"}
        ]
    },
    {
        "intrebare": "Când trebuie să treci?",
        "imagine": "imagine5.png",
        "variante": [
            {"text": "Aici", "corect": True, "imagine": "raspuns13.png"},
            {"text": "Aici", "corect": False, "imagine": "raspuns14.png"},
        ]
    },
    {
        "intrebare": "Ce faci după ce ajungi acasă de la școală?",
        "imagine": "imagine6.png",
        "variante": [
            {"text": "Îmi fac temele", "corect": True, "imagine": "raspuns16.png"},
            {"text": "Alerg prin casă", "corect": False, "imagine": "raspuns17.png"},
            {"text": "Mă întind pe jos și mă culc", "corect": False, "imagine": "raspuns18.png"}
        ]
    },
    {
        "intrebare": "Ce faci în această situație?",
        "imagine": "imagine7.png",
        "variante": [
            {"text": "Mă pun să dorm", "corect": False, "imagine": "raspuns19.png"},
            {"text": "Fac curat", "corect": True, "imagine": "raspuns20.png"},
            {"text": "Mă apuc să mă joc", "corect": False, "imagine": "raspuns21.png"}
        ]
    },
    {
        "intrebare": "Ce faci după ce mănânci?",
        "imagine": "imagine8.png",
        "variante": [
            {"text": "Încep să arunc ce a rămas în farfurie", "corect": False, "imagine": "raspuns22.png"},
            {"text": "Pun farfuria in chiuveta și o spăl", "corect": True, "imagine": "raspuns23.png"},
            {"text": "Las farfuria pe masa", "corect": False, "imagine": "raspuns24.png"}
        ]
    },
    {
        "intrebare": "Ce faci înainte de culcare?",
        "imagine": "imagine9.png",
        "variante": [
            {"text": "Mă spăl pe dinți și mă pun în pijamale", "corect": True, "imagine": "raspuns25.png"},
            {"text": "Mănânc dulciuri", "corect": False, "imagine": "raspuns26.png"},
            {"text": "Mă uit la filme", "corect": False, "imagine": "raspuns27.png"}
        ]
    },
    {
        "intrebare": "Ce faci când termini de jucat?",
        "imagine": "imagine10.png",
        "variante": [
            {"text": "Îmi pun jucăriile la loc", "corect": True, "imagine": "raspuns28.png"},
            {"text": "Le las împrăștiate", "corect": False, "imagine": "raspuns29.png"},
            {"text": "Le arunc prin cameră", "corect": False, "imagine": "raspuns30.png"}
        ]
    }
]

index_intrebare = 0

# Cadrul pentru întrebare și imagine
question_frame = tk.Frame(root, bg="#D3E8F5", width=800, height=800)  # Mărire dimensiune cadru
question_frame.pack_propagate(False)
question_frame.pack(side=tk.LEFT, padx=40, pady=20, fill=tk.BOTH, expand=True)

intrebare_label = tk.Label(question_frame, text="", font=("Arial", 36, "bold"), bg="#D3E8F5", wraplength=700, justify="left")  # Font mai mare
intrebare_label.pack(pady=20)

img_label = tk.Label(question_frame, bg="#D3E8F5")
img_label.pack()

# Cadrul pentru răspunsuri
response_frame = tk.Frame(root, bg="#D3E8F5", width=800, height=800)  # Mărire dimensiune cadru
response_frame.pack_propagate(False)
response_frame.pack(side=tk.RIGHT, padx=40, pady=20, fill=tk.BOTH, expand=True)

# Mesajul pentru feedback (ajustare font și wraplength)
mesaj_label = tk.Label(root, text="", font=("Arial", 24), bg="#D3E8F5", wraplength=900, justify="center")  # Font mai mare
mesaj_label.pack(pady=40, padx=20)

# Label pentru imaginea de feedback
img_feedback_label = tk.Label(root, bg="#D3E8F5")
img_feedback_label.pack(pady=10)

buton_hai = tk.Button(root, text="➔", font=("Arial", 28), command=lambda: urmatoarea_intrebare())  # Font mai mare
buton_hai.pack_forget()

def afiseaza_intrebare():
    global index_intrebare
    buton_hai.pack_forget()
    mesaj_label.config(text="")
    img_feedback_label.config(image="")  # Resetăm imaginea de feedback

    # Reafișează întrebare și imagine la următoarea întrebare
    intrebare_label.pack(pady=20)
    img_label.pack()

    if index_intrebare < len(intrebari):
        img_path = intrebari[index_intrebare]["imagine"]
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((600, 600))  # Ajustează dimensiunea imaginii întrebării
            img_tk = ImageTk.PhotoImage(img)
            img_label.config(image=img_tk)
            img_label.image = img_tk
        else:
            img_label.config(image="")

        intrebare_label.config(text=intrebari[index_intrebare]["intrebare"])

        for widget in response_frame.winfo_children():
            widget.destroy()

        for raspuns in intrebari[index_intrebare]["variante"]:
            raspuns_frame = tk.Frame(response_frame, bg="#D3E8F5")
            raspuns_frame.pack(anchor="center", pady=20)

            rasp_img_path = raspuns["imagine"]
            if os.path.exists(rasp_img_path):
                img_raspuns = Image.open(rasp_img_path)
                img_raspuns = img_raspuns.resize((240, 240))
                img_raspuns_tk = ImageTk.PhotoImage(img_raspuns)
                img_label_raspuns = tk.Label(raspuns_frame, image=img_raspuns_tk, bg="#D3E8F5")
                img_label_raspuns.image = img_raspuns_tk
                img_label_raspuns.pack(side=tk.LEFT, padx=20)

            buton = tk.Button(raspuns_frame, text=raspuns["text"], font=("Arial", 24), command=lambda c=raspuns: verifica_raspuns(c), width=30, anchor="w")
            buton.pack(side=tk.LEFT, padx=20)

def verifica_raspuns(raspuns):
    global index_intrebare
    for widget in response_frame.winfo_children():
        widget.destroy()

    # Ascunde întrebare și imagine după alegerea răspunsului
    intrebare_label.pack_forget()
    img_label.pack_forget()

    # Afișează mesajul complet și ajustează lățimea și fontul mesajului
    if raspuns["corect"]:
        mesaj_label.config(text="Foarte bine!", fg="green", font=("Arial", 16), wraplength=300, width=40)
        
        feedback_image_path = "feedback_corect.png"
        if os.path.exists(feedback_image_path):
            feedback_img = Image.open(feedback_image_path)
            feedback_img = feedback_img.resize((300, 300))
            feedback_img_tk = ImageTk.PhotoImage(feedback_img)
            img_feedback_label.config(image=feedback_img_tk)
            img_feedback_label.image = feedback_img_tk
        else:
            img_feedback_label.config(image="")

        buton_hai.pack(pady=20)  # Afișează butonul "Hai mai departe" pentru a continua
    else:
        mesaj_label.config(text="Mai incearcă!", fg="red", font=("Arial", 16), wraplength=300, width=40)
        
        wrong_feedback_image_path = "feedback_gresit.png"
        if os.path.exists(wrong_feedback_image_path):
            wrong_feedback_img = Image.open(wrong_feedback_image_path)
            wrong_feedback_img = wrong_feedback_img.resize((300, 300))
            wrong_feedback_img_tk = ImageTk.PhotoImage(wrong_feedback_img)
            img_feedback_label.config(image=wrong_feedback_img_tk)
            img_feedback_label.image = wrong_feedback_img_tk
        else:
            img_feedback_label.config(image="")

        buton_hai.pack_forget()
        root.after(3000, afiseaza_intrebare)




def urmatoarea_intrebare():
    global index_intrebare
    index_intrebare += 1
    afiseaza_intrebare()

afiseaza_intrebare()

buton_fullscreen = tk.Button(root, text="Ieși din Fullscreen", font=("Arial", 18), command=toggle_fullscreen)  # Font mai mare
buton_fullscreen.place(x=root.winfo_screenwidth() - 220, y=20)

root.mainloop()
