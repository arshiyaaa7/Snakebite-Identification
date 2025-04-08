# 🐍 SnakeBite Identification

## 📑 Project Description
The SnakeBite Identification project is a machine learning-based application designed to identify whether a snakebite is from a venomous or non-venomous snake. This project leverages image processing and classification techniques to predict the type of snake using a trained model.

## 🌟 Features
- 🐍 Snakebite image classification
- 🧠 Machine Learning model for venomous/non-venomous prediction
- 🗃️ Dataset handling and preprocessing

## 💻 Technologies Used
- 🐍 Python
- 📦 OpenCV for image processing
- 🤖 Scikit-learn for model training
- 💾 NumPy and Pandas for data manipulation

## 🧠 Model Training
The Keras model used in this project was trained using Google's Teachable Machine. 

Model Training Image:
![Teachable Machine](https://github.com/user-attachments/assets/215b2b35-8d1c-4b67-ab28-14250a1de618)
Please collect the dataset from webscraping and create your own keras model.


## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arshiyaaa7/snakebite-identification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd snakebite-identification
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Usage
1. Run the Python script:
   ```bash
   python SNAKEBITEFINAL.py
   ```
2. Provide an input image of the snakebite.
3. View the prediction result: venomous or non-venomous.

## 🗂️ Folder Structure
```
SnakeBite-Identification/
├── .idea/
├── non venomous/
├── testing/
├── SNAKEBITEFINAL.py
├── labels.txt
├── image_2023-01-09_21-31-37.png
├── .gitignore
└── README.md
```

## 🧪 Testing
- Test images can be placed in the `testing` folder.
- The script will process and predict the type for each image.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## 🖼️ Images
Output for venomous snake 
![Venomous](https://github.com/user-attachments/assets/da049b42-c083-49f9-b60b-9b804ea95e41)

Output for Non venomous snake 
![Non - Venomous](https://github.com/user-attachments/assets/2d9e7fef-3b95-4613-8afd-66a9ce78ca04)

