import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
import tkinter as tk
from tkinter import ttk, Label, Entry, Button

# Veri seti: Burçlar ve tarih aralıkları
burc_tarihleri = {
    "Koc": (datetime(2000, 3, 21), datetime(2000, 4, 19)),
    "Boga": (datetime(2000, 4, 20), datetime(2000, 5, 20)),
    "Ikizler": (datetime(2000, 5, 21), datetime(2000, 6, 20)),
    "Yengec": (datetime(2000, 6, 21), datetime(2000, 7, 22)),
    "Aslan": (datetime(2000, 7, 23), datetime(2000, 8, 22)),
    "Basak": (datetime(2000, 8, 23), datetime(2000, 9, 22)),
    "Terazi": (datetime(2000, 9, 23), datetime(2000, 10, 22)),
    "Akrep": (datetime(2000, 10, 23), datetime(2000, 11, 21)),
    "Yay": (datetime(2000, 11, 22), datetime(2000, 12, 21)),
    "Oglak": (datetime(2000, 12, 22), datetime(2001, 1, 19)),
    "Kova": (datetime(2001, 1, 20), datetime(2001, 2, 18)),
    "Balik": (datetime(2001, 2, 19), datetime(2001, 3, 20)),
}

# Veri setini hazırla
X = []
y = []
for burc, tarihler in burc_tarihleri.items():
    for tarih in pd.date_range(tarihler[0], tarihler[1]):
        X.append([tarih.month, tarih.day])
        y.append(burc)

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı sınıflandırıcı modelini oluştur
model = DecisionTreeClassifier()

# Modeli eğit
model.fit(X_train, y_train)

# Tkinter arayüzü
def tahmin_yap():
    dogum_ay = int(combo_ay.get())
    dogum_gun = int(combo_gun.get())
    dogum_yil = int(entry_yil.get())
    cinsiyet = combo_cinsiyet.get()

    tahmin = model.predict([[dogum_ay, dogum_gun]])
    label_sonuc.config(text=f"Tahmin edilen burcunuz: {tahmin[0]}")

# Ana pencere oluştur
root = tk.Tk()
root.title("Burç Tahmini")
root.configure(bg='#e6e6e6')

# Giriş etiketleri ve giriş kutuları
Label(root, text="Doğum Ayı:", bg='#e6e6e6').grid(row=0, column=0, padx=10, pady=10, sticky="e")
aylar = [str(i) for i in range(1, 13)]
combo_ay = ttk.Combobox(root, values=aylar)
combo_ay.grid(row=0, column=1, padx=10, pady=10, sticky="w")
combo_ay.set("1")

Label(root, text="Doğum Günü:", bg='#e6e6e6').grid(row=1, column=0, padx=10, pady=10, sticky="e")
gunler = [str(i) for i in range(1, 32)]
combo_gun = ttk.Combobox(root, values=gunler)
combo_gun.grid(row=1, column=1, padx=10, pady=10, sticky="w")
combo_gun.set("1")

Label(root, text="Doğum Yılı:", bg='#e6e6e6').grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_yil = Entry(root)
entry_yil.grid(row=2, column=1, padx=10, pady=10, sticky="w")

Label(root, text="Cinsiyet:", bg='#e6e6e6').grid(row=3, column=0, padx=10, pady=10, sticky="e")
cinsiyetler = ["Erkek", "Kadın"]
combo_cinsiyet = ttk.Combobox(root, values=cinsiyetler)
combo_cinsiyet.grid(row=3, column=1, padx=10, pady=10, sticky="w")
combo_cinsiyet.set("Erkek")

# Tahmin yap butonu
Button(root, text="Tahmin Yap", command=tahmin_yap, bg='#4CAF50', fg='white').grid(row=4, column=0, columnspan=2, pady=10)

# Tahmin sonucu etiketi
label_sonuc = Label(root, text="", bg='#e6e6e6', font=('Helvetica', 12, 'bold'))
label_sonuc.grid(row=5, column=0, columnspan=2, pady=10)

# Pencereyi çalıştır
root.mainloop()
