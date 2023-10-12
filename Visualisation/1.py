# Impor library yang diperlukan
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Muat dataset
data = pd.read_csv("creditcard.csv")

# Bagi data menjadi fitur (X) dan label (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Bagi data menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Latih model pada data pelatihan
model.fit(X_train, y_train)

# Lakukan prediksi pada data pengujian
y_pred = model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Akurasi Model: {accuracy * 100:.2f}%')
print(f'Matrix Konfusi:\n{confusion}')
print(f'Laporan Klasifikasi:\n{report}')
