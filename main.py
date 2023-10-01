import tkinter as tk

# Créez une fenêtre
root = tk.Tk()
root.title("Système de Chat")
root.geometry("400x300")  # Définir la taille de la fenêtre

# Couleurs personnalisées
bg_color = "#F6D55C"  # Couleur de fond
text_color = "#3CAEA3"  # Couleur du texte
button_color = "#ED553B"  # Couleur du bouton

# Configurez la couleur de fond de la fenêtre
root.configure(bg=bg_color)

# Ajoutez une étiquette avec une couleur de texte personnalisée
label = tk.Label(root, text="Bienvenue dans le système de chat!", bg=bg_color, fg=text_color, font=("Arial", 16))
label.pack(pady=20)  # Ajoutez un espacement en bas

# Ajoutez un bouton avec une couleur de fond personnalisée
button = tk.Button(root, text="Cliquez-moi", bg=button_color, fg="white", font=("Arial", 12))
button.pack()

# Ajoutez un champ de texte
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)  # Ajoutez un espacement en bas

# Ajoutez une zone de texte avec une couleur de fond personnalisée
text_widget = tk.Text(root, height=10, width=40, bg=bg_color, fg=text_color, font=("Arial", 12))
text_widget.pack()

# Exécutez la boucle principale de Tkinter
root.mainloop()
